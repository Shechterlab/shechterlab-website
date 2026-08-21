# Local development setup

For small edits (news items, bios, typos), just edit files in the GitHub web UI and commit. No local setup needed.

For bigger changes — adding a new section, testing layout — you want local preview. The build uses Hugo + pnpm + pagefind, so bare `hugo server` alone won't fully work.

---

## Mac (fastest path)

```bash
# Install Homebrew if you don't have it: https://brew.sh
brew install hugo go node
npm install -g pnpm
```

## Windows

Download Hugo (extended edition) from https://github.com/gohugoio/hugo/releases — get the `extended` variant. Add it to your PATH. Install Node from https://nodejs.org, then `npm install -g pnpm`.

## WSL (Windows Subsystem for Linux)

WSL runs actual Linux (usually Ubuntu), so it needs Linux instructions, not the Windows ones above — and `apt install hugo` alone isn't enough, since Ubuntu's `hugo` package is typically an old, non-`extended` build that can't do this site's image processing.

```bash
sudo apt update
sudo apt install -y golang-go nodejs npm git
npm install -g pnpm

# Get the extended Linux binary directly, pinned to the version
# this site actually builds with (see HUGO_VERSION in netlify.toml):
cd /tmp
curl -LO https://github.com/gohugoio/hugo/releases/download/v0.158.0/hugo_extended_0.158.0_linux-amd64.tar.gz
tar -xzf hugo_extended_0.158.0_linux-amd64.tar.gz
sudo mv hugo /usr/local/bin/
hugo version   # confirm it says "+extended linux/amd64"
```

**Clone the repo inside the WSL filesystem** (e.g. `~/shechterlab-website`), not under `/mnt/c/Users/...`. Editing Windows-drive files from WSL is slow and makes Hugo's live-reload file-watcher unreliable — a very common source of "the dev server isn't picking up my changes" confusion that has nothing to do with Hugo itself.

`http://localhost:1313` opens fine from your regular Windows browser — WSL2 forwards `localhost` automatically.

---

## First-time setup (do once after cloning)

```bash
cd shechterlab-website
pnpm install
```

This installs the JS dependencies (pagefind, etc.) that the build needs.

---

## Preview the site

```bash
hugo server
```

Opens at http://localhost:1313. Live-reloads as you save files. Ctrl-C to stop.

If you see module errors, run `hugo mod tidy` first — this resolves Hugo module dependencies.

---

## Troubleshooting

**"command not found: hugo"** — Hugo isn't in your PATH. On Mac with Homebrew: `brew link hugo`. On Windows: make sure the folder containing `hugo.exe` is in your system PATH.

**Module download errors** — Go needs network access to fetch Hugo modules. Run `hugo mod download` once to cache them.

**pnpm install fails** — make sure Node is version 18 or later: `node --version`. Update if needed.

**Port 1313 already in use** — `hugo server --port 1314`

---

## Checking the full build (matches Netlify exactly)

```bash
pnpm install
hugo --gc --minify
```

Output goes to `public/`. You can open `public/index.html` in a browser, but local-file paths won't work for all assets — use `hugo server` for the best preview experience.
