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
| About, History, Speakers, Sponsors, Gallery, Join, Code of conduct | `content/*.md` |
| Agendas | `content/events/<slug>/agenda.csv` |
| Sponsor list | `data/sponsors.yaml` |
| Gallery photo list | `data/gallery.yaml` |
| Gallery image files | `assets/media/gallery/<year>/` |
| Steering committee and speaker profiles | `data/authors/<slug>.yaml` |
| Logo, favicon, custom CSS | `assets/` |
| Images referenced from raw HTML | `static/media/` |
| Local theme overrides | `layouts/` |

`layouts/_partials/hbx/blocks/` holds two blocks written for this site —
`sponsors` and `gallery`. Both read from `data/`, so adding a sponsor or a photo
is a YAML edit, never a template edit. The rest of `layouts/` patches bugs in the
upstream theme; each file explains itself at the top:

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

## The hero, and the generated art

The home page hero is deliberately unlike shechterlab.org: full-bleed navy,
left-aligned display type, and the numbers sitting *inside* the hero. That is
the shape of the Hugo Blox premium **Conference** template's `hero-with-stats`,
rebuilt here on the current stack (see the note at the end of this file).

Two hero assets are **generated from the club logo**, not drawn by hand, each by
a build script kept beside its output so it can be re-run if the logo changes:

| Asset | Script | What it does |
|---|---|---|
| `assets/media/hero-skyline.jpg` | `hero-skyline.build.py` | Lifts the skyline silhouette out of the logo (masking off the wordmark and the mirrored reflection) and composites it over a navy gradient with a warm low-left glow. |
| `assets/media/logo/wordmark-white.png` | `logo/wordmark-white.build.py` | White knockout of the wordmark alone — no skyline, since the hero background already is one. The letters inside the N/Y/C roundels stay transparent so the navy shows through them. |

Re-run either with `python3 <script>` from the repo root (needs `pillow` and
`numpy`). If the hero image is replaced with a photograph, keep it dark enough
for white text, or set `text_color_light: false` on the block.

`static/media/logo/wordmark-white.png` is a **copy** of the asset version: the
hero uses a raw `<img src="/media/...">`, which resolves against `static/`, not
`assets/`. Update both if you change it.

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

## Agendas, registration and abstracts

**The agenda for each symposium is a CSV** sitting next to that symposium's
`index.md`, rendered by the theme's `table` shortcode:

```
content/events/symposium-2026/agenda.csv
```

```csv
Time,Session,Location
9:00,"Registration, coffee and poster setup",Foyer
10:00,Keynote I — Brian Strahl,Auditorium
```

It opens in Excel or Numbers, so the program can be handed to whoever is running
the day without them touching Markdown. Quote any cell containing a comma. The
page pulls it in with:

```
<div class="ncc-schedule">

{{</* table path="agenda.csv" header="true" */>}}

</div>
```

Past agendas therefore stay with their symposium and never need migrating.

**Registration and abstract links** are front matter on the event page:

```yaml
registration_url: 'https://forms.gle/...'   # any URL: Google Forms, Eventbrite, mailto:
abstract_url: 'https://forms.gle/...'
abstract_deadline: '2027-05-14'
registration_closed: false                  # true greys the button out after the event
registration_note: 'Registration is free.'
```

`{{</* event-actions */>}}` in the body renders them as buttons. Empty fields
drop their button, so the page is safe to publish before anything opens — with
only `registration_note` set it shows the note alone, which is what an announced
but not-yet-open symposium needs. Because the URLs live in front matter rather
than in body text, the events list can also read them.

**A symposium with no date yet** still needs a `date:` so Hugo sorts it and
counts it as upcoming. Set `date_text: 'To be announced'` so that placeholder is
never shown to a reader, and set `lastmod:` too — the "Last updated on" line
falls back to `date` and would otherwise print a date in the future. Delete both
once the real date is set.

## Adding a sponsor

Edit `data/sponsors.yaml`. Only `name` is required:

```yaml
years:
  - year: 2027
    current: true              # this year's list, shown at the top of /sponsors/
    sponsors:
      - name: Acme Epigenetics
        tier: lead             # lead | supporting | exhibitor (rename in `tiers:`)
        url: https://example.com/
        logo: sponsors/acme.svg   # OPTIONAL — assets/media/sponsors/acme.svg
```

A sponsor with no `logo` renders as a typographic card, deliberately: the page
should never be blocked on chasing a vector file. Use artwork the sponsor
supplies; don't scrape a logo off their site. A sponsor whose `tier` doesn't
match any entry in `tiers:` is still displayed, under a generic heading, so a
typo shows up instead of silently dropping the sponsor.

Years without `current: true` fall into "Sponsors over the years", newest first.

## Adding gallery photos

1. Drop the files into `assets/media/gallery/<year>/`.
2. List them in `data/gallery.yaml` under that year.

```yaml
albums:
  - year: 2026
    photos:
      - src: gallery/2026/posters-01.jpg
        caption: Poster session, Vagelos Education Center
```

Upload at full size — Hugo generates the thumbnails. `caption` doubles as the
alt text, so it is worth writing. An album with no photos shows an empty state
rather than disappearing, so it stays obvious where photos are still wanted.

The lightbox is CSS-only (`:target`), so it works without JavaScript and the
back button closes it. The trade-off is that every full-size image is in the
page HTML — fine for tens of photos, worth revisiting past a few hundred.

**Before posting:** these are photographs of identifiable people. Make sure
attendees were told photos would be published, pull any photo on request, and
don't post a slide or poster without the presenter's say-so.

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
