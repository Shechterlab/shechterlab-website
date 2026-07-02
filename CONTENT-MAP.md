# Content map

Every file in the site, briefly.

---

## Config

| File | What it does |
|------|-------------|
| `config/_default/hugo.yaml` | Site title, baseURL, Hugo settings |
| `config/_default/params.yaml` | Colors, fonts, social links, contact info, SEO |
| `config/_default/menus.yaml` | Navigation items and order |
| `netlify.toml` | Build command and Hugo version for Netlify |

## Content

| File or folder | What it is |
|----------------|-----------|
| `content/_index.md` | Entire homepage — hero, research areas, values, team, publications, funders |
| `content/research/` | One file per research area |
| `content/publications/<slug>/index.md` | One folder per paper |
| `content/people.md` | Current lab + alumni |
| `content/news/` | One `.md` file per news item |
| `content/lab-life/_index.md` | Photo gallery/slider |
| `content/contact.md` | Contact card |
| `content/resources.md` | Protocols, Addgene, data, code, tools |
| `content/projects/<slug>/index.md` | Extended project pages (linked from research cards) |

## Authors

`data/authors/<slug>.yaml` — one file per person.  
Headshots at `assets/media/authors/<slug>.jpg` (600×600 px, JPG, <200 KB).

## Assets

| Path | Contents |
|------|---------|
| `assets/media/authors/` | Headshots |
| `assets/media/lab/` | Lab photos (hero, Lab Life) |
| `assets/media/research/` | Featured images for research cards |
| `assets/css/custom.css` | Font and color overrides |
| `static/uploads/shechter-cv-2026.pdf` | CV linked from Contact |
