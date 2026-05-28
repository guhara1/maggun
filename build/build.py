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
import pages_dong


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
    robots = f"""# robots.txt for {SITE['brand_full']} ({SITE['base_url']})
# Updated: 2026-05-28

# ── Mainstream search bots ──────────────────────────────────
User-agent: Googlebot
Allow: /
Crawl-delay: 0

User-agent: Googlebot-Image
Allow: /

User-agent: Googlebot-News
Allow: /magazine/

User-agent: Yeti
Allow: /
Crawl-delay: 0

User-agent: NaverBot
Allow: /

User-agent: Daum
Allow: /

User-agent: bingbot
Allow: /

User-agent: DuckDuckBot
Allow: /

# ── AI training crawlers (allowed) ──────────────────────────
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: anthropic-ai
Allow: /

# ── Aggressive scrapers (blocked) ───────────────────────────
User-agent: SemrushBot
Disallow: /

User-agent: AhrefsBot
Disallow: /

User-agent: MJ12bot
Disallow: /

User-agent: DotBot
Disallow: /

# ── Default ─────────────────────────────────────────────────
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Disallow: /*?*

# ── Sitemap & feed ──────────────────────────────────────────
Sitemap: {SITE['base_url']}/sitemap.xml
Sitemap: {SITE['base_url']}/sitemap-news.xml
Sitemap: {SITE['base_url']}/rss.xml

Host: {SITE['domain']}
"""
    (OUT / "robots.txt").write_text(robots, encoding="utf-8")


def write_indexnow_key():
    """IndexNow 프로토콜 키 파일 — Bing·Naver·Yandex가 즉시 색인 알림 받음."""
    key = "a8f3c2d9b54e7f1c6d3a8b2e5f9c4d7a"  # 32자 hex
    (OUT / f"{key}.txt").write_text(key, encoding="utf-8")
    (OUT / "indexnow-key.txt").write_text(key, encoding="utf-8")
    return key


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


TODAY = "2026-05-28"


def _sitemap_xml(items):
    """sitemap urlset — items: list of dict {loc, pri, freq, lastmod, image?}"""
    rows = []
    for it in items:
        lastmod = it.get("lastmod", TODAY)
        img = ""
        if it.get("image"):
            img = f'<image:image><image:loc>{it["image"]}</image:loc></image:image>'
        rows.append(
            f'  <url><loc>{SITE["base_url"]}{it["loc"]}</loc>'
            f'<lastmod>{lastmod}</lastmod>'
            f'<changefreq>{it["freq"]}</changefreq>'
            f'<priority>{it["pri"]}</priority>'
            f'{img}</url>'
        )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
            + "\n".join(rows) + "\n</urlset>")


def write_sitemaps(urls):
    """sitemap index + 분할 sitemap. 카테고리별로 나눠 크롤링 효율 ↑."""
    og = f"{SITE['base_url']}/assets/og-cover.jpg"

    # 카테고리 분할
    cats = {
        "main": [],      # /, about, pricing, reviews, contact, policy
        "services": [],  # /service/*
        "therapists": [],
        "magazine": [],
        "locations": [], # /locations/{city}/ + /locations/{city}/{district}/
        "dongs-seoul": [],
        "dongs-gyeonggi": [],
        "dongs-incheon": [],
        "dongs-busan": [],
    }
    for loc, pri, freq in urls:
        item = {"loc": loc, "pri": pri, "freq": freq, "lastmod": TODAY, "image": og}
        if loc.startswith("/service/"):
            cats["services"].append(item)
        elif loc.startswith("/therapists/"):
            cats["therapists"].append(item)
        elif loc.startswith("/magazine/"):
            cats["magazine"].append(item)
        elif loc.startswith("/locations/seoul/") and "/dong/" in loc:
            cats["dongs-seoul"].append(item)
        elif loc.startswith("/locations/gyeonggi/") and "/dong/" in loc:
            cats["dongs-gyeonggi"].append(item)
        elif loc.startswith("/locations/incheon/") and "/dong/" in loc:
            cats["dongs-incheon"].append(item)
        elif loc.startswith("/locations/busan/") and "/dong/" in loc:
            cats["dongs-busan"].append(item)
        elif loc.startswith("/locations/"):
            cats["locations"].append(item)
        else:
            cats["main"].append(item)

    # 개별 sitemap 파일
    sitemap_files = []
    for name, items in cats.items():
        if not items: continue
        fname = f"sitemap-{name}.xml"
        (OUT / fname).write_text(_sitemap_xml(items), encoding="utf-8")
        sitemap_files.append(fname)

    # sitemap index
    idx_rows = "\n".join(
        f'  <sitemap><loc>{SITE["base_url"]}/{f}</loc><lastmod>{TODAY}</lastmod></sitemap>'
        for f in sitemap_files
    )
    idx = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + idx_rows + "\n</sitemapindex>")
    (OUT / "sitemap.xml").write_text(idx, encoding="utf-8")

    return sitemap_files


def write_news_sitemap():
    """Google News 사이트맵 — 매거진 3편 (48시간 이내 글만 효과)."""
    from data.catalog import MAGAZINE
    rows = []
    for a in MAGAZINE:
        rows.append(
            f'  <url><loc>{SITE["base_url"]}/magazine/{a["slug"]}/</loc>'
            f'<news:news>'
            f'<news:publication><news:name>{SITE["brand_full"]}</news:name><news:language>ko</news:language></news:publication>'
            f'<news:publication_date>{a["date"]}</news:publication_date>'
            f'<news:title>{a["title"]}</news:title>'
            f'</news:news></url>'
        )
    body = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n'
            + "\n".join(rows) + "\n</urlset>")
    (OUT / "sitemap-news.xml").write_text(body, encoding="utf-8")


def write_rss():
    """RSS 2.0 — 매거진 글 + 전체 사이트 업데이트 알림용."""
    from data.catalog import MAGAZINE
    from email.utils import formatdate
    import time
    pub_date = formatdate(time.time(), localtime=False, usegmt=True)

    items = []
    for a in MAGAZINE:
        items.append(
            f'<item>'
            f'<title>{a["title"]}</title>'
            f'<link>{SITE["base_url"]}/magazine/{a["slug"]}/</link>'
            f'<guid isPermaLink="true">{SITE["base_url"]}/magazine/{a["slug"]}/</guid>'
            f'<description><![CDATA[{a["lead"]}]]></description>'
            f'<author>{SITE["email"]} ({a["author"]})</author>'
            f'<category>{a["category"]}</category>'
            f'<pubDate>{formatdate(time.mktime(time.strptime(a["date"], "%Y-%m-%d")), usegmt=True)}</pubDate>'
            f'</item>'
        )

    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:dc="http://purl.org/dc/elements/1.1/">
<channel>
<title>{SITE['brand_full']} 매거진</title>
<link>{SITE['base_url']}/magazine/</link>
<atom:link href="{SITE['base_url']}/rss.xml" rel="self" type="application/rss+xml"/>
<description>{SITE['tagline']} 운영진·자문 트레이너가 직접 쓰는 회복 가이드.</description>
<language>ko-KR</language>
<copyright>© 2026 {SITE['company']['legal_name']}</copyright>
<managingEditor>{SITE['email']} ({SITE['company']['representative']})</managingEditor>
<webMaster>{SITE['email']} ({SITE['company']['representative']})</webMaster>
<pubDate>{pub_date}</pubDate>
<lastBuildDate>{pub_date}</lastBuildDate>
<category>건강</category>
<category>출장마사지</category>
<ttl>720</ttl>
<image>
<url>{SITE['base_url']}/assets/og-cover.jpg</url>
<title>{SITE['brand_full']}</title>
<link>{SITE['base_url']}/</link>
<width>1200</width>
<height>630</height>
</image>
{"".join(items)}
</channel>
</rss>'''
    (OUT / "rss.xml").write_text(body, encoding="utf-8")


def write_atom():
    """Atom 1.0 — 표준 피드."""
    from data.catalog import MAGAZINE
    entries = []
    for a in MAGAZINE:
        entries.append(
            f'<entry>'
            f'<title>{a["title"]}</title>'
            f'<link href="{SITE["base_url"]}/magazine/{a["slug"]}/"/>'
            f'<id>{SITE["base_url"]}/magazine/{a["slug"]}/</id>'
            f'<updated>{a["date"]}T00:00:00Z</updated>'
            f'<published>{a["date"]}T00:00:00Z</published>'
            f'<author><name>{a["author"]}</name></author>'
            f'<category term="{a["category"]}"/>'
            f'<summary type="html"><![CDATA[{a["lead"]}]]></summary>'
            f'</entry>'
        )
    body = f'''<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="ko">
<title>{SITE['brand_full']} 매거진</title>
<subtitle>{SITE['tagline']}</subtitle>
<link href="{SITE['base_url']}/atom.xml" rel="self"/>
<link href="{SITE['base_url']}/magazine/" rel="alternate"/>
<id>{SITE['base_url']}/</id>
<updated>{TODAY}T00:00:00Z</updated>
<rights>© 2026 {SITE['company']['legal_name']}</rights>
<generator>마사지꾼 빌드 파이프라인</generator>
{"".join(entries)}
</feed>'''
    (OUT / "atom.xml").write_text(body, encoding="utf-8")


def write_humans_txt():
    """humans.txt — 사람이 만든 것임을 명시 (E-E-A-T 부수 신호)."""
    txt = f"""/* TEAM */
대표: {SITE['company']['representative']}
회사: {SITE['company']['legal_name']}
이메일: {SITE['email']}
주소: {SITE['company']['address']}

운영팀: 김세영(서울권), 박정훈(경기·인천권), 이수민(부산권)
자문: 박지연(KSPO 스포츠 트레이너), 정민호(물리치료사 PT), 윤하늬(IFA 아로마테라피스트)

/* SITE */
최종 갱신: {TODAY}
언어: 한국어 (ko-KR)
표준: HTML5, JSON-LD, RSS 2.0, Atom 1.0, IndexNow, Sitemap 0.9
"""
    (OUT / "humans.txt").write_text(txt, encoding="utf-8")


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

    # 서울·경기·인천·부산 행정동 (모든 도시 합산 ~850개)
    for city_slug in ("seoul", "gyeonggi", "incheon", "busan"):
        for path, html in pages_dong.all_dong_pages(city_slug):
            write(path, html)
            u = "/" + path.lstrip("/").replace("index.html","")
            urls.append((u, "0.7", "weekly"))

    # robots / manifest / sitemap / RSS / IndexNow / favicon
    write_robots()
    write_manifest()
    write_favicon_svg()
    sitemap_files = write_sitemaps(urls)
    write_news_sitemap()
    write_rss()
    write_atom()
    write_indexnow_key()
    write_humans_txt()

    # 보고
    n = len(urls)
    print(f"✅ Built {n} pages")
    print(f"   Sitemap index → {len(sitemap_files)} sub-sitemaps: {', '.join(sitemap_files)}")
    print(f"   Feeds: rss.xml, atom.xml, sitemap-news.xml")
    print(f"   IndexNow key file generated")
    # 디렉토리 트리 요약
    by_section = {}
    for u, _, _ in urls:
        top = u.split("/")[1] or "root"
        by_section[top] = by_section.get(top, 0) + 1
    for k, v in sorted(by_section.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
