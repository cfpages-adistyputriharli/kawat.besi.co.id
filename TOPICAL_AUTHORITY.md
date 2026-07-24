# Topical Authority — kawat.besi.co.id

## Role and boundary

`kawat.besi.co.id` is a Syamsul-owned product subdomain for practical education and commercial support around steel wire, welded mesh, woven mesh, reinforcement accessories, gabions, expanded metal, and wire rope in Indonesia. The authority layer must help buyers, designers, contractors, fabricators, operators, and asset owners identify products, specify them responsibly, procure verifiable material, install them safely, and manage them through end of life.

Knowledge articles remain non-geographic. Existing product and location routes own transactional enquiries; neutral articles must not imitate a quotation page, promise unverified grades, or manufacture city-swapped content. Structural capacity, lifting, security, geotechnical, and safety-critical decisions require competent professional review and project-specific calculations.

## Evidence audited

- Git branch and source: clean `main` at `cfe02527`, tracking `origin/main` at `cfpages-adistyputriharli/kawat.besi.co.id`.
- Repository inventory: 15,041 tracked files, including 6,267 HTML files, 112 XML files, and one pre-existing Markdown file (`README.md`).
- Root HTML: 5,906 files. Of these, 5,904 are geographic product templates and the remaining two are `index.html` and `hello-world.html`.
- Geographic template families: begel 490, bendrat 491, BRC 491, bronjong 490, expanded metal 491, harmonika 490, wiremesh 491, kawat duri 494, kawat ram 494, kawat loket 494, kawat stainless 494, and wire rope 494.
- Product hubs inspected: `/begel/`, `/bendrat/`, `/brc/`, `/bronjong/`, `/duri/`, `/expanded/`, `/harmonika/`, `/kawat-ram/`, `/kawat-stainless/`, `/loket/`, `/wire-rope/`, and `/wiremesh/`.
- Main sitemap evidence: `README.md` and `sitemap-complete.xml` each report 3,776 URLs. Eighteen post sitemaps contain 3,417 entries and `page-sitemap.xml` contains 11 entries.
- Archive evidence: 345 tracked category/author archive or pagination HTML pages. The repository also carries many overlapping `sitemap-detail-*.xml` files, so aggregate XML `<loc>` counts are not unique URL counts.
- Framework: static WordPress export with copied WordPress assets, archive routes, and mass-generated commercial pages rather than a source content collection.

## Existing coverage and risks

| Existing URL/pattern | Observed role/problem | Decision | Destination/owner | Verification needed |
|---|---|---|---|---|
| `/` | Broad supplier landing page and navigation hub | keep | Commercial home | Confirm live canonical, current product availability, and conversion tracking |
| `/{begel,bendrat,brc,bronjong,duri,expanded,harmonika,kawat-ram,kawat-stainless,loket,wire-rope,wiremesh}/` | Product-family sales hubs; useful commercial intent but claims need evidence | expand | Respective commercial hub plus KAW-03 through KAW-14 educational clusters | Verify specifications, photos, stock, certifications, and claims with supplier records |
| Root geographic product files | 5,904 location-swapped sales templates; strong duplication and doorway risk | manual review | Keep only pages with real local fulfilment evidence; consolidate or noindex unsupported variants | Check Search Console performance, backlinks, canonical response, local proof, and live deployment parity |
| `/category/**`, `/author/**`, pagination | 345 archive/pagination pages with thin or duplicated listings | noindex | Product hubs and article hubs | Confirm indexation, internal links, canonical tags, and whether any archive has external links |
| `hello-world.html` | Default WordPress residue without editorial value | remove | None; return 410 or redirect only if it has meaningful links | Check live status, traffic, and backlinks first |
| `sitemap-complete.xml`, `sitemap_index.xml`, `post-sitemap*.xml`, `sitemap-detail-*.xml` | Multiple overlapping sitemap systems can submit stale or duplicate URLs | merge | One canonical sitemap index containing only indexable canonical URLs | Compare live sitemap responses, modification dates, and Search Console submissions |
| WordPress asset copies and malformed `"wp-content` directory | Static-export residue increases weight and may contain unreachable duplicates | manual review | Minimal assets actually referenced by canonical pages | Run reference scan and production build/deploy comparison before removal |

## Coverage matrix

| Completeness lens | Owning topics | Coverage decision |
|---|---|---|
| Definition, vocabulary, history, measurement | KAW-01, KAW-16 | Distinguish wire, rod, mesh, rope, opening, diameter, coating, roll, sheet, and common Indonesian trade terms |
| Taxonomy and variants | KAW-01, KAW-03–KAW-14 | Each evidenced family receives an independent six-article cluster |
| Anatomy, materials, properties, mechanisms | KAW-02–KAW-14 | Explain wires, welds, twists, knots, strands, coatings, apertures, edges, and load paths without inventing performance |
| Need recognition, survey, requirements, selection | KAW-15, KAW-16 | Connect site purpose, exposure, dimensions, load, access, and service life to a specification |
| Budget, procurement, logistics | KAW-16, KAW-17 | Cover take-off, waste, comparable quotations, evidence packs, storage, and delivery |
| Fabrication, preparation, installation, handover | KAW-18 | Establish process checkpoints and stop conditions across families |
| Operation, inspection, maintenance, troubleshooting | KAW-19 | Build symptom-to-cause paths and repair-versus-replacement decisions |
| Upgrade, reuse, recycling, decommissioning | KAW-19, KAW-20 | Treat safe removal and material recovery as planned lifecycle stages |
| Stakeholders and building/site contexts | KAW-03–KAW-18 | Serve buyer, contractor, fabricator, designer, operator, owner, agriculture, civil works, and industrial contexts |
| Climate and exposure | KAW-02, KAW-07–KAW-14, KAW-19 | Address humid, rainy, coastal, polluted, immersed, and soil-contact exposure without city pages |
| DIY versus professional and quality levels | KAW-15, KAW-18, KAW-20 | State safe DIY limits; safety-critical design, lifting, structural, and geotechnical work needs competent review |
| Safety, standards, evidence, myths | KAW-02, KAW-16–KAW-20 | Require current primary standards, certificates, calculations, field evidence, and claim qualification |
| Editorial intents and formats | KAW-01–KAW-20 | Fundamentals, comparisons, calculators, diagrams, checklists, diagnostics, and commercial-support assets all have distinct owners |
| Geography-swapped editorial pages | N/A | Existing geographic sales templates are an audit problem; new knowledge briefs are deliberately non-geographic |

## Topical map

| Topic ID | Parent topic | Reader outcome | Required subtopics/questions | Evidence/formats | Boundary | Article target |
|---|---|---|---|---|---|---:|
| KAW-01 | Fundamentals and wire-product vocabulary | Correctly identify product forms and translate trade language into a usable starting requirement | Wire versus rod versus strand; mesh versus woven net; diameter and opening; roll, coil, and sheet; welded, woven, twisted, and expanded forms; reading labels | Illustrated glossary, taxonomy tree, comparison table, sourced explanation | Does not select material/coating (KAW-02), calculate quantities (KAW-16), or replace each family guide (KAW-03–KAW-14) | 6 |
| KAW-02 | Steel, stainless, coating, and corrosion | Select a defensible material/coating strategy for the exposure and expected life | Base metal; galvanizing and other finishes; stainless families; corrosion mechanisms; dissimilar-metal contact; coating damage; evidence and myths | Exposure matrix, corrosion diagrams, manufacturer data comparison, expert review | Does not specify stainless wire geometry (KAW-13), repair installed damage (KAW-19), or assert project suitability without professional review | 6 |
| KAW-03 | Wiremesh for concrete reinforcement | Understand welded reinforcement mesh and prepare questions for structural specification and installation | Sheet/roll forms; wire diameter and spacing; load path; laps and supports; cutting; placement; certificates; common defects | Anatomy diagram, calculation concepts, installation checklist, primary-standard review | Owns concrete-reinforcement mesh education; BRC fence panels belong to KAW-04 and structural design remains with the engineer | 6 |
| KAW-04 | BRC welded fence systems | Select and plan modular welded-mesh fencing without confusing it with reinforcement mesh | Panel anatomy; folds; post and clamp system; height/security; gates and corners; coatings; installation; inspection | System diagram, selection matrix, detail drawings, field checklist | Owns welded fence-panel intent; concrete wiremesh belongs to KAW-03 and other fence fabrics to KAW-08–KAW-11 | 6 |
| KAW-05 | Kawat bendrat | Specify and use tie wire appropriately in reinforcement and general tying tasks | Black versus coated wire; diameter; ductility; packaging; tying methods; tools; consumption; storage; breakage | Tool photos, workflow diagram, quantity worksheet, expert review | Owns temporary tying wire; does not design reinforcement cages (KAW-06), welded mesh (KAW-03), or permanent load-bearing connections | 6 |
| KAW-06 | Besi begel and reinforcement cages | Understand stirrup/begel forms and coordinate fabrication, spacing, and cage quality with structural documents | Shape vocabulary; dimensions; hooks; spacing; schedules; cutting/bending; cage assembly; tolerances; checks | Annotated drawing, schedule-reading guide, fabrication checklist, primary-standard review | Educational coordination only; engineer-approved reinforcement design governs, while bendrat tying belongs to KAW-05 | 6 |
| KAW-07 | Kawat bronjong and gabion systems | Plan a gabion solution from mesh selection through filling, drainage, inspection, and repair | Hexagonal mesh; lacing; diaphragms; stone fill; filter/drainage; foundation; deformation; corrosion; environmental interface | Section diagrams, site checklist, defect atlas, geotechnical expert review | Owns gabion-system education; site stability, hydraulic, and geotechnical design require professionals and are not sales claims | 6 |
| KAW-08 | Kawat duri | Choose and maintain barbed-wire barriers with explicit human/animal safety controls | Barbs and strands; spacing; post systems; tensioning; agriculture/security contexts; visibility; corrosion; legal/site controls | Anatomy diagram, safety checklist, comparison matrix, inspection guide | Owns barbed wire; chain-link belongs to KAW-09, welded fencing to KAW-04/KAW-11, and site security design to KAW-15 | 6 |
| KAW-09 | Kawat harmonika or chain-link mesh | Plan chain-link fencing from aperture and wire choice to tensioning and repair | Diamond mesh; selvage; posts; rails; tension wire/bars; gates; slope details; coatings; sagging and patches | Component diagram, detail set, material take-off, defect guide | Owns chain-link systems; welded panels belong to KAW-04/KAW-11 and general security zoning belongs to KAW-15 | 6 |
| KAW-10 | Kawat ram and lightweight wire netting | Match lightweight woven/netted wire to screening, animal, garden, and craft uses | Terminology; aperture; wire diameter; roll form; support frames; cutting edges; rust; animal containment limits; repair | Use-case matrix, anatomy photos, cutting/safety guide, comparison table | Owns lightweight netting sold as kawat ram; heavier chain-link is KAW-09 and welded square mesh is KAW-11 | 6 |
| KAW-11 | Kawat loket and welded square mesh | Select welded square mesh for cages, guards, partitions, and light barriers | Aperture/diameter; panel versus roll; weld quality; frame attachment; cutting; coatings; loads; damage | Selection matrix, weld-detail photos, fabrication checklist, expert review | Owns light welded square mesh; structural wiremesh is KAW-03, BRC fence panels KAW-04, expanded metal KAW-12 | 6 |
| KAW-12 | Expanded metal | Specify expanded sheet by opening, strand, thickness, profile, and application | Manufacturing mechanism; SWD/LWD concepts; raised/flattened; open area; orientation; edges; grating/guard/facade uses; finishes | Dimension diagram, sample-measurement guide, comparison table, fabrication details | Owns slit-and-stretched metal sheet; welded/woven mesh belongs to KAW-03/KAW-04/KAW-09/KAW-11 | 6 |
| KAW-13 | Stainless steel wire | Choose stainless wire for corrosion, hygiene, heat, fabrication, and finishing constraints | Grade evidence; temper; diameter; surface; magnetism myths; forming/welding; contamination; storage; application limits | Grade decision matrix, certificate checklist, manufacturer comparison, expert review | Owns stainless wire material/product decisions; general corrosion is KAW-02 and wire rope construction is KAW-14 | 6 |
| KAW-14 | Wire rope or steel cable | Understand rope construction, selection evidence, handling, inspection, and retirement boundaries | Wires/strands/core; lay; diameter; terminations; sheaves/drums; lubrication; broken wires; storage; lifting controls | Anatomy diagram, inspection checklist, manufacturer manual comparison, competent-person review | Owns wire-rope education; never supplies an unsupervised lifting design, capacity promise, or retirement threshold without current authoritative criteria | 6 |
| KAW-15 | Application and system selection | Select the right family by function, threat, exposure, access, life, and maintenance rather than by name alone | Fence, screen, reinforcement, tying, erosion, guards, animal control, facade, lifting; new build/retrofit; security zones; alternatives | Decision tree, stakeholder matrix, requirement worksheet, comparison table | Owns cross-family choice; detailed specifications remain with KAW-02–KAW-14 and quantities with KAW-16 | 6 |
| KAW-16 | Measurement, specification, and quantity planning | Turn dimensions and requirements into a reviewable specification and quantity estimate | Diameter/opening measurement; tolerances; area/length; laps/waste; posts/fixings; weight concepts; drawing/spec sheet; estimator limits | Measurement diagrams, calculators, worked examples, specification template | Owns measurement and take-off methods; pricing/vendor checks are KAW-17 and engineering capacity stays with competent designers | 6 |
| KAW-17 | Procurement, quality evidence, storage, and logistics | Compare quotations and receive material without substituting evidence with marketing claims | RFQ scope; certificates; samples; inspection; batch traceability; tolerances; packaging; transport; storage; claims; handover | RFQ template, bid-comparison table, receiving checklist, document register | Owns buying and receipt assurance; product selection is KAW-02–KAW-15 and installation acceptance is KAW-18 | 6 |
| KAW-18 | Fabrication, installation, and handover | Plan safe sequencing and quality checkpoints from preparation through acceptance | Survey; cutting/forming/welding; frames/supports; tensioning; fixing; coating repair; interfaces; punch list; records; stop conditions | Method-statement outline, ITP/checklist, detail diagrams, toolbox-talk prompts | Owns execution workflow; design/specification remains KAW-03–KAW-16 and in-service defects belong to KAW-19 | 6 |
| KAW-19 | Inspection, maintenance, failure, and repair | Diagnose common symptoms, control deterioration, and decide repair versus replacement | Corrosion; broken wires/welds; sagging; looseness; deformation; blocked gabions; damaged coatings; intervals; records; retirement | Symptom-cause matrix, inspection forms, defect atlas, decision tree | Owns installed-asset care; initial installation is KAW-18, material selection KAW-02, and worker/end-of-life safety KAW-20 | 6 |
| KAW-20 | Safety, environment, and end of life | Control sharp-edge, tension, lifting, exposure, public, animal, waste, and decommissioning risks | PPE hierarchy; stored energy; cutting/grinding/welding; lifting; exclusion zones; public visibility; contamination; reuse/recycling; disposal records | Hazard register, stop-work checklist, decommissioning plan, primary safety guidance | Owns cross-family risk controls; does not replace task-specific regulations, competent supervision, structural design, or product manuals | 6 |

## Related-domain opportunities

- `besi.co.id` may independently explain the broader steel supply chain and material taxonomy; cross-link only when the reader needs context beyond wire products.
- `batang.besi.co.id`, `bajaringan.besi.co.id`, and other product subdomains may independently cover reinforcement or fabrication from their own entity perspective. Overlap across domains is allowed and is not same-domain cannibalization.
- Construction properties using fences, concrete, erosion control, screens, or lifting systems can contribute real project details, original photos, and verified case evidence. Do not invent shared project experience.
- Where a family has its own commercial hub on this domain, that hub receives contextual links from educational selection/procurement articles but remains the sole owner of quote intent.

## Consolidation plan

1. Verify which sitemap is actually submitted and generate one canonical sitemap index from indexable canonical URLs.
2. Segment the 5,904 geographic pages by impressions, clicks, backlinks, uniqueness, fulfilment evidence, and conversion value. Preserve proven pages; merge, noindex, or retire unsupported templates in controlled batches.
3. Keep each product hub as the commercial owner and add a clearly distinct educational hub for its KAW topic.
4. Noindex low-value category, author, and pagination archives unless a specific archive demonstrates unique navigational value.
5. Remove `hello-world.html` only after confirming it has no useful history; audit malformed/copied assets before deleting them.
6. Publish the bounded first cluster before scaling. Re-run same-domain title, slug, and SERP-intent audits after every wave.

## Internal-link architecture

- A central “jenis kawat dan mesh” hub links to KAW-01, KAW-02, and every family hub; each family hub links back and to its six children.
- KAW-15 routes readers from application requirements to the correct family. It links laterally to KAW-16 for quantities and KAW-17 for procurement.
- Every product guide links to its relevant measurement, installation, inspection, and safety article instead of receiving one repeated generic link list.
- Diagnostic pages in KAW-19 link backward to material choice (KAW-02), execution controls (KAW-18), and forward to repair/replacement and decommissioning (KAW-20).
- Commercial product hubs receive links only from relevant selection, specification, and procurement education; articles do not duplicate quote calls or location landing-page intent.
- Existing location routes should link upward only when a page is retained and the product hub/article genuinely helps the local buyer.

## Evidence and editorial standards

- Verify current SNI, ISO, ASTM, manufacturer, occupational-safety, lifting, structural, and project requirements from primary sources before naming a designation, clause, capacity, tolerance, inspection threshold, or retirement rule.
- Label rule-of-thumb calculations as estimates; publish assumptions, units, waste factors, and stop conditions. Engineering outcomes require competent review.
- Use certificates, batch documents, calibrated measurements, original close-up photos, and manufacturer data where product claims matter.
- Never fabricate field tests, prices, warranties, case studies, stock, grade equivalence, corrosion life, or local service evidence.
- Show dangerous tasks with hierarchy-of-control thinking. Cutting, welding, tensioning, lifting, work at height, sharp edges, and public barriers require explicit stop conditions.
- Date volatile commercial or regulatory information and assign an update owner.

## First bounded publication cluster

Wave 1 contains 14 assets: KAW-01-01, KAW-01-02, KAW-02-01, KAW-02-02, KAW-03-01, KAW-04-01, KAW-07-01, KAW-09-01, KAW-12-01, KAW-14-01, KAW-15-01, KAW-16-01, KAW-17-01, and KAW-20-01.

This cluster establishes the shared vocabulary, material/exposure logic, representative family guides, cross-family selection path, measurement and buying controls, and a safety baseline. It is coherent enough to link as a reference path while remaining small enough for original diagrams, verified sources, and human technical review.

Monitor indexation and canonical selection, impressions by distinct intent, click paths from family guides to measurement/procurement content, estimator or checklist completion, qualified product enquiries, engagement with diagrams, and query/page overlap. Ranking alone is not the finish signal.

## Definition of done

- All 20 topics have six published, evidence-backed articles or a documented merge decision.
- All 120 catalog IDs, titles, slugs, intents, boundaries, evidence plans, and related IDs remain unique and valid.
- Every knowledge asset has a parent hub and contextual lateral/lifecycle links; no article is orphaned.
- Product hubs own commercial quote intent; retained location routes have verified local value and no knowledge brief imitates them.
- Sitemaps contain only live, canonical, indexable URLs; archive and geographic-template decisions are implemented and measured.
- Safety-critical, structural, geotechnical, and lifting claims have current primary evidence and competent review.
- Search Console shows no unresolved same-domain cannibalization cluster after each publication wave.
