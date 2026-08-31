# Update guide

What file to edit for any given task. After editing, push:

```bash
git add . && git commit -m "brief note" && git push
```

Or edit directly in the GitHub browser UI for small changes.

---

## Hero tagline

`content/_index.md` → the `title:` line inside the `block: hero` section.

---

## Hero photo

The homepage hero is `content/_index.md` → the first `block: hero` section → `design.background.image.filename`. It currently points to `lab/david-with-colleague.jpg`.

To swap it: drop the new photo in `assets/media/lab/`, then update `filename:` to match. Landscape photos with a clear subject work best — the text sits centered over the middle of the image, so avoid photos where the important content is in a narrow strip (see "Hero gotchas" below).

**Do not delete or reorder** `filters:`, `color:`, `position:`, `no_padding:`, or the `border-bottom`/`::after` overlay rules in `assets/css/custom.css` (search for `#about`) unless you mean to change the look — see gotchas below for why.

---

## Navigation

`config/_default/menus.yaml` — each entry has `name`, `url`, and `weight` (lower = further left).

---

## Add a lab member

1. Create `data/authors/firstname-lastname.yaml` — copy an existing file (e.g. `data/authors/haeun-kim.yaml`) as a template rather than starting from scratch, since the real schema has more fields than shown here:

```yaml
schema: hugoblox/author/v1
slug: firstname-lastname
avatar_filename: firstname-lastname.jpg
name:
  display: Firstname Lastname
  family: Lastname
role: PhD Student
bio: One or two sentences on research focus.
affiliations:
  - name: Albert Einstein College of Medicine
interests:
  - Topic one
  - Topic two
user_groups:
  - PhD Student
```

Use `name.family` (not `last_name`) — that's the field the theme's sort-by-surname logic actually reads on the People/homepage team blocks.

**The Current Lab Members and Alumni sections on `content/people.md` are both `team-showcase` blocks filtered by `user_groups:`** — Current shows everyone whose `user_groups` list includes `Current`, Alumni shows everyone whose list includes `Alumni`. Every current member's file needs `Current` in `user_groups` (in addition to whatever role tag they already have, e.g. `PhD Student` — the extra tags don't hurt, only `Current`/`Alumni` are actually filtered on). Without that tag, a person's card won't show up anywhere, even though their file exists. `role` is still shown on each person's card (and used in their bio sentence), so set it to whatever's accurate for them (e.g. `PhD Student`, `MD-PhD Student (MSTP)`, `Postdoctoral Fellow`) — it no longer has to match an exact list of allowed values.

**Sort order:** both blocks use `sort_by: 'weight'`. David (`david-shechter.yaml`) has `weight: 1` and Subray (`subray-hegde.yaml`) has `weight: 2`, so they always appear first, in that order among current members. Everyone else has no `weight` field at all — the theme treats a missing weight as "very large," which pushes them after David/Subray, and sorts everyone in that tied group alphabetically by `name.family`. **This means new lab members need no `weight` field and no manual reordering** — just add their file with `Current` in `user_groups` and they'll automatically slot in alphabetically after David and Subray. Only add a `weight:` to someone else if you specifically want them pinned before the alphabetical group too. Alumni cards are also weight-sorted, but that list is small enough that each alumni file sets an explicit `weight:` matching the order they appear in on the CV/original table — there's no alphabetical fallback logic to lean on there.

2. Drop a headshot at `assets/media/authors/<slug>.jpg` — 600×600 px, JPG, ~85% quality, under 200 KB, where `<slug>` is the **exact filename stem of the YAML file** (not the `slug:` field inside it, and not necessarily the person's name — see the gotcha below about David's own photo). If there's no headshot yet, skip this — the theme shows a colored initials placeholder automatically (this is normal, not a broken image; see gotchas below). This is exactly how alumni photos work too, when you have them — same file, same 1:1 crop, same fallback if you don't.

---

## Update a lab member

Edit `data/authors/<slug>.yaml`. Swap photo: replace `assets/media/authors/<slug>.jpg`.

---

## Move someone to alumni

In their `data/authors/<slug>.yaml`, change `user_groups` from `Current` to `Alumni`, add a `weight:` (see sort order above — put them at the end of the existing alumni sequence, i.e. one higher than the current highest), and update their `role:` to include their dates in the lab (e.g. `"Postdoctoral Fellow, 2021–2025"`) and their `affiliations:` to a single `"Now: <where they went>"` entry — that's what shows as the line under their name on the Alumni card. Their photo (if they have one) carries over automatically; no separate step needed. This replaced an earlier version of this page that used a plain markdown table for alumni with no photos — now both sections use the same card mechanism.

---

## Add a publication

Create a folder `content/publications/your-paper-slug/` with an `index.md`. Copy an existing entry (e.g. `content/publications/gnmt-folate-methyl-donor-2026/index.md`) as your starting point — the real schema is more specific than it looks:

```yaml
---
title: "Full paper title, exactly as published"
authors:
- "First Author Name"
- "Second Author Name"
- "David Shechter"   # David's own name, like everyone else's — it maps to data/authors/david-shechter.yaml
date: "2026-01-01T00:00:00Z"
publishDate: "2026-01-01T00:00:00Z"
publication_types: ["article-journal"]   # or ["article"] for a preprint
pub_category: lab   # lab | coauthored | review — see below
publication: "*Journal Name, volume*(issue), pages"   # markdown italics around the journal name
abstract: "The actual published abstract — copy it verbatim from the paper, don't paraphrase or invent one."
summary: "One sentence for the card preview."
tags:
- Topic tag
featured: false
links:
- name: Article        # or "bioRxiv" for a preprint — this is the visible label
  type: doi             # or "preprint" for a bioRxiv/arXiv link — this picks the icon; see below
  url: https://doi.org/10.xxxx/xxxxx
image:
  filename: "research/nucleosome-cartoon.jpg"
  focal_point: ""
  preview_only: false
projects: []
slides: ""
---
```

There is **no `doi:` field** — the DOI goes inside `links:` as a full URL, not as a bare identifier. Set `featured: true` to show the paper in the homepage publications strip. Double-check `publication:`, the date, and the DOI against the actual journal page (or PubMed/PMC) before publishing — several of these had wrong dates/volumes from earlier drafting and had to be corrected against the real record.

Every `links:` entry needs both `name:` (the visible label — "Article", "bioRxiv", etc.) and `type:` (`doi` for a published article, `preprint` for bioRxiv/arXiv — this is what picks the icon). `name:` alone still displays fine but silently falls back to a generic link icon instead of the one that actually matches what the link is.

**`pub_category:`** controls which section of the `/publications/` list page an entry appears in (see `layouts/publications/list.html`, a local override). `pub_category: review` is checked first, so a review-ish item that is not a journal article — a book chapter, an application note — still lands under Reviews & Commentary. Anything else without `publication_types: ["article-journal"]` is grouped under "Preprints":
- `lab` (default if omitted) — first-author or corresponding-author work driven by the lab. Shown under "Lab Papers".
- `coauthored` — genuine collaborations where David is a middle author, not the paper's driver. Shown under "Co-authored Work".
- `review` — reviews, commentaries, book chapters. Shown under "Reviews & Commentary".

Each section is independently grouped by year and only renders at all if it has at least one entry, so adding the first `coauthored` or `review` publication is enough to make that heading appear — no template changes needed. The jump-links bar across the top of the page follows the same rule automatically (it's generated from the same non-empty checks), so there's nothing extra to update there either.

---

## Update a publication status (preprint → published)

Open `content/publications/<slug>/index.md` and edit:
- `publication_types:` from `["article"]` to `["article-journal"]`
- `publication:` from `"*bioRxiv*"` to the journal citation, e.g. `"*Nature Communications, 17*(1), 1234"`
- `date:` / `publishDate:` to the journal's online-publish date (not the bioRxiv posting date)
- `links:` — add or replace with the journal DOI (`name: Article`, `type: doi`); you can keep the bioRxiv link as a second entry (`name: bioRxiv`, `type: preprint`) if useful

---

## Add a news item

Create `content/news/YYYY-MM-description.md`:

```yaml
---
title: 'Headline'
date: 2026-07-01
tags: [People]   # People | Preprint | Grant | Talk | Revision | Upcoming
summary: 'One sentence shown in the news list.'
image:
  filename: "lab/some-existing-photo.jpg"   # see assets/media/lab/ for what's available
  focal_point: Smart
---

Body text in markdown.
```

**Always set `image:`.** Without it, the card falls back to a generic gray gradient placeholder — every news item once had this problem until photos were added retroactively. Reuse an existing photo from `assets/media/lab/` or `assets/media/research/` rather than leaving it unset.

The news list (`content/news/_index.md`) shows the most recent 20 items sorted by date, newest first — there's no automatic archiving of older items, so the list just grows. If it gets long, consider lowering `count:` in that file's `collection` block or adding pagination, but nothing does this automatically today.

---

## Add a Lab Life photo

This page is **not** a Hugo Blox photo-gallery block — it's a hand-built HTML grid inside `content/lab-life/_index.md`'s single `block: markdown` section. To add a photo:

1. Drop the JPG into `assets/media/lab/`.
2. In `content/lab-life/_index.md`, copy one of the existing `<figure>...</figure>` blocks inside the `<div style="display:grid;...">` and edit its `img src` (path is `/media/lab/<filename>.jpg`) and `<figcaption>` text.

The grid is fixed at 2 columns regardless of how many photos are in it — with an odd number, the last one just doesn't have a pair. There's no cropping/resizing step, so use images that are already reasonably sized and roughly landscape/square; a huge original will slow the page down since nothing resizes it for you.

There's also `content/lab-life/archive.md` (`/lab-life/archive/`) for photos from prior years, linked from both the current Lab Life page and the People page. It's currently a placeholder ("Photos to be added") — same hand-built grid pattern as above once there's something to put in it.

---

## Contact page

`content/contact.md` — edit the markdown block directly. The email is encoded as HTML entities to block scrapers. To change the address, re-encode it — paste the new address into an HTML encoder (e.g., mothereff.in/html-entities) and replace the entity string.

---

## Update the CV PDF

Replace `static/uploads/shechter-cv-2026.pdf`. Keep the filename so existing links hold. To rename it, update any references in `content/contact.md`.

---

## Funders strip

`content/_index.md`, section `id: funders` ("Supported by"), and the matching Funding section on `content/research/_index.md` — both are plain `block: markdown` with a centered, dot-separated list of `[Name](url)` links. Add, remove, or reorder entries by editing that list directly.

**This is deliberately not `block: logos`,** the vendored Hugo Blox block that name suggests. That block requires an `image:` per entry — if you don't give it one, the entry renders as an *invisible* clickable box (a `title` attribute a mouse-hover shows, nothing else — there's no plain-text fallback in the vendored template). We don't have logo image files for any of these funders, and both sections rendered completely empty this way for a long time before anyone noticed (the section title showed, the actual funder list didn't). If you ever do get real logo files and want the logo-grid look back, switch back to `block: logos` and note it uses `logos:` as the list key, not `items:` — that was the original bug here, easy to reintroduce by copying a `research-areas` or similar block's `items:` pattern by habit.

---

## Research area text

The lab's research is organized as two mechanistic programs and three disease-focus areas, each with its own file in `content/research/`:

- **Mechanism:** `arginine-methylation.md` (PRMTs, GNMT, methylation in gene regulation and RNA processing), `glutamylation-chaperones.md` (glutamylation, histone chaperones, disordered regions)
- **Disease focus:** `aml.md` (NPM1-mutant AML), `als.md` (C9orf72 ALS), `aging.md` (aging and one-carbon metabolism)

Edit the body or the `summary:` in front matter for any of these directly. The homepage (`content/_index.md`) has two separate `block: research-areas` sections — **Disease Focus comes first** (ALS, then AML, then aging), **Research Areas comes second** (the 2 mechanism cards) — each card's `cta.url` links to the matching page above. If you rename a research page's filename (which changes its URL), update the matching `cta.url` in both places.

`methyl-economy.md` still exists in `content/research/` but isn't linked from anywhere on the site (its content was folded into `arginine-methylation.md`'s GNMT section) — it's an orphan page, reachable only by direct URL, kept in case it's useful as a deeper reference later.

Both `research-areas` blocks render through a **local override** of the vendored block (`layouts/_partials/hbx/blocks/research-areas/block.html`) — a compact card style (small icon/image square beside the title, smaller text) rather than the vendored version's big banner-image card. Only the "cards" layout is ported; `design.layout: hexagon` or `timeline` won't render anything useful here. Each card can carry an `image:` field (page-bundle path, `assets/media/...` path, or a remote URL) instead of `icon:` — set it and a real photo/figure replaces the gradient icon square automatically, no template changes needed.

**`content/research/_index.md`** is its own `type: landing` page (not the generic auto-listing archive it used to be) with five hand-built `block: markdown` sections: an overview (David's Einstein faculty-bio text, expanded with CV detail) with a jump-nav row, brief link lists to the Molecular Research Areas and Disease Focus pages, Collaborators, and Funding (current grant support, pulled from the CV — dollar amounts intentionally left off, matching how the homepage funders strip handles this). If you add/remove a research page, update the matching bullet list here too — there's no automatic sync between this page and the actual `content/research/*.md` files anymore, since converting to `type: landing` turned off the auto-listing.

Research detail pages (`content/research/*.md`) render through their own local override too (`layouts/research/single.html`), with a smaller prose size than the sitewide default — this only affects the Research section, not projects/publications/news. That override also supports a `image:` front-matter field (same `filename`/`focal_point` shape as projects and publications) — set it and a contained figure renders below the title, above the body text. No research page has one yet.

Einstein faculty links (in `content/_index.md`'s Collaborators section and the matching one on `content/research/_index.md`) use the real `einsteinmed.edu/faculty/<id>/<slug>` URL pattern, not the shorter `einsteinmed.edu/faculty/<lastname>` guess that seven of these links originally used (all silently 404ing). If you add a new Einstein collaborator, look up their actual numeric faculty ID rather than guessing the URL — the short form doesn't resolve.

---

## Resources page

`content/resources.md` — plain markdown. Add new protocol links, datasets, or tools directly to the table.

---

## Renaming or moving a page (keep the old URL working)

If a page's URL changes, add the old path to `aliases:` in its front
matter. Hugo generates a redirect at the old address, so links in
published papers, emails, and other people's sites keep working.

```yaml
---
title: "NPM1-mutant Acute Myeloid Leukemia"
aliases:
  - /research/leukemia/
  - /aml/
---
```

Keep the leading and trailing slashes, and list every old path a page
has ever had — aliases cost nothing and there is no way to know which
one someone bookmarked.

**Do not hand-edit `_redirects`.** On this site `disableAliases: true`
is set in `config/_default/hugo.yaml`, so Hugo does not write the usual
meta-refresh redirect pages. Instead the `redirects` output format
(`outputs.home` in the same file) collects every `aliases:` entry in the
site and writes them into `public/_redirects` at build time, where
Netlify serves them as real 301s — better than a meta refresh for both
browsers and search engines. That file is generated on every build, so
anything typed into it by hand is overwritten and lost. Front matter is
the only place to put a redirect.

Verify after a rename by checking the built file:

```bash
hugo --gc --minify && cat public/_redirects
```

---

## HTTPS and security headers

Two halves, in two different places.

**The certificate is Netlify's job, in the UI.** Site configuration → Domain
management → HTTPS. Once DNS points at Netlify it provisions a Let's Encrypt
certificate automatically and renews it forever; if it has not, use "Verify DNS
configuration" then "Provision certificate". Turn **Force HTTPS** on in the same
panel so `http://` is redirected rather than served.

**The headers are this repo's job.** `layouts/index.headers` generates
`public/_headers`, which Netlify reads at deploy time. Values come from
`config/_default/params.yaml` under `hugoblox.security` — edit them there, not
in the generated file. Currently shipping:

| Header | What it does |
|---|---|
| `Strict-Transport-Security` | after one visit, the browser refuses plain HTTP for a year |
| `Content-Security-Policy` | only lets the page load scripts, styles, fonts and images from listed origins |
| `X-Frame-Options: DENY` | no one can embed the site in an iframe |
| `X-Content-Type-Options: nosniff` | browser trusts declared MIME types instead of guessing |
| `Referrer-Policy` | no full URL leaks to other sites |
| `Permissions-Policy` | camera, microphone, geolocation etc. denied outright |

**Two things not to "improve" without reading first.**

`Strict-Transport-Security` has **no `includeSubDomains`**, on purpose — see the
comment in `layouts/index.headers`. The apex serves the redirect to www, so that
directive would cover every `*.shechterlab.org`, including the Fastmail-hosted
subdomains this site neither serves nor controls. And never add `preload`: it is
effectively permanent.

The **CSP is the thing that breaks when you add a widget.** Any new external
script, font, embed or analytics tag is blocked silently — no error on the page,
the resource simply never loads. Add its origin to the right directive in
`params.yaml` at the same time you add the widget. Note every directive there
must sit on one line at the same indentation: a line indented deeper becomes a
literal newline inside the header value and truncates the policy.

## Who is allowed to crawl the site

`layouts/robots.txt` is a local template (Hugo builds robots.txt because
`enableRobotsTXT: true` is set). The policy: search engines and the AI
assistants that **cite and link back** are allowed; crawlers that only harvest
text into a training corpus are blocked.

Two things to know before editing it:

- **A crawler obeys exactly one group** — the one naming its own product
  token — and falls back to `User-agent: *` only when nothing names it
  (RFC 9309). So a named bot ignores the `*` group entirely, and group order
  in the file does not matter.
- **It is a blocklist over an open default.** Search engines keep working
  without being enumerated, but a brand-new scraper is allowed until someone
  adds it. Glance at Netlify's traffic analytics now and then and extend the
  list.

Watch the vendor split: OpenAI's `GPTBot` and Anthropic's `ClaudeBot` are the
training crawlers and are blocked, while `OAI-SearchBot`/`ChatGPT-User` and
`Claude-SearchBot`/`Claude-User` from the same vendors are allowed.
`Google-Extended` and `Applebot-Extended` are **training opt-out tokens only** —
blocking them does not affect Google Search or Siri, which use `Googlebot` and
`Applebot`.

**robots.txt is a request, not a fence.** Several crawlers are documented as
ignoring it (Bytespider is the usual offender). To actually stop one, use
Netlify's user-agent blocker: Site configuration → Traffic → User agent
blocker, and add the token there. Do that only for bots you can see in the
analytics ignoring the file — every rule is another thing to maintain, and the
blocker cannot tell a spoofed user-agent from a real one either.

## Sitewide settings (colors, fonts, social links)

`config/_default/params.yaml` → `hugoblox.theme.colors` for brand colors and `hugoblox.identity.social` for social links/SEO.

- **Primary (teal, buttons/badges):** `primary: "#155e75"` in `params.yaml`.
- **Secondary (orange, in-content links, "Read more" links, hero trim/button):** `secondary: "#c2410c"` in `params.yaml`, applied via `assets/css/custom.css` (search for `--color-accent`). The two files have to agree — changing one without the other will leave the accent color inconsistent between buttons/badges and links.
- **Fonts:** headings are IBM Plex Serif, body text is Inter, both set in `assets/css/custom.css` (`--font-display` / `--font-body`). The theme also has its own font-pack system (`hugoblox.typography` in `params.yaml`, packs listed under the module's `data/fonts/`) but it is **not** what's actually controlling the fonts on this site — `custom.css` overrides it. If fonts ever look wrong after an edit, check `custom.css` first, not `params.yaml`.

---

## Known gotchas

Things that look like they should work but will silently break the layout or produce wrong output — found the hard way, so future edits don't reintroduce them.

- **Hero padding doubles up if you're not careful.** The hero section's own component adds large top/bottom padding automatically. `content/_index.md`'s hero block has `no_padding: true` specifically to disable that, and controls spacing itself via `design.spacing.padding`. If you remove `no_padding: true`, the hero becomes roughly twice as tall as it should be — this happened once already.
- **A `background.color` on a hero/section with a full-size photo does nothing visible.** The color paints *behind* the image, and an opaque photo covers it completely. The hero's actual teal tint comes from a CSS overlay in `assets/css/custom.css` (search `#about`), not from the `color:` field in `content/_index.md`. If you want to change the tint, edit the `linear-gradient(...)` in that CSS block.
- **Any `statistic:` value in a `block: stats` that's 1000 or more gets a comma inserted** (e.g. a bare year like `"2009"` renders as `"2,009"`). This is a bug in the vendored Hugo Blox stats counter — it animates the number through `Intl.NumberFormat`, which comma-groups anything ≥ 1000, and there's no per-item way to opt out. Keep big numbers/years out of `statistic:` — put them in `description:` or `sub_metric:` instead (those aren't animated or formatted). See how the "Years at Einstein" stat on the homepage is split for the pattern to copy.
- **A missing headshot is not a bug.** If `data/authors/<slug>.yaml` has no `avatar_filename`, or the file listed doesn't exist, the team card shows a colored circle with the person's initials instead of a photo. That's the theme's intended fallback, not broken image loading.
- **A missing `image:` on a news/publication/project entry is not a bug either**, but it does make the card look worse — it falls back to a generic gray gradient. Always set one (see "Add a news item" above).
- **The `Contact` link only lives in one place on purpose.** It used to appear both as a nav-bar link and as the header's `Contact` button (both pointing to `/contact`), which read as a mistake. The nav-bar entry was removed; if `Contact` reappears in `config/_default/menus.yaml`, it'll be duplicated again.
- **`/publications/` and `/projects/` are set to text-only views on purpose.** Both `_index.md` files have `view: citation` / `view: date-title-summary` in their front matter. Without that line, Hugo Blox's default archive template falls back to `view: card`, which shows a big image above every single entry — and since every publication/project reuses the same placeholder image, that made the whole list look repetitive and hard to scan. If you add a real, distinct photo/figure for an entry and want it to actually show, you'd need to switch that entry's list back to a view that renders images (`card`) — the per-item `image.preview_only: true` (see below) would also need removing.
- **`image.preview_only: true` hides the figure from the article body, not from search/social previews.** Every publication and project has this set — the big banner image that used to sit above the abstract/body text on each detail page is now suppressed, but the image is still available for link-preview (OG) metadata. Leave it `true` unless you specifically want a figure to show inline.
- **The publications citation format (`layouts/_partials/views/citation.html`) is a local override, not the stock Hugo Blox one.** It exists only to bold the title/journal/year in the Publications list. Because it's a full copy of the vendored file living at the same path in our own repo, Hugo always prefers ours — which also means it will **not** pick up any future upstream fixes/improvements to that file automatically. If citations ever look broken after an `hugo mod get -u`, compare this file against the current vendored copy under `$(hugo mod vendor)`'s cache and re-apply the bold/underline changes by hand.
- **To pull a project or publication off the site without deleting it, set `draft: true`** in its front matter (see `content/projects/methyl-economy/index.md`). Hugo excludes drafts from the build entirely — the page won't render at its URL, won't appear in any list, and won't 404-link from anywhere. Remove the line to bring it back.
- **The Projects list shows a small thumbnail instead of a date, and it's also a local override.** `layouts/_partials/views/date-title-summary.html` replaces the vendored view (same override mechanism as the citation view above) so it pulls each project's featured image (`image.filename`) into a small square next to the title/summary instead of the publish date. Right now all 4 projects reuse the same generic placeholder (`assets/media/research/nucleosome-cartoon.jpg`), so the thumbnails all look identical — give a project a real, distinct image via its `image.filename` front matter to make this useful. This view is only used for Projects; it does not affect news, publications, or anything else.
- **The Publications list bibliography does not (yet) include everything in the CV.** Original-research entries (Lab Papers, Co-authored Work, Preprints) start from 2010, verified against the CV (`static/uploads/shechter-cv-2026.pdf`) and a PubMed export cross-check — David's own scoping call on where the lab's own experimental work starts, plus the one 2007 Nature Protocols methods paper that predates that cutoff but is still commonly cited. Reviews & Commentary is scoped more broadly and does include earlier ones from David's graduate work with Jean Gautier and postdoc with C. David Allis (2004-2007) — those are explicitly wanted even though the primary-research papers from that era are not. When adding older papers, check both the CV and PubMed for the real DOI/date/author order — don't invent one from the title alone.
- **The People page photo is a contained image, not a `block: hero`.** It used to be a full-bleed banner with a fixed short height (`css_class: 'h-64 md:h-80'`) that force-cropped the group photo to fill that width — with a wide landscape photo, that crops off people's heads. It's now a plain `<img>` inside the page's `block: markdown` section, capped at `max-width:640px` so the whole photo shows at its real aspect ratio. If you swap in a new group photo, no crop math is needed — just replace the file and update the caption; very tall or very wide originals will just make the box taller/wider, they won't get force-cropped.
- **A person's headshot is looked up by their `data/authors/` filename, not by the `slug:` field inside the file or their display name.** Whatever the `.yaml` file is *named* is what the matching image file in `assets/media/authors/` must be named too, regardless of what's inside either file. Get this wrong and there's no error — the card quietly falls back to the initials placeholder. (David's photo was broken this way for a while, back when his data file was still called `me.yaml` but his photo was already `david-shechter.jpg`.)
- **A publication's `authors:` entries must be full names, not initials.** One older publication had `"D. Shechter"`, `"H. Chen"` etc. instead of full names — each author string becomes its own Hugo taxonomy term, so `"D. Shechter"` created a separate, disconnected `/authors/d.-shechter/` page instead of linking into David's real profile at `/authors/david-shechter/` (and similarly orphaned the co-authors from their own alumni profiles). Fixed for that one file; if a new publication's authors don't show up linked to the right person's profile page, check for this.
- **David's individual profile page (`/authors/david-shechter/`) is a local override too** (`layouts/authors/term.html`), on top of what the vendored template does (avatar, name, role, affiliations, bio, social links, then a list of authored publications). Two changes: it actually renders `interests`, `education`, and a new `teaching:` field from `data/authors/<slug>.yaml` (the vendored template computes `interests`/`education` into the profile data but never displays them at all — dead fields until now), and it lists authored publications with the same `citation` view as `/publications/` instead of the vendored template's large-image `card` view (same repeated-placeholder-image problem as the fixes on the Projects/Publications list pages, just worse here since one person can have 30+ papers). `teaching:` is a plain list of `{title, detail, dates}` — only David's file sets it today, but any author can. This override applies to every `/authors/<slug>/` page, not just David's.
- **Research pages can carry a figure now, but none has a real one yet.** `content/research/*.md` supports `image.filename` (same convention as projects/publications) via a local override at `layouts/research/single.html`; it renders as a contained figure below the title. All 5 research pages currently point at obvious placeholder files (`assets/media/research/PLACEHOLDER-*.jpg`, generated locally, not real figures) specifically so they're easy to find and swap — search the repo for `PLACEHOLDER` when a real figure is ready, replace the image file, and you can leave the `image.filename:` line as-is if you keep the same filename, or update it if you rename the file.

---

## Preview changes without publishing them

Three ways, cheapest first.

**1. On your own machine — instant, sees nobody.**

```bash
hugo server
# opens http://localhost:1313, rebuilds as you save
```

Nothing leaves your laptop. Best for wording and layout tweaks.

**2. A deploy preview — the real site, at a private URL.**

Push your work to a branch and open a pull request against `main` **without
merging it**. Netlify builds that PR and comments a preview link on it
(`deploy-preview-<number>--shechterlab-website.netlify.app`). It is the
production build — same Hugo version, same images, same headers — just at a
different address. Merge the PR when you are happy; that is the moment it goes
live. Close it instead and nothing ever shipped.

This is the one to use for anything structural, or when you want to send
someone a link before committing to it.

**3. A branch deploy** — push a branch and Netlify builds it at
`<branch>--shechterlab-website.netlify.app` with no PR at all. Needs turning on
first: Site configuration → Build & deploy → Branches and deploy contexts.
Useful for a long-running draft.

Previews are unlisted but not secret — anyone with the URL can open one. Netlify
does send `X-Robots-Tag: noindex` on them, so they will not turn up in search
results and compete with the real site.

**One thing that differs between preview and production:** previews build with
`-b $DEPLOY_PRIME_URL` so links work at the preview address, while production
uses the `baseURL` in `config/_default/hugo.yaml`. So absolute URLs — canonical
tags, the sitemap, the RSS feed — will read `deploy-preview-…netlify.app` in a
preview. That is correct, not a bug.
