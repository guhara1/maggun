# -*- coding: utf-8 -*-
"""모든 페이지를 빌드해 /home/user/maggun/(루트)에 배포."""
import os
import sys
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

OUT = ROOT.parent  # /home/user/maggun

from data.site import SITE
from data.districts import CITIES, all_districts
from data.catalog import SERVICES, THERAPISTS, MAGAZINE

import pages_core
import pages_service
import pages_therapist
import pages_magazine
import pages_location
import pages_seoul_dong


def minify_html(html):
    # JSON-LD 미니파이
    def mini_ld(m):
        try:
            obj = json.loads(m.group(2))
            return f'<script type="application/ld+json">{json.dumps(obj,ensure_ascii=False,separators=(",", ":"))}</script>'
        except Exception:
            return m.group(0)
    html = re.sub(r'(<script[^>]*application/ld\+json[^>]*>)(.*?)(</script>)', mini_ld, html, flags=re.S)

    # CSS 미니파이
    def mini_css(m):
        css = m.group(1)
        css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
        css = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css)
        css = re.sub(r'\s+', ' ', css)
        css = re.sub(r';}', '}', css)
        return f'<style>{css.strip()}</style>'
    html = re.sub(r'<style[^>]*>(.*?)</style>', mini_css, html, flags=re.S)
    return html


def write(rel_path, html):
    rel = rel_path.lstrip("/")
    full = OUT / rel
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(minify_html(html), encoding="utf-8")


def write_robots():
    robots = f"""User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {SITE['base_url']}/sitemap.xml
Host: {SITE['domain']}
"""
    (OUT / "robots.txt").write_text(robots, encoding="utf-8")


def write_manifest():
    manifest = {
        "name": SITE["brand_full"],
        "short_name": SITE["brand"],
        "description": SITE["tagline"],
        "start_url": "/",
        "scope": "/",
        "display": "standalone",
        "background_color": SITE["theme_color"],
        "theme_color": SITE["theme_color"],
        "lang": "ko-KR",
        "orientation": "portrait",
        "icons": [
            {"src": "/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }
    (OUT / "site.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def write_favicon_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#f4d29c"/><stop offset="45%" stop-color="#e9b8a7"/><stop offset="100%" stop-color="#c98a6b"/></linearGradient></defs><rect width="64" height="64" rx="14" fill="#0b0b0e"/><path d="M14 46V18l10 16 10-16v28" stroke="url(#g)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="46" cy="38" r="6" fill="url(#g)"/></svg>"""
    (OUT / "favicon.svg").write_text(svg, encoding="utf-8")


def write_sitemap(urls):
    items = []
    for loc, pri, freq in urls:
        items.append(f"  <url><loc>{SITE['base_url']}{loc}</loc><changefreq>{freq}</changefreq><priority>{pri}</priority></url>")
    body = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(items) + "\n</urlset>"
    (OUT / "sitemap.xml").write_text(body, encoding="utf-8")


def main():
    pages = []
    urls = []

    # 코어
    coremap = {
        "/": pages_core.index_page(),
        "/about/index.html": pages_core.about_page(),
        "/pricing/index.html": pages_core.pricing_page(),
        "/reviews/index.html": pages_core.reviews_page(),
        "/contact/index.html": pages_core.contact_page(),
        "/policy/privacy/index.html": pages_core.privacy_page(),
        "/policy/terms/index.html": pages_core.terms_page(),
        "/policy/youth/index.html": pages_core.youth_page(),
    }
    for path, html in coremap.items():
        if path == "/":
            write("/index.html", html)
            urls.append(("/", "1.0", "daily"))
        else:
            write(path, html)
            url = "/" + path.lstrip("/").replace("index.html","")
            pri = "0.3" if "/policy/" in path else "0.8"
            freq = "yearly" if "/policy/" in path else "monthly"
            urls.append((url, pri, freq))

    # 서비스
    for path, html in pages_service.all_service_pages():
        write(path, html)
        u = "/" + path.lstrip("/").replace("index.html","")
        urls.append((u, "0.85", "weekly"))

    # 관리사
    for path, html in pages_therapist.all_therapist_pages():
        write(path, html)
        u = "/" + path.lstrip("/").replace("index.html","")
        urls.append((u, "0.8", "weekly"))

    # 매거진
    for path, html in pages_magazine.all_magazine_pages():
        write(path, html)
        u = "/" + path.lstrip("/").replace("index.html","")
        urls.append((u, "0.7", "monthly"))

    # 지역 (가장 큼)
    for path, html in pages_location.all_location_pages():
        write(path, html)
        u = "/" + path.lstrip("/").replace("index.html","")
        depth = u.count("/") - 1
        pri = "0.9" if depth == 1 else ("0.85" if depth == 2 else "0.75")
        urls.append((u, pri, "weekly"))

    # 서울 행정동 (244개)
    for path, html in pages_seoul_dong.all_seoul_dong_pages():
        write(path, html)
        u = "/" + path.lstrip("/").replace("index.html","")
        urls.append((u, "0.7", "weekly"))

    # robots / manifest / sitemap / favicon
    write_robots()
    write_manifest()
    write_favicon_svg()
    write_sitemap(urls)

    # 보고
    n = len(urls)
    print(f"✅ Built {n} pages")
    # 디렉토리 트리 요약
    by_section = {}
    for u, _, _ in urls:
        top = u.split("/")[1] or "root"
        by_section[top] = by_section.get(top, 0) + 1
    for k, v in sorted(by_section.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
