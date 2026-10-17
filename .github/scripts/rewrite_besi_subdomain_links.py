#!/usr/bin/env python3
"""Canonical Engine: Rewrite Besi Subdomain Outbound Links from bajabesi.co.id to parent apex besi.co.id.

Sanitizes cross-domain footprint:
1. Subdomains of besi.co.id (e.g. plat.besi.co.id, grating.besi.co.id, bajaringan.besi.co.id)
   currently contain outbound hyperlinks pointing to https://bajabesi.co.id/.
2. Rewrites these links to their own parent apex domain https://besi.co.id/ (e.g. https://besi.co.id/).
3. Rewrites image alt tags referencing 'bajaesicoid' or 'bajabesi' to 'Besi.co.id'.
4. Preserves UTF-8 BOM, line endings (CRLF/LF), and guarantees 100% idempotency.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class TextStyle:
    bom: bool
    newline: str
    final_newline: bool


def fail(message: str) -> None:
    raise SystemExit(message)


def git_result(root: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def git_bytes(root: Path, *args: str) -> bytes:
    result = git_result(root, *args)
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", "replace").strip()
        fail(message or f"git {' '.join(args)} failed")
    return result.stdout


def decode_document(data: bytes, label: str) -> Tuple[str, TextStyle]:
    bom = data.startswith(b"\xef\xbb\xbf")
    payload = data[3:] if bom else data
    try:
        text = payload.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        fail(f"{label} is not strict UTF-8: {exc}")
    if "\r" in text.replace("\r\n", ""):
        fail(f"{label} contains unsupported bare carriage returns")
    has_crlf = "\r\n" in text
    has_lf = "\n" in text.replace("\r\n", "")
    if has_crlf and has_lf:
        fail(f"{label} contains mixed LF and CRLF newlines")
    normalized = text.replace("\r\n", "\n")
    return normalized, TextStyle(bom, "\r\n" if has_crlf else "\n", normalized.endswith("\n"))


def encode_document(normalized: str, style: TextStyle) -> bytes:
    body = normalized.replace("\n", "\r\n") if style.newline == "\r\n" else normalized
    encoded = body.encode("utf-8")
    return (b"\xef\xbb\xbf" if style.bom else b"") + encoded


def safe_relative_path(relative: str, label: str) -> PurePosixPath:
    if any(ord(char) < 32 or ord(char) == 127 for char in relative):
        fail(f"{label} contains a control character: {relative!r}")
    pure = PurePosixPath(relative)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        fail(f"unsafe {label}: {relative!r}")
    return pure


def tracked_html_paths(root: Path) -> List[str]:
    raw = git_bytes(root, "-c", "core.quotepath=false", "ls-files", "-z")
    candidates: List[Tuple[str, PurePosixPath]] = []
    for item in raw.split(b"\0"):
        if not item:
            continue
        try:
            relative = item.decode("utf-8", "strict")
        except UnicodeDecodeError:
            continue
        pure = safe_relative_path(relative, "tracked path")
        if pure.suffix.casefold() in (".html", ".htm"):
            candidates.append((relative, pure))
    ordered = sorted(candidates, key=lambda item: item[0].encode("utf-8"))
    return [item[0] for item in ordered]


def rewrite_bajabesi_links(content: str) -> Tuple[str, int]:
    """Rewrite bajabesi.co.id outbound links to parent apex besi.co.id."""
    modified = content
    replacement_count = 0

    patterns = [
        # href="https://bajabesi.co.id/..." -> href="https://besi.co.id/..."
        (re.compile(r'href=["\']https?://(?:www\.)?bajabesi\.co\.id/([^"\']*)["\']', re.IGNORECASE), r'href="https://besi.co.id/\1"'),
        (re.compile(r'href=["\']https?://(?:www\.)?bajabesi\.co\.id["\']', re.IGNORECASE), r'href="https://besi.co.id/"'),
        # Escaped JSON in Elementor config
        (re.compile(r'https?:\\/\\/(?:www\.)?bajabesi\.co\.id\\/', re.IGNORECASE), r'https:\/\/besi.co.id\/'),
        (re.compile(r'https?:\\/\\/(?:www\.)?bajabesi\.co\.id', re.IGNORECASE), r'https:\/\/besi.co.id'),
        # Alt tags referencing bajaesicoid or bajabesi
        (re.compile(r'alt=["\']([^"\']*)bajaesicoid([^"\']*)["\']', re.IGNORECASE), r'alt="\1Besi.co.id\2"'),
        (re.compile(r'alt=["\']([^"\']*)bajabesi\.co\.id([^"\']*)["\']', re.IGNORECASE), r'alt="\1Besi.co.id\2"'),
    ]

    for pattern, repl in patterns:
        matches = len(pattern.findall(modified))
        if matches > 0:
            modified = pattern.sub(repl, modified)
            replacement_count += matches

    return modified, replacement_count


def run(root: Path, apply: bool, check: bool) -> int:
    tracked_paths = tracked_html_paths(root)
    modified_files: List[str] = []
    total_rewritten = 0

    for relative_path in tracked_paths:
        file_path = root / relative_path
        if not file_path.is_file():
            continue
        try:
            data = file_path.read_bytes()
            content, style = decode_document(data, relative_path)
        except Exception:
            continue

        sanitized, count = rewrite_bajabesi_links(content)
        if sanitized != content:
            total_rewritten += count
            modified_files.append(relative_path)
            if apply:
                encoded = encode_document(sanitized, style)
                file_path.write_bytes(encoded)

    summary = {
        "repository": root.name,
        "files_scanned": len(tracked_paths),
        "files_modified": len(modified_files),
        "links_rewritten": total_rewritten,
    }
    print(json.dumps(summary, indent=2))

    if check:
        if modified_files:
            print(f"FAIL: Repository contains {len(modified_files)} files with un-rewritten bajabesi links.")
            return 1
        print("PASS: Repository has zero outbound links to bajabesi.co.id.")
        return 0

    if apply and modified_files:
        print(f"Successfully rewritten {total_rewritten} bajabesi links across {len(modified_files)} files to parent apex besi.co.id.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Rewrite bajabesi.co.id links to parent apex besi.co.id on subdomain repos.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Root directory of the repository.")
    parser.add_argument("--apply", action="store_true", help="Apply link rewrites in-place.")
    parser.add_argument("--check", action="store_true", help="Assert repository has zero bajabesi links.")
    args = parser.parse_args()

    exit_code = run(args.root.resolve(), apply=args.apply, check=args.check)
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
