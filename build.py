#!/usr/bin/env python3
"""Build the static site: wraps each page in src/pages with src/layout.html.

Usage: python3 build.py
Output is written to the repo root (index.html, book.html, services/*.html ...)
and committed, so Vercel serves the result with no build step.

Each page starts with a JSON block inside an HTML comment:
<!-- {"title": "...", "description": "...", "path": "/book"} -->
"""
import json, os, re, pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
LAYOUT = (SRC / "layout.html").read_text()
DOMAIN = "https://haroldsqualityautorepair.com"

def build_page(src_path: pathlib.Path):
    raw = src_path.read_text()
    m = re.match(r"\s*<!--\s*(\{.*?\})\s*-->", raw, re.S)
    if not m:
        raise SystemExit(f"{src_path}: missing meta comment")
    meta = json.loads(m.group(1))
    content = raw[m.end():].strip("\n")
    jsonld = ""
    if meta.get("jsonld"):
        jsonld = '<script type="application/ld+json">' + json.dumps(meta["jsonld"], indent=2) + "</script>"
    html = LAYOUT
    for k, v in {"title": meta["title"], "description": meta["description"], "path": meta["path"], "content": content, "jsonld": jsonld}.items():
        html = html.replace("{{" + k + "}}", v)
    rel = src_path.relative_to(SRC / "pages")
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    return meta["path"]

def main():
    paths = []
    for p in sorted((SRC / "pages").rglob("*.html")):
        paths.append(build_page(p))
        print("built", p.relative_to(SRC / "pages"))
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in paths:
        if path == "/privacy":
            continue
        sitemap.append(f"  <url><loc>{DOMAIN}{path}</loc></url>")
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    print(f"{len(paths)} pages, sitemap.xml, robots.txt")

if __name__ == "__main__":
    main()
