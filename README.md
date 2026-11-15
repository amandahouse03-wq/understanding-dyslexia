# Understanding Dyslexia

The website at **www.understanding-dyslexia.com**: what school is really like with dyslexia, dysgraphia and dyscalculia, by Jocelyn House.

It is a plain static site. There is nothing to install and no server code.

## What is in here

| Path | What it is |
|---|---|
| `site/` | The published website. This folder is what goes live. |
| `site/index.html` | The home page (built, do not edit by hand) |
| `site/simulation/index.html` | The interactive simulation (built, do not edit by hand) |
| `site/videos/` | The four narrated videos |
| `site/posters/` | The still image shown before each video plays |
| `site/og.png`, `site/favicon.svg` | The image shown when the link is shared, and the browser tab icon |
| `src/home.html` | Source for the home page: all of its words, styles and script |
| `src/simulation.html` | Source for the simulation |
| `build.py` | Turns the two source pages into the two published pages |
| `vercel.json` | Tells Vercel to publish the `site/` folder as is |

## Changing the site

1. Edit `src/home.html` (the home page) or `src/simulation.html` (the simulation).
2. Run `python3 build.py`.
3. Commit and push. Vercel publishes the change automatically within a minute or so.

To replace a video, put the new file in `site/videos/` under the same name (`reading.mp4`, `lecture.mp4`, `writing.mp4`, `math.mp4`).

To look at the site on your own computer before pushing:

```
cd site
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Hosting

The site is hosted on Vercel, connected to this GitHub repository. Every push to `main` goes live.

The domain `www.understanding-dyslexia.com` is added under the Vercel project's Settings, Domains. Vercel shows the DNS records to set at the domain registrar.
