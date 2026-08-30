# nycchromatinclub.org

Source for the [NYC Chromatin Club](https://www.nycchromatinclub.org/) website — Hugo + [Hugo Blox Kit](https://github.com/HugoBlox/kit) + Tailwind CSS v4.

Same stack as [shechterlab.org](https://github.com/Shechterlab/shechterlab-website), so anything you have learned editing that site applies here.

## Run it locally

```bash
pnpm install
pnpm dev          # http://localhost:1313
pnpm build        # production build into public/
```

Requires Hugo **extended** 0.158.0 and Go 1.21+ (Hugo pulls the theme as a Go module).

## Where things live

| What | Where |
|---|---|
| Site title, colors, nav, SEO, CSP | `config/_default/` |
| Homepage | `content/_index.md` |
| Symposium and meeting pages | `content/events/<slug>/index.md` |
| About, History, Speakers, Join, Code of conduct | `content/*.md` |
| Steering committee and speaker profiles | `data/authors/<slug>.yaml` |
| Logo, favicon, custom CSS | `assets/` |
| Images referenced from raw HTML | `static/media/` |
| Local theme overrides | `layouts/` |

Two files in `layouts/` patch bugs in the upstream theme; each explains itself at the top:

- `index.headers` — the vendored Netlify `_headers` generator collapses its own
  whitespace and emits a file that sets **no headers at all**. Copied from the
  Shechter Lab site, which hit the same bug.
- `_partials/views/card--start.html` — the card view hardcodes `grid-cols-1`, so
  a collection's `design.columns` is silently ignored.

## Typography

Everything is set in **Inter**, which the theme already self-hosts at
`/dist/font/Inter.var.woff2`. The logo wordmark is Helvetica, and Inter is the
screen-native neo-grotesque in that lineage — so the page reads as the same
voice as the logo. The site makes **zero external requests**: no Google Fonts,
no CDN, nothing for the CSP to allow.

To change the heading face, override `--hb-font-heading` in
`assets/css/custom.css` — it is the only place to touch, and the comment there
explains what else has to change if the new face is not self-hosted.

## Brand colors

Sampled from the club logo and set in `config/_default/params.yaml`:

| | Hex | Used for |
|---|---|---|
| Navy | `#003884` | `primary` — links, buttons, headings |
| Orange | `#FF6600` | `secondary` — date badge, accents |
| Gray | `#919191` | skyline, muted text |

They are also exposed to hand-written markup as `--ncc-navy`, `--ncc-orange`, and `--ncc-gray` in `assets/css/custom.css`.

## Adding an event

Create `content/events/<slug>/index.md`:

```yaml
---
title: 4th Annual NYC Chromatin Club Symposium
summary: One line for the card on the events page.
date: 2027-07-20            # drives sort order and past/upcoming
type: events                # REQUIRED — selects the event layout
event_start: 2027-07-20T09:00:00
event_end: 2027-07-20T18:00:00
location: Venue name
address:
  street: 123 Example Ave
  city: New York
  region: NY
  postcode: '10001'
  country: United States
abstract: Shown in the event metadata block above the body text.
authors:                    # slugs from data/authors/
  - some-keynote-speaker
tags:
  - Symposium
featured: true              # pins it on the homepage
---
```

> **Future dates:** `buildFuture: true` is set in `config/_default/hugo.yaml`, and the
> Netlify preview/branch builds pass `--buildFuture`. Without it Hugo silently drops
> future-dated pages — which would delete the upcoming symposium page, the one thing
> the site exists to announce. Do not remove it.

## Adding a person

Create `data/authors/<slug>.yaml`:

```yaml
schema: hugoblox/author/v1
slug: jane-doe
weight: 3                   # manual ordering within a group
name:
  display: Jane Doe
  family: Doe
role: Steering Committee
bio: One or two sentences.
affiliations:
  - name: Some University
    url: https://example.edu/
interests:
  - Topic one
  - Topic two
user_groups:                # drives which team-showcase blocks show them
  - Steering Committee
```

Drop a headshot at `assets/media/authors/<slug>.jpg` and it is picked up automatically.
`user_groups` currently in use: `Steering Committee`, `2026 Keynote Speakers`, `2025 Keynote Speakers`.

## Outstanding content

Search the repo for `TODO (organizers)`. Currently:

- `content/events/symposium-2026/index.md` — the running order is the club's usual shape, not a confirmed 2026 timetable; abstract submission link and deadline still needed.
- `content/events/symposium-2024/index.md` — stub with a **placeholder date**; needs the real date, venue, and keynotes, or delete the file.
- `content/join.md` — Slack invite link.
- `content/history.md` — the 2020-23 entry describes the virtual era in general
  terms; the speaker list from those years and the date the Slack forum started
  are not recorded anywhere public.
- `info@nycchromatinclub.org` is used throughout as the contact address. Change it everywhere if that is not the right inbox.

## Deploying

Netlify: point it at this repo, no build settings needed — `netlify.toml` has them.
The `netlify-plugin-hugo-cache-resources` plugin needs installing once from the Netlify UI.
