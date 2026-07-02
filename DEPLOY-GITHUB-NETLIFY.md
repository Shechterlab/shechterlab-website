# Setting up GitHub + Netlify + custom domain

This is a one-time setup. After it's done, publishing any change is just:

```bash
git add .
git commit -m "what you changed"
git push
```

Netlify builds and deploys automatically, usually in under two minutes.

---

## What you need before starting

- Git on your machine (`git --version` to check; install from git-scm.com if needed)
- A GitHub account with access to the `shechterlab` org
- A Netlify account (free tier is fine)
- The ability to add DNS records to `shechterlab.org`, or have IT do it

---

## Create the GitHub repository

Go to github.com/shechterlab, click **New repository**, name it `shechterlab-website`. Leave it empty — don't initialize with a README.

From the terminal, in this folder:

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/shechterlab/shechterlab-website.git
git push -u origin main
```

---

## Connect Netlify

In Netlify: **Add new site → Import an existing project → GitHub**. Select `shechterlab/shechterlab-website`.

Build settings — confirm these before deploying:

- Build command: `hugo --gc --minify`
- Publish directory: `public`

Add one environment variable under **Site settings → Environment variables**:

| Key | Value |
|-----|-------|
| `HUGO_VERSION` | `0.128.0` |

This pins Hugo to a known version. Without it, Netlify's default Hugo version may not match what this site was built on. Click **Deploy**.

Netlify gives you a URL like `random-name.netlify.app`. The site is live there immediately.

---

## Connect the custom domain

In Netlify under **Domain management**, add `www.shechterlab.org`. Netlify shows you the DNS records to set.

The domain currently redirects to your Einstein faculty page. Log in to your registrar and update two records:

| Type | Name | Value |
|------|------|-------|
| CNAME | `www` | `your-site-name.netlify.app` |
| A | `@` | `75.2.60.5` |

The old redirect stays active until the new records propagate (usually a few minutes, up to an hour), so there's no gap where the domain goes dark. HTTPS provisions automatically once DNS is live.

---

## Routine workflow

Edit files, then push. Or for small edits, use the GitHub web UI directly — find the file, click the pencil, commit. No terminal needed.

To roll back a bad deploy: in Netlify under **Deploys**, find the last good deploy and click **Publish deploy**. Instant, no Git involved.
