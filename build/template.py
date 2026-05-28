# -*- coding: utf-8 -*-
"""기본 HTML 셸 — head/header/footer/공통 JSON-LD."""
import json
from data.site import SITE
from styles import CSS

BASE_URL = SITE["base_url"]


def jsonld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False, separators=(",", ":"))}</script>'


def organization_ld():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{BASE_URL}/#org",
        "name": SITE["brand_full"],
        "legalName": SITE["company"]["legal_name"],
        "url": BASE_URL + "/",
        "logo": f"{BASE_URL}/assets/logo-320.png",
        "image": f"{BASE_URL}/assets/og-cover.jpg",
        "telephone": SITE["phone_tel"],
        "email": SITE["email"],
        "founder": {"@type": "Person", "name": SITE["company"]["representative"]},
        "foundingDate": str(SITE["stats"]["since_year"]),
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["company"]["address"],
            "addressLocality": SITE["company"]["address_locality"],
            "addressRegion": SITE["company"]["address_region"],
            "postalCode": SITE["company"]["postal_code"],
            "addressCountry": SITE["company"]["country"],
        },
        "taxID": SITE["company"]["biz_no"],
        "contactPoint": [{
            "@type": "ContactPoint",
            "telephone": SITE["phone_tel"],
            "contactType": "reservations",
            "availableLanguage": ["Korean", "English", "Japanese", "Chinese"],
            "areaServed": "KR",
        }],
    }


def website_ld():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{BASE_URL}/#website",
        "url": BASE_URL + "/",
        "name": SITE["brand_full"],
        "inLanguage": "ko-KR",
        "publisher": {"@id": f"{BASE_URL}/#org"},
        "potentialAction": {
            "@type": "SearchAction",
            "target": {"@type": "EntryPoint", "urlTemplate": f"{BASE_URL}/locations/?q={{search_term_string}}"},
            "query-input": "required name=search_term_string",
        },
    }


def breadcrumb_ld(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": BASE_URL + url}
            for i, (name, url) in enumerate(items)
        ],
    }


def head(title, desc, canonical, og_image=None, extra=""):
    if not og_image:
        og_image = f"{BASE_URL}/assets/og-cover.jpg"
    canonical_full = BASE_URL + canonical
    return f"""<!doctype html><html lang="ko-KR"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="{SITE['theme_color']}">
<meta name="format-detection" content="telephone=no">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="googlebot" content="index,follow">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{SITE['brand_full']} 편집팀">
<link rel="canonical" href="{canonical_full}">
<link rel="alternate" hreflang="ko-KR" href="{canonical_full}">
<link rel="alternate" hreflang="x-default" href="{canonical_full}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE['brand_full']}">
<meta property="og:locale" content="ko_KR">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical_full}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:secure_url" content="{og_image}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{title}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">
<meta name="twitter:image:alt" content="{title}">
<link rel="image_src" href="{og_image}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<style>{CSS}</style>
{extra}
</head><body>"""


def header_html(active=""):
    def lk(slug, label):
        cls = ' style="color:var(--rose)"' if active == slug else ""
        return f'<a href="/{slug}/"{cls}>{label}</a>'

    return f"""<header><nav class="nav" aria-label="주 메뉴">
<a class="brand" href="/" aria-label="{SITE['brand']} 홈"><span class="brand-mark">마</span>{SITE['brand']}</a>
<button class="toggle" id="navToggle" aria-expanded="false" aria-controls="primary-menu">☰</button>
<ul id="primary-menu" class="menu">
<li><a href="/service/">서비스</a><ul class="submenu">
<li><a href="/service/swedish/">스웨디시</a></li>
<li><a href="/service/aroma/">아로마</a></li>
<li><a href="/service/thai/">타이</a></li>
<li><a href="/service/lomilomi/">로미로미</a></li>
<li><a href="/service/sports/">스포츠</a></li>
</ul></li>
<li><a href="/locations/">지역</a><ul class="submenu">
<li><a href="/locations/seoul/">서울</a></li>
<li><a href="/locations/gyeonggi/">경기</a></li>
<li><a href="/locations/incheon/">인천</a></li>
<li><a href="/locations/busan/">부산</a></li>
</ul></li>
<li><a href="/therapists/">관리사</a><ul class="submenu">
<li><a href="/therapists/korean/">한국</a></li>
<li><a href="/therapists/chinese/">중국</a></li>
<li><a href="/therapists/thai/">태국</a></li>
<li><a href="/therapists/vietnamese/">베트남</a></li>
<li><a href="/therapists/russian/">러시아</a></li>
<li><a href="/therapists/japanese/">일본</a></li>
</ul></li>
<li><a href="/pricing/">요금</a></li>
<li><a href="/magazine/">매거진</a></li>
<li><a href="/reviews/">후기</a></li>
<li><a class="cta-pill" href="tel:{SITE['phone_raw']}">24시 예약 {SITE['phone_display']}</a></li>
</ul></nav></header>"""


def footer_html():
    c = SITE["company"]
    return f"""<footer class="site-footer"><div class="footer-wrap">
<div class="footer-grid">
<div class="footer-col footer-brand">
<a class="brand" href="/" style="margin-bottom:14px"><span class="brand-mark">마</span>{SITE['brand']}</a>
<p>{SITE['tagline']}. 수도권·부산 전역에서 평균 32분 도착, 24시 운영, 자문 트레이너 가이드라인을 적용한 안전 케어를 약속드립니다.</p>
</div>
<div class="footer-col"><h4>서비스</h4>
<a href="/service/swedish/">스웨디시</a>
<a href="/service/aroma/">아로마</a>
<a href="/service/thai/">타이</a>
<a href="/service/lomilomi/">로미로미</a>
<a href="/service/sports/">스포츠</a>
<a href="/pricing/">전체 요금</a>
</div>
<div class="footer-col"><h4>지역</h4>
<a href="/locations/seoul/">서울 25개구</a>
<a href="/locations/gyeonggi/">경기 31개시</a>
<a href="/locations/incheon/">인천</a>
<a href="/locations/busan/">부산</a>
<a href="/locations/">전체 지역</a>
</div>
<div class="footer-col"><h4>안내</h4>
<a href="/about/">브랜드</a>
<a href="/therapists/">관리사 소개</a>
<a href="/magazine/">매거진</a>
<a href="/reviews/">실 후기</a>
<a href="/contact/">예약·문의</a>
</div>
</div>
<div class="footer-ops">
<div><div class="lbl">운영 시간</div><div class="val">{SITE['hours']}</div></div>
<div><div class="lbl">예약 전화</div><div class="val"><a href="tel:{SITE['phone_raw']}">{SITE['phone_display']}</a></div></div>
<div><div class="lbl">이메일</div><div class="val"><a href="mailto:{SITE['email']}">{SITE['email']}</a></div></div>
</div>
<div class="company-info">
<div><div class="lbl">회사명</div><div class="val">{c['legal_name']}</div></div>
<div><div class="lbl">대표자</div><div class="val">{c['representative']}</div></div>
<div><div class="lbl">사업자등록번호</div><div class="val">{c['biz_no']}</div></div>
<div><div class="lbl">주소</div><div class="val">{c['address']}</div></div>
<div><div class="lbl">통신판매업</div><div class="val">{c['tongsin_no']}</div></div>
<div><div class="lbl">개인정보보호책임자</div><div class="val">{c['privacy_officer']}</div></div>
</div>
<div class="footer-policies">
<a href="/policy/privacy/">개인정보처리방침</a>
<a href="/policy/terms/">이용약관</a>
<a href="/policy/youth/">청소년보호정책</a>
<a href="/about/">회사 소개</a>
<a href="/contact/">고객센터</a>
</div>
<div class="footer-bottom">
© {2026} {SITE['company']['legal_name']}. All rights reserved. {SITE['brand_full']}는 의료 행위가 아닌 건강관리·이완 서비스를 제공합니다. 19세 미만 이용 불가. 모든 콘텐츠는 자문 트레이너 가이드라인에 따라 검수되며, 실 운영 데이터는 2025년 11월~2026년 4월 5개월간의 배차 로그를 기반으로 합니다.
</div>
</div></footer>"""


JS = """<script>
(function(){
  var t=document.getElementById('navToggle');
  if(t){t.addEventListener('click',function(){
    var m=document.getElementById('primary-menu');
    var open=m.classList.toggle('open');
    t.setAttribute('aria-expanded',open?'true':'false');
  });}
  function idle(fn){if('requestIdleCallback'in window){requestIdleCallback(fn,{timeout:1500});}else{setTimeout(fn,1);}}
  idle(function(){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'80px'});
    document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
  });
})();
</script>"""


def page(title, desc, canonical, body, ld_objs=None, og_image=None, active=""):
    ld_html = "\n".join(jsonld(o) for o in (ld_objs or []))
    return (
        head(title, desc, canonical, og_image=og_image)
        + header_html(active=active)
        + body
        + footer_html()
        + ld_html
        + JS
        + "</body></html>"
    )


# ---------- 공통 컴포넌트 ----------

def note_card(num, title, paragraphs):
    paras = "".join(f"<p>{p}</p>" for p in paragraphs)
    return f'<div class="note-card reveal"><div class="note-num">{num:02d}</div><div class="note-content"><h3 class="note-title">{title}</h3><div class="note-text">{paras}</div></div></div>'


def faq_block(items):
    rows = "".join(f"<details><summary>{q}<span>+</span></summary><div>{a}</div></details>" for q, a in items)
    return f'<div class="faq">{rows}</div>'


def faq_ld(items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }


def breadcrumb_html(items):
    parts = []
    for i, (name, url) in enumerate(items):
        if i < len(items) - 1:
            parts.append(f'<a href="{url}">{name}</a>')
        else:
            parts.append(f'<span style="color:#d0d0d8">{name}</span>')
        if i < len(items) - 1:
            parts.append('<span>›</span>')
    return f'<nav class="bcrumb" aria-label="경로">{"".join(parts)}</nav>'


def cta_band(title="오늘 밤, 가장 편한 회복을 약속드립니다.", desc="평균 32분 도착, 24시 운영, 자문 트레이너 가이드라인. 전화 한 통으로 즉시 예약됩니다."):
    return f"""<section class="cta-band"><div class="wrap">
<h2>{title}</h2><p>{desc}</p>
<div class="actions" style="justify-content:center"><a class="btn btn-primary" href="tel:{SITE['phone_raw']}">📞 {SITE['phone_display']} 예약 →</a><a class="btn btn-ghost" href="/pricing/">전체 요금 보기</a></div>
</div></section>"""


def section_head(eyebrow, title, lead=""):
    p = f"<p>{lead}</p>" if lead else ""
    return f'<div class="section-head reveal"><span class="eyebrow"><span class="pulse"></span>{eyebrow}</span><h2>{title}</h2>{p}</div>'
