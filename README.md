# Static Site Generator (Python)

A small static site generator that converts Markdown content into HTML using a shared template, copies static assets, and outputs a ready-to-serve site in `docs/`. Built to practice parsing Markdown, building HTML trees, and wiring a simple build pipeline.

## How it works

1. **Markdown input** lives in `content/`.
2. **Template** in `template.html` provides the HTML shell with `{{ Title }}` and `{{ Content }}` placeholders.
3. **Generator** in `src/` parses Markdown into HTML nodes, injects into the template, and writes HTML files to `docs/`.
4. **Static assets** from `static/` are copied into `docs/`.
5. **Base path rewriting** ensures links and image paths are prefixed (useful for GitHub Pages).

## Tech used

- **Python 3** standard library
- **Markdown parsing logic** (custom, in `src/`)
- **HTML templating by string replacement** (simple placeholders)
- **Shell scripts** for build/test convenience

## What you learn

- Building a small compiler-style pipeline (parse -> transform -> render)
- Traversing directories and generating output recursively
- Handling relative/absolute URLs for static hosting
- Writing tests for pure functions and parsing logic
- Packaging a simple static site build process

## Usage

Build the site (writes to `docs/` and creates `.nojekyll`):

```bash
./build.sh
```

Build and serve locally on port 8888:

```bash
./main.sh
```

Run tests:

```bash
./test.sh
```

### Base path

The scripts pass a base path of `/static_site_generator/`, which matches the asset links seen in `docs/index.html`. You can pass a different base path via `python3 src/main.py "/"` if you want root-relative links for a non-GitHub-Pages host.

## Project structure

- `content/` - Markdown source pages
- `template.html` - HTML template
- `static/` - CSS/images copied as-is
- `docs/` - Generated HTML output
- `src/` - Generator and parsing code
- `build.sh`, `main.sh`, `test.sh` - helper scripts

