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

Replace `assets/media/lab/lab-glass-experiment-notes.jpg` with a new file (same name), or add a new file and update `filename:` in the hero `background.image` section of `content/_index.md`.

---

## Navigation

`config/_default/menus.yaml` — each entry has `name`, `url`, and `weight` (lower = further left).

---

## Add a lab member

1. Create `data/authors/firstname-lastname.yaml`:

```yaml
name: Liana Valin
role: Graduate Student (MSTP)
bio: One or two sentences on research focus.
avatar_filename: liana-valin.jpg
orcid: ''
social:
  - icon: linkedin
    icon_pack: fab
    link: ''
```

2. Drop a headshot at `assets/media/authors/liana-valin.jpg` — 600×600 px, JPG, ~85% quality, under 200 KB.

3. Add the slug `liana-valin` to the team list in `content/people.md` or the team-showcase block in `content/_index.md`.

---

## Update a lab member

Edit `data/authors/<slug>.yaml`. Swap photo: replace `assets/media/authors/<slug>.jpg`.

---

## Move someone to alumni

In `content/people.md`, move their name from the current members section to alumni. Add their current position in parentheses. Keep or remove their `data/authors/<slug>.yaml` — either is fine.

---

## Add a publication

Create a folder `content/publications/your-paper-slug/` with an `index.md`:

```yaml
---
title: 'Full paper title'
authors: [author-slug-1, author-slug-2]
date: '2026-01-01'
doi: '10.1038/...'
publication: '*Nature Communications*'
publication_types: ['article-journal']
abstract: One paragraph.
tags: [PRMT5, cancer]
featured: false
---
```

Set `featured: true` to show the paper in the homepage publications strip.

---

## Update a publication status

Open `content/publications/<slug>/index.md` and edit:
- `publication_types:` from `['preprint']` to `['article-journal']`
- `doi:` to add the final DOI
- `publication:` from "bioRxiv" to the journal name

---

## Add a news item

Create `content/news/YYYY-MM-description.md`:

```yaml
---
title: 'Headline'
date: 2026-07-01
tags: [People]   # People | Preprint | Grant | Talk | Revision | Upcoming
summary: 'One sentence shown in the news list.'
---

Body text in markdown.
```

Items dated more than two years before today collapse automatically into "Older news."

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

`config/_default/params.yaml` for social links and SEO.  
`assets/css/custom.css` for colors — the primary teal is `#155e75`, accent amber is `#d97706`.

---

## Preview locally

```bash
hugo server
# opens http://localhost:1313
```

Nothing publishes until you push.
