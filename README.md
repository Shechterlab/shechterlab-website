# Shechter Lab website

Source for [shechterlab.org](https://www.shechterlab.org) — the lab site for the Shechter Lab, Department of Biochemistry, Albert Einstein College of Medicine. Built with [Hugo](https://gohugo.io) + the [Hugo Blox Kit](https://hugoblox.com) theme, deployed on Netlify.

## Editing this site

**Most edits — a news item, a new publication, updating someone's bio — can be done entirely in the GitHub web UI.** Find the file, click the pencil icon, edit, commit directly to `main` (or open a pull request if you'd like a second pair of eyes). Netlify rebuilds and deploys automatically, usually in under two minutes. No local setup required.

Start here:

| Doc | What it's for |
|-----|----------------|
| **[UPDATE-GUIDE.md](UPDATE-GUIDE.md)** | Task-oriented "I want to..." guide — the file to open first for any content edit. Includes a list of known gotchas that will silently break the layout. |
| **[CONTENT-MAP.md](CONTENT-MAP.md)** | What every file and folder in the repo is for. |
| **[DEV-SETUP.md](DEV-SETUP.md)** | Setting up a local preview (`hugo server`) for bigger changes — new sections, layout testing. Not needed for routine edits. |
| **[DEPLOY-GITHUB-NETLIFY.md](DEPLOY-GITHUB-NETLIFY.md)** | How the GitHub → Netlify → custom domain pipeline is wired up. Only relevant if that pipeline itself needs to change. |

If you're not sure where something lives, `UPDATE-GUIDE.md` is organized by task ("add a lab member," "add a publication," "hero photo," ...) rather than by file, so search there first.

## Stack

- **Hugo** (static site generator) + **Hugo Blox Kit** (`github.com/HugoBlox/kit`, loaded as a Hugo Module — see `go.mod` / `config/_default/module.yaml`)
- **Tailwind CSS v4**, compiled at build time
- Deployed on **Netlify**, building from the `main` branch

## License

Site content is © Shechter Lab. The Hugo Blox Kit theme is MIT-licensed.
