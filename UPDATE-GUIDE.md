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
  last_name: Lastname
role: PhD Student
bio: One or two sentences on research focus.
affiliations:
  - name: Albert Einstein College of Medicine
interests:
  - Topic one
  - Topic two
user_groups:
  - PhD Student
last_name: Lastname
```

`role` and `user_groups` must be one of exactly: `Principal Investigator`, `Instructor`, `MD-PhD Student`, `PhD Student`, `Postdoctoral Fellow` — these are the values the homepage and People page team-showcase blocks filter on (`user_groups:` in `content/_index.md` and `content/people.md`). A person is listed **automatically** once their file exists with a matching role — there is no separate slug list to edit.

2. Drop a headshot at `assets/media/authors/firstname-lastname.jpg` — 600×600 px, JPG, ~85% quality, under 200 KB. If there's no headshot yet, skip this — the theme shows a colored initials placeholder automatically (this is normal, not a broken image; see gotchas below).

---

## Update a lab member

Edit `data/authors/<slug>.yaml`. Swap photo: replace `assets/media/authors/<slug>.jpg`.

---

## Move someone to alumni

In `content/people.md`, move their name from the current members section to alumni. Add their current position in parentheses. Keep or remove their `data/authors/<slug>.yaml` — either is fine.

---

## Add a publication

Create a folder `content/publications/your-paper-slug/` with an `index.md`. Copy an existing entry (e.g. `content/publications/gnmt-folate-methyl-donor-2026/index.md`) as your starting point — the real schema is more specific than it looks:

```yaml
---
title: "Full paper title, exactly as published"
authors:
- "First Author Name"
- "Second Author Name"
- me   # use the literal word `me` (unquoted) wherever David is an author — it maps to data/authors/me.yaml
date: "2026-01-01T00:00:00Z"
publishDate: "2026-01-01T00:00:00Z"
publication_types: ["article-journal"]   # or ["article"] for a preprint
publication: "*Journal Name, volume*(issue), pages"   # markdown italics around the journal name
abstract: "The actual published abstract — copy it verbatim from the paper, don't paraphrase or invent one."
summary: "One sentence for the card preview."
tags:
- Topic tag
featured: false
links:
- name: Article        # or "bioRxiv" for a preprint
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

---

## Update a publication status (preprint → published)

Open `content/publications/<slug>/index.md` and edit:
- `publication_types:` from `["article"]` to `["article-journal"]`
- `publication:` from `"*bioRxiv*"` to the journal citation, e.g. `"*Nature Communications, 17*(1), 1234"`
- `date:` / `publishDate:` to the journal's online-publish date (not the bioRxiv posting date)
- `links:` — add or replace with the journal DOI; you can keep the bioRxiv link as a second entry if useful

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

Drop a JPG into `content/lab-life/`. Hugo Blox reads the folder. Optionally add a matching `.md` file with the same stem for a caption.

---

## Contact page

`content/contact.md` — edit the markdown block directly. The email is encoded as HTML entities to block scrapers. To change the address, re-encode it — paste the new address into an HTML encoder (e.g., mothereff.in/html-entities) and replace the entity string.

---

## Update the CV PDF

Replace `static/uploads/shechter-cv-2026.pdf`. Keep the filename so existing links hold. To rename it, update any references in `content/contact.md`.

---

## Funders strip

`content/_index.md` → the `block: logos` section. Add, remove, or reorder entries.

---

## Research area text

Each area has its own file in `content/research/`. Edit the body or the `summary:` in front matter.

---

## Resources page

`content/resources.md` — plain markdown. Add new protocol links, datasets, or tools directly to the table.

---

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

---

## Preview locally

```bash
hugo server
# opens http://localhost:1313
```

Nothing publishes until you push.
