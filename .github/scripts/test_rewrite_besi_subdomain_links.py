#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

# Add canonical scripts dir to sys.path
SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "canonical" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from rewrite_besi_subdomain_links import (
    TextStyle,
    decode_document,
    encode_document,
    rewrite_bajabesi_links,
)


class TestRewriteBesiSubdomainLinks(unittest.TestCase):
    def test_rewrite_outbound_anchor_links(self):
        sample_html = (
            '<div class="elementor-widget-container">\n'
            '<a href="https://bajabesi.co.id/" target="_blank" rel="noopener">\n'
            '<img src="/wp-content/uploads/logo.png" alt="Layanan Logo Bajaesicoid Tentang">\n'
            '</a>\n'
            '</div>'
        )
        rewritten, count = rewrite_bajabesi_links(sample_html)
        self.assertGreater(count, 0)
        self.assertNotIn("bajabesi.co.id", rewritten)
        self.assertNotIn("Bajaesicoid", rewritten)
        self.assertIn('href="https://besi.co.id/"', rewritten)
        self.assertIn('alt="Layanan Logo Besi.co.id Tentang"', rewritten)

    def test_rewrite_subpath_links(self):
        sample_html = (
            '<p>Lihat profil kami di <a href="https://bajabesi.co.id/tentang/">Tentang Kami</a></p>\n'
            '<a href="http://bajabesi.co.id/produk/besi-beton/">Produk</a>'
        )
        rewritten, count = rewrite_bajabesi_links(sample_html)
        self.assertGreater(count, 0)
        self.assertNotIn("bajabesi.co.id", rewritten)
        self.assertIn('href="https://besi.co.id/tentang/"', rewritten)
        self.assertIn('href="https://besi.co.id/produk/besi-beton/"', rewritten)

    def test_rewrite_escaped_json_links(self):
        sample_html = (
            '<script>\n'
            'var config = {"partnerUrl":"https:\\/\\/bajabesi.co.id\\/partner"};\n'
            '</script>'
        )
        rewritten, count = rewrite_bajabesi_links(sample_html)
        self.assertGreater(count, 0)
        self.assertNotIn("bajabesi.co.id", rewritten)
        self.assertIn('"partnerUrl":"https:\\/\\/besi.co.id\\/partner"', rewritten)

    def test_idempotency(self):
        sample = (
            '<a href="https://bajabesi.co.id/" target="_blank">BajaBesi</a>\n'
            '<img alt="Layanan bajabesi.co.id">'
        )
        pass1, c1 = rewrite_bajabesi_links(sample)
        self.assertGreater(c1, 0)

        pass2, c2 = rewrite_bajabesi_links(pass1)
        self.assertEqual(c2, 0)
        self.assertEqual(pass1, pass2)

    def test_encoding_preservation(self):
        raw = b'\xef\xbb\xbf<a href="https://bajabesi.co.id/">Link</a>\r\n'
        content, style = decode_document(raw, "test.html")
        self.assertTrue(style.bom)
        self.assertEqual(style.newline, "\r\n")

        rewritten, _ = rewrite_bajabesi_links(content)
        re_encoded = encode_document(rewritten, style)
        self.assertTrue(re_encoded.startswith(b"\xef\xbb\xbf"))
        self.assertIn(b"\r\n", re_encoded)
        self.assertNotIn(b"bajabesi.co.id", re_encoded)


if __name__ == "__main__":
    unittest.main()
