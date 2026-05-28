#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""배포 후 검색엔진에 즉시 색인 알림 — IndexNow + Google/Bing/Naver ping.

사용:
    python3 ping_search_engines.py            # 전체 sitemap 핑
    python3 ping_search_engines.py /new-page  # 단일 URL IndexNow 핑
"""
import sys
import urllib.request
import urllib.parse
import json

BASE_URL = "https://massageggun.netlify.app"
HOST = "massageggun.netlify.app"
INDEXNOW_KEY = "a8f3c2d9b54e7f1c6d3a8b2e5f9c4d7a"
KEY_LOCATION = f"{BASE_URL}/{INDEXNOW_KEY}.txt"

# IndexNow 엔드포인트 — 한 번 핑하면 모든 참여 검색엔진(Bing, Yandex, Naver Yeti)에 전파
INDEXNOW_ENDPOINTS = [
    "https://api.indexnow.org/IndexNow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
]

# 사이트맵 핑 (구식이지만 여전히 동작)
SITEMAP_PINGS = [
    f"https://www.google.com/ping?sitemap={BASE_URL}/sitemap.xml",
    f"https://www.bing.com/ping?sitemap={BASE_URL}/sitemap.xml",
]


def indexnow_ping(urls):
    """URL 리스트를 IndexNow 프로토콜로 일괄 알림."""
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": [BASE_URL + u if u.startswith("/") else u for u in urls],
    }).encode("utf-8")

    headers = {"Content-Type": "application/json; charset=utf-8"}
    for ep in INDEXNOW_ENDPOINTS:
        try:
            req = urllib.request.Request(ep, data=payload, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=10) as r:
                print(f"  ✓ {ep} → HTTP {r.status}")
        except Exception as e:
            print(f"  ✗ {ep} → {e}")


def sitemap_ping():
    """sitemap.xml 위치를 Google/Bing에 알림."""
    for url in SITEMAP_PINGS:
        try:
            with urllib.request.urlopen(url, timeout=10) as r:
                print(f"  ✓ {url} → HTTP {r.status}")
        except Exception as e:
            print(f"  ✗ {url} → {e}")


def main():
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
        print(f"IndexNow ping for {len(urls)} URLs:")
        indexnow_ping(urls)
        return

    print("==> Sitemap ping (Google/Bing)")
    sitemap_ping()
    print()
    print("==> IndexNow ping (Bing/Yandex/Naver — 핵심 페이지 30개)")
    core = [
        "/", "/about/", "/pricing/", "/reviews/", "/contact/",
        "/service/", "/service/swedish/", "/service/aroma/", "/service/thai/",
        "/service/lomilomi/", "/service/sports/",
        "/therapists/", "/magazine/",
        "/locations/", "/locations/seoul/", "/locations/gyeonggi/",
        "/locations/incheon/", "/locations/busan/",
        "/locations/seoul/gangnam/", "/locations/seoul/seocho/",
        "/locations/seoul/songpa/", "/locations/seoul/mapo/",
        "/locations/gyeonggi/seongnam/", "/locations/gyeonggi/suwon/",
        "/locations/incheon/yeonsu/", "/locations/incheon/namdong/",
        "/locations/busan/haeundae/", "/locations/busan/busanjin/",
        "/magazine/post-meeting-recovery/", "/magazine/swedish-vs-aroma/",
        "/magazine/in-home-safety/",
    ]
    indexnow_ping(core)


if __name__ == "__main__":
    main()
