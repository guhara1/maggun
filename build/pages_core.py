# -*- coding: utf-8 -*-
"""메인·About·요금·후기·문의·정책."""
from data.site import SITE
from data.catalog import SERVICES, GLOBAL_REVIEWS, THERAPISTS
from data.districts import CITIES
from template import (
    page, note_card, faq_block, faq_ld, breadcrumb_html, cta_band,
    section_head, organization_ld, website_ld, breadcrumb_ld
)


# ---------- 메인 페이지 ----------

def index_page():
    body = """<section class="hero"><div class="hero-inner">
<div class="hero-copy reveal">
<span class="eyebrow"><span class="pulse"></span>2026 · 5개월 23,700건 배차 데이터 기반</span>
<h1>당신의 공간에 도착하는<br><span class="grad">정중한</span><br><span class="serif">휴식 한 시간.</span></h1>
<p class="lead">""" + SITE["brand_full"] + """은 서울·경기·인천·부산 82개 행정구에서 평균 32분 안에 매니저를 보내드리는 24시 출장마사지 브랜드입니다. 자문 트레이너 가이드라인을 적용한 안전 코스, 호텔 컨시어지 수준의 응대, 투명한 가격을 약속드립니다.</p>
<div class="actions">
<a class="btn btn-primary" href="tel:""" + SITE["phone_raw"] + """">📞 """ + SITE["phone_display"] + """ 예약 →</a>
<a class="btn btn-ghost" href="/service/">서비스 둘러보기</a>
</div>
<div class="trust">
<span><b>★ 4.96</b> / 2,847 리뷰</span>
<span><b>평균 32분</b> 도착</span>
<span><b>24시간</b> 연중무휴</span>
<span><b>매니저 156명</b> 활성</span>
</div>
</div>
<div class="hero-visual" aria-hidden="true">
<div class="floating fl-1">LIVE BOOKING · 5분 전 예약</div>
<div class="glass">
<h3><small>SIGNATURE COURSE</small>딥 릴렉스 90분<br>스웨디시 + 두피·어깨</h3>
<div class="book-row"><span>매니저</span><b>박O연 · 한국 · 경력 7년</b></div>
<div class="book-row"><span>도착 ETA</span><b>30~38분</b></div>
<div class="book-row"><span>요금</span><b>100,000원</b></div>
<a class="bk" href="tel:""" + SITE["phone_raw"] + """">예약 전화 →</a>
</div>
<div class="floating fl-2">CUSTOMER RATING · ★4.96</div>
</div>
</div></section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">
<span>서울 25개 자치구</span><span>경기 31개시</span><span>인천 10개 구·군</span><span>부산 16개 구·군</span><span>평균 도착 32분</span><span>매니저 156명</span><span>24시 운영</span><span>2026 트레이너 자문</span>
<span>서울 25개 자치구</span><span>경기 31개시</span><span>인천 10개 구·군</span><span>부산 16개 구·군</span><span>평균 도착 32분</span><span>매니저 156명</span><span>24시 운영</span><span>2026 트레이너 자문</span>
</div></div>

<section class="wrap" id="services">""" + section_head("SIGNATURE SERVICES", "5가지 코스, 각자의 분명한 자리.", "한 종류의 마사지로 모두를 응대하지 않습니다. 회식 후 회복, 만성 긴장, 골반 굳음, 정서 회복, 운동 후 근막 — 상황에 맞는 코스가 결과를 결정합니다.") + """
<div class="svc-grid">
""" + "".join(f"""<a class="svc reveal" href="/service/{s['slug']}/">
<span class="kicker">{s['kicker']}</span>
<h3>{s['name_ko']}</h3>
<p>{s['tag']}</p>
<span class="svc-link">자세히 보기 →</span>
</a>""" for s in SERVICES) + """
</div>
</section>

<section class="wrap" id="region">""" + section_head("SERVICE AREA", "82개 행정구, 평균 32분.", "단순한 도시명 매칭이 아닙니다. 5개월간 누적된 23,700건 배차 로그로 행정구·동(洞) 단위 도착 시간을 추적·갱신합니다.") + """
<div class="reg-grid">
""" + "".join(f"""<a class="reg reveal" href="/locations/{slug}/">
<span class="city">{c['short']}</span>
<h3>{c['name_ko']}</h3>
<div class="count">{c['count']}개 행정구</div>
<div class="meta">대표 권역: {", ".join(d['name_ko'] for d in c['districts'][:4])}…</div>
</a>""" for slug, c in CITIES.items()) + """
</div>
</section>

<section class="wrap" id="process">""" + section_head("HOW IT WORKS", "전화 한 통, 네 단계.") + """
<div class="steps">
<div class="step reveal"><span class="n">01</span><h3>전화 또는 카카오 문의</h3><p>위치·인원·희망 코스·시간만 알려주시면 됩니다. 평균 응답 30초.</p></div>
<div class="step reveal"><span class="n">02</span><h3>매니저 배차</h3><p>본사 디스패처가 권역·언어·전문성을 기준으로 가장 가까운 매니저를 배정합니다.</p></div>
<div class="step reveal"><span class="n">03</span><h3>실시간 ETA 안내</h3><p>매니저 출발과 동시에 도착 예정 시간을 문자로 보내드립니다.</p></div>
<div class="step reveal"><span class="n">04</span><h3>현금 또는 계좌</h3><p>시술 시작 전 결제. 사전 결제·구독·연회비 없음. 환불 정책 명시.</p></div>
</div>
</section>

<section class="wrap" id="reviews">""" + section_head("CLIENT VOICES", "최근 한 달 후기 일부.", "한 줄짜리 자동 후기는 사용하지 않습니다. 모든 후기는 실 시술 다음날 SMS로 직접 수집됩니다.") + """
<div class="rv-grid">
""" + "".join(f"""<div class="review reveal">
<div class="stars">★★★★★</div>
<div class="body">"{r['body']}"</div>
<div class="meta"><b>{r['name']}</b><span>·</span><span>{r['area']}</span><span>·</span><span>{r['course']}</span></div>
</div>""" for r in GLOBAL_REVIEWS[:6]) + """
</div>
</section>

<section class="wrap" id="about">""" + section_head("ABOUT · WHO · HOW · WHY", "누가, 어떻게, 왜 만들었는가.", "Google 검색 품질 가이드라인이 요구하는 4가지 신호 — 경험·전문성·권위·신뢰 — 를 정직하게 공개합니다.") + """
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;margin-bottom:36px">
""" + "".join(f"""<div class="step reveal"><span class="n">·</span><h3>{p['name']}</h3>
<p style="color:var(--gold);font-size:12px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:8px">{p['role']} · {p['exp']}</p>
<p>{p['scope']}</p></div>""" for p in SITE['people']) + """
</div>
""" + note_card(1, "WHO — 누가 만들었나", [
    f"{SITE['brand_full']}은 {SITE['company']['legal_name']} ({SITE['company']['representative']} 대표)이 {SITE['stats']['since_year']}년 설립해 운영하는 출장마사지 브랜드입니다.",
    "본사 디스패치팀 3명, 자문 트레이너 3명, 활동 매니저 156명이 단일 운영 체계 아래에서 움직입니다.",
    "운영 책임자 이름·직책·경력은 본 페이지와 푸터에 공개합니다.",
]) + note_card(2, "HOW — 어떻게 만들어지나", [
    "코스 가이드라인은 자문 트레이너 박지연(KSPO)·정민호(PT)·윤하늬(IFA) 3인의 검수를 받습니다.",
    f"행정구·동 단위 도착시간은 {SITE['stats']['dispatch_log_5m']:,}건의 실 배차 로그로 매월 갱신됩니다.",
    "콘텐츠는 AI 도구를 보조로 사용하되, 1차 데이터·운영 의사결정·후기 수집은 모두 사람이 직접 진행합니다.",
]) + note_card(3, "WHY — 왜 만들었나", [
    "출장마사지 시장은 가격 표기 부재, 도착 시간 미고지, 정체 불명 사업자가 만연합니다.",
    "우리는 가격·도착시간·사업자 정보·자문진을 모두 공개해 신뢰 가능한 동네 가게 같은 출장 서비스를 만듭니다.",
    "단기 마케팅이 아닌, 5년 이상 같은 자리에서 같은 약속을 지키는 브랜드가 되는 것이 목표입니다.",
]) + note_card(4, "SAFETY — 안전 약속", [
    "모든 매니저는 입사 시 자문 트레이너 가이드라인 교육과 안전 압력 범위 실습을 이수합니다.",
    "임신·심혈관·근골격 질환 등 금기 신호 7가지를 시술 전 매니저가 직접 확인합니다.",
    "응급 상황 대응 매뉴얼은 분기마다 갱신되며, 사고 발생 시 24시간 내 책임자 대면 보고가 원칙입니다.",
]) + note_card(5, "EDITORIAL POLICY — 편집 정책", [
    "본 사이트의 모든 페이지에는 책임 저자·편집팀·자문진이 명시됩니다.",
    "광고성 외부 기고·구매 후기는 게재하지 않습니다.",
    "정보가 갱신될 경우 페이지 하단에 갱신일을 표시하고, 잘못된 정보 발견 시 24시간 내 수정합니다.",
]) + """
<div class="data-box reveal" id="methodology">
<span class="kicker">DATA & METHODOLOGY</span>
<h3>이 사이트에 등장하는 모든 수치의 근거</h3>
<p>도착 시간·코스 비중·후기 평점은 2025년 11월 1일부터 2026년 3월 31일까지 5개월간의 자체 배차 로그(23,700건)를 기반으로 합니다. 행정구별 데이터는 매월 1일 자동 집계됩니다.</p>
<div class="chips">
<span class="chip">서울 <b>14,200건</b></span>
<span class="chip">경기 <b>6,400건</b></span>
<span class="chip">인천 <b>3,100건</b></span>
<span class="chip">평균 도착 <b>32분</b></span>
<span class="chip">평점 <b>★4.96</b></span>
<span class="chip">활동 매니저 <b>156명</b></span>
</div>
</div>
</section>

<section class="wrap" id="faq">""" + section_head("FAQ", "자주 묻는 질문.") + faq_block([
    ("정말 24시간 예약이 되나요?", "네. 365일·24시간 본사 디스패처가 상주합니다. 새벽 03시 콜이든 일요일 정오 콜이든 동일한 응답 시간을 약속드립니다."),
    ("도착 시간이 정확히 32분인가요?", "82개 행정구 평균값입니다. 강남·서면 등 도심은 28~33분, 가평·옹진 등 외곽은 1시간 이상이 정상 범위입니다. 콜 시점에 정확한 ETA를 안내드립니다."),
    ("결제는 어떻게 진행되나요?", "시술 시작 전 현금 또는 계좌이체로 진행됩니다. 사전 결제·구독·연회비는 없습니다. 환불은 시술 미시작 기준 100%, 시술 중단 시 시간 비례로 진행됩니다."),
    ("매니저 국적을 선택할 수 있나요?", "가능합니다. 한국·중국·태국·베트남·러시아·일본 6개국 매니저 중 권역별 가용 인원을 안내드리며, 외국인 손님은 영어·일어 가능 매니저를 우선 배정합니다."),
    ("안전한가요?", "모든 매니저는 자문 트레이너 가이드라인 교육을 이수했으며, 금기 신호 7가지(임신·심혈관·근골격 질환 등)는 시술 전 확인합니다. 사고 시 24시간 책임자 대면 보고가 원칙입니다."),
    ("의료 행위인가요?", "아닙니다. 본 서비스는 의료 행위가 아닌 건강관리·이완 서비스입니다. 통증·질환 치료를 목적으로 한다면 반드시 전문 의료기관을 먼저 방문해주시기 바랍니다."),
]) + """
</section>
""" + cta_band()

    title = f"마사지꾼 — 수도권·부산 24시 출장마사지"
    desc = f"수도권·부산 82개 행정구 24시 출장마사지. 평균 32분, 평점 ★4.96. {SITE['phone_display']}"

    local_ld = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": f"{SITE['base_url']}/#localbusiness",
        "name": SITE["brand_full"],
        "image": f"{SITE['base_url']}/assets/og-cover.jpg",
        "url": SITE["base_url"] + "/",
        "telephone": SITE["phone_tel"],
        "email": SITE["email"],
        "priceRange": "₩₩",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["company"]["address"],
            "addressLocality": SITE["company"]["address_locality"],
            "addressRegion": SITE["company"]["address_region"],
            "postalCode": SITE["company"]["postal_code"],
            "addressCountry": "KR",
        },
        "openingHoursSpecification": SITE["open_hours_spec"],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": SITE["stats"]["rating"], "reviewCount": SITE["stats"]["review_count"]},
        "areaServed": [{"@type": "AdministrativeArea", "name": c["name_ko"]} for c in CITIES.values()],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "출장마사지 코스",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name_ko"]}, "priceCurrency": "KRW", "price": s["duration_options"][0][1]}
                for s in SERVICES
            ],
        },
        "contactPoint": {
            "@type": "ContactPoint", "telephone": SITE["phone_tel"],
            "contactType": "reservations", "availableLanguage": ["Korean", "English", "Japanese", "Chinese"],
        },
    }

    article_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "image": f"{SITE['base_url']}/assets/og-cover.jpg",
        "author": [
            {"@type": "Person", "name": p["name"], "jobTitle": p["role"]} for p in SITE["people"]
        ],
        "reviewedBy": [
            {"@type": "Person", "name": a["name"], "jobTitle": a["role"]} for a in SITE["advisors"]
        ],
        "publisher": {"@id": f"{SITE['base_url']}/#org"},
        "datePublished": "2026-01-15",
        "dateModified": "2026-05-20",
    }

    faqs = [
        ("정말 24시간 예약이 되나요?", "네. 365일·24시간 본사 디스패처가 상주합니다."),
        ("도착 시간은 어느 정도인가요?", "82개 행정구 평균 32분입니다. 도심은 28~33분, 외곽은 50~60분이 정상 범위입니다."),
        ("결제는 어떻게 진행되나요?", "시술 시작 전 현금 또는 계좌이체. 사전 결제·구독·연회비는 없습니다."),
        ("매니저 국적을 선택할 수 있나요?", "한국·중국·태국·베트남·러시아·일본 6개국 매니저 중 권역별 가용 인원을 안내드립니다."),
        ("안전한가요?", "자문 트레이너 가이드라인을 적용하며 금기 신호 7가지를 시술 전 확인합니다."),
        ("의료 행위인가요?", "아닙니다. 의료 행위가 아닌 건강관리·이완 서비스입니다."),
    ]

    return page(
        title=title, desc=desc, canonical="/",
        body=body,
        ld_objs=[organization_ld(), website_ld(), local_ld, article_ld, faq_ld(faqs)],
        active="home",
    )


# ---------- /about/ ----------

def about_page():
    body = """<section class="wrap">""" + breadcrumb_html([("홈","/"),("브랜드 소개","/about/")]) + section_head("BRAND", f"{SITE['brand_full']} — 신뢰가 시작된 자리.") + """
""" + note_card(1, "처음 시작은 한 권역에서", [
        f"{SITE['stats']['since_year']}년 봄, 강남 한 권역에서 매니저 4명으로 시작했습니다.",
        "당시 시장에는 가격을 묻기 전에는 답이 오지 않는 업체, 도착 시간을 약속하지 않는 업체가 대부분이었습니다.",
        "우리는 '동네 가게처럼 정직한 출장마사지'를 만들기로 했고, 그 약속이 6년째 이어지고 있습니다.",
    ]) + note_card(2, "운영 철학 — 가격·시간·사람을 공개합니다", [
        "가격은 페이지에 명시합니다. 전화로 따로 흥정하지 않습니다.",
        "도착 시간은 권역별 평균값을 공개합니다. 예측 가능한 도착이 신뢰의 시작입니다.",
        "운영 책임자·자문 트레이너의 이름과 경력을 공개합니다. 누가 책임지는지 분명해야 합니다.",
    ]) + note_card(3, "확장의 원칙 — 천천히, 정확히", [
        "신규 권역 진입 시 최소 3개월간 매니저 가용성·도착시간·후기를 모니터링합니다.",
        f"현재 서울·경기·인천·부산 82개 행정구에서 활동 매니저 156명이 움직입니다.",
        "이 페이지에 적힌 모든 수치는 5개월간 23,700건 배차 로그를 기반으로 합니다.",
    ]) + note_card(4, "팀 — 본사 운영진 3명", [
        f"{SITE['people'][0]['name']} · {SITE['people'][0]['role']} · {SITE['people'][0]['exp']}: {SITE['people'][0]['scope']}.",
        f"{SITE['people'][1]['name']} · {SITE['people'][1]['role']} · {SITE['people'][1]['exp']}: {SITE['people'][1]['scope']}.",
        f"{SITE['people'][2]['name']} · {SITE['people'][2]['role']} · {SITE['people'][2]['exp']}: {SITE['people'][2]['scope']}.",
    ]) + note_card(5, "자문 — 트레이너 3인 검수", [
        f"{SITE['advisors'][0]['name']} · {SITE['advisors'][0]['role']} · {SITE['advisors'][0]['exp']}: {SITE['advisors'][0]['scope']}.",
        f"{SITE['advisors'][1]['name']} · {SITE['advisors'][1]['role']} · {SITE['advisors'][1]['exp']}: {SITE['advisors'][1]['scope']}.",
        f"{SITE['advisors'][2]['name']} · {SITE['advisors'][2]['role']} · {SITE['advisors'][2]['exp']}: {SITE['advisors'][2]['scope']}.",
    ]) + note_card(6, "콘텐츠 정책 — AI 사용 명시", [
        "본 사이트의 일부 글 초안은 AI 도구의 도움을 받습니다. 그러나 1차 데이터·운영 의사결정·후기 수집은 모두 사람이 직접 진행합니다.",
        "Google의 'Who, How, Why' 원칙에 따라 책임 저자·자문진·편집팀을 모두 공개합니다.",
        "잘못된 정보 발견 시 본 페이지 하단 이메일로 알려주시면 24시간 내 수정합니다.",
    ]) + """
<div class="signoff">📝 책임 편집: <b>{rep}</b> · 최종 갱신: <b>2026-05-20</b> · 문의: <b><a href="mailto:{email}">{email}</a></b></div>
</section>""".format(rep=SITE['company']['representative'], email=SITE['email']) + cta_band()

    title = f"브랜드 소개 — 마사지꾼"
    desc = f"마사지꾼 운영 철학·운영진 3명·자문 트레이너 3명·5개월 23,700건 배차 로그 기반 신뢰."

    return page(title, desc, "/about/", body, ld_objs=[
        organization_ld(),
        breadcrumb_ld([("홈","/"),("브랜드 소개","/about/")]),
    ])


# ---------- /pricing/ ----------

def pricing_page():
    cards = []
    for s in SERVICES:
        rows = "".join(f"<div><span>{m}분</span><span>{p:,}원</span></div>" for m, p in s["duration_options"])
        best_class = " best" if s["slug"] == "swedish" else ""
        best_badge = '<span class="best-badge">BEST</span>' if s["slug"] == "swedish" else ""
        cards.append(f"""<div class="price-card{best_class} reveal">{best_badge}
<span class="kicker">{s['kicker']}</span>
<h3>{s['name_ko']}</h3>
<p>{s['tag']}</p>
<div class="time-rows">{rows}</div>
</div>""")
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("요금","/pricing/")])}{section_head("PRICING","투명한 요금 — 전화로 흥정하지 않습니다.","모든 가격은 사이트에 명시된 그대로입니다. 심야·주말 할증 없음. 신규 가입비·구독료·연회비 없음.")}
<div class="price-grid">{"".join(cards)}</div>
{note_card(1,"가격 정책 — 명시 가격 외 추가 비용 없음",[
    "표기 가격은 출장비·재료비·세금이 모두 포함된 최종 가격입니다.",
    "심야(00시~06시)·주말 할증을 적용하지 않습니다.",
    "단, 가평·옹진군·연천 등 외곽 권역은 별도 출장비가 발생할 수 있으며 콜 시점에 미리 안내드립니다.",
])}
{note_card(2,"결제 방법",[
    "시술 시작 전 현금 또는 계좌이체로 결제합니다.",
    "사전 결제·예약금·구독은 운영하지 않습니다. 시술 시작 전까지 100% 취소 가능합니다.",
    "법인·세금계산서가 필요하신 경우 콜 시점에 말씀해주시면 발급해드립니다.",
])}
{note_card(3,"환불 정책",[
    "매니저 도착 전 취소: 100% 환불.",
    "시술 시작 전 취소: 100% 환불.",
    "시술 중단: 진행 시간 비례 환불. 예) 60분 코스 30분 시점 중단 → 50% 환불.",
    "매니저 귀책 사유로 인한 중단: 100% 환불 + 동일 코스 무료 재예약.",
])}
{note_card(4,"커플·동시 진행",[
    "두 분이 같은 공간에서 동시에 받는 커플 코스가 가능합니다.",
    "동일 코스 ×2 가격이며, 두 매니저가 동시에 출발합니다.",
    "특정 매니저 조합(예: 두 분 다 한국)을 원하시는 경우 사전에 말씀해주시면 가능 시간을 안내드립니다.",
])}
{note_card(5,"호텔·오피스텔 출장",[
    "프론트 통화 없이 객실까지 매니저가 직접 도착합니다.",
    "외국인 손님은 영어·일어·중국어 가능 매니저를 우선 배정합니다.",
    "호텔 별도 정책으로 출장이 제한되는 경우 있으니 사전 문의 부탁드립니다.",
])}
</section>{cta_band()}"""

    faqs = [("심야 할증이 있나요?","없습니다. 표기 가격이 24시간 동일하게 적용됩니다."),
            ("출장비는 따로 받나요?","수도권·부산 도심은 출장비가 포함된 가격입니다. 외곽 일부 권역만 별도 안내드립니다."),
            ("환불은 언제 가능한가요?","시술 시작 전까지 100% 환불 가능합니다.")]
    title = f"요금표 — 마사지꾼 출장마사지 가격"
    desc = f"스웨디시·아로마·타이·로미로미·스포츠 전 코스 가격. 심야 할증·사전 결제 없음."
    return page(title, desc, "/pricing/", body, ld_objs=[
        organization_ld(),
        breadcrumb_ld([("홈","/"),("요금","/pricing/")]),
        faq_ld(faqs),
    ])


# ---------- /reviews/ ----------

def reviews_page():
    cards = "".join(f"""<div class="review reveal">
<div class="stars">{"★" * r['rating']}{"☆" * (5 - r['rating'])}</div>
<div class="body">"{r['body']}"</div>
<div class="meta"><b>{r['name']}</b><span>·</span><span>{r['area']}</span><span>·</span><span>{r['course']}</span><span>·</span><span>{r['date']}</span></div>
</div>""" for r in GLOBAL_REVIEWS)

    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("후기","/reviews/")])}{section_head("REAL VOICES",f"실 후기 {len(GLOBAL_REVIEWS)}편 — 시술 다음날 직접 수집",f"평점 ★{SITE['stats']['rating']} · 누적 {SITE['stats']['review_count']:,}개 리뷰 중 최근 한 달 일부.")}
<div class="rv-grid">{cards}</div>
{note_card(1,"후기 수집 방식",[
    "모든 후기는 시술 다음날 SMS로 직접 수집됩니다.",
    "외부 후기 플랫폼에 의뢰하지 않으며, 자체 작성·자체 평점 조작을 하지 않습니다.",
    "별점 1~3점 후기도 삭제하지 않고 모두 누적합니다. 평균 평점은 그 결과입니다.",
])}
{note_card(2,"개인정보 보호",[
    "이름은 첫 글자만 노출합니다.",
    "주소는 행정구·동 단위까지만 노출하며, 정확한 호수·번지는 표시하지 않습니다.",
    "후기 게재 동의는 SMS 응답 시 명시적으로 확인합니다.",
])}
{note_card(3,"잘못된 후기 신고",[
    f"본인 후기가 잘못 게재된 경우 {SITE['email']}로 알려주시면 24시간 내 수정·삭제합니다.",
    "허위 후기가 의심되는 경우에도 동일 채널로 신고 부탁드립니다.",
    "신고된 후기는 내부 검토 후 즉시 비공개 처리합니다.",
])}
</section>{cta_band()}"""

    review_items = [{
        "@type": "Review",
        "author": {"@type": "Person", "name": r["name"]},
        "datePublished": r["date"],
        "reviewBody": r["body"],
        "reviewRating": {"@type": "Rating", "ratingValue": r["rating"], "bestRating": 5},
    } for r in GLOBAL_REVIEWS]
    ld_reviews = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "itemListElement": [{"@type": "ListItem", "position": i+1, "item": r} for i, r in enumerate(review_items)],
    }
    agg = {
        "@context": "https://schema.org",
        "@type": "AggregateRating",
        "itemReviewed": {"@type": "LocalBusiness", "name": SITE["brand_full"]},
        "ratingValue": SITE["stats"]["rating"],
        "reviewCount": SITE["stats"]["review_count"],
    }
    title = f"실 후기 — 마사지꾼 (★{SITE['stats']['rating']})"
    desc = f"누적 {SITE['stats']['review_count']:,}개 리뷰 중 최근 후기 {len(GLOBAL_REVIEWS)}편. 시술 다음날 SMS 수집 1차 후기."
    return page(title, desc, "/reviews/", body, ld_objs=[organization_ld(), breadcrumb_ld([("홈","/"),("후기","/reviews/")]), ld_reviews, agg])


# ---------- /contact/ ----------

def contact_page():
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("문의","/contact/")])}{section_head("CONTACT","24시 예약·문의 — 빠르고 정확하게.")}
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;margin-bottom:36px">
<div class="step reveal"><span class="n">·</span><h3>전화 예약 (권장)</h3>
<p style="margin-bottom:18px">평균 응답 30초. 권역·코스·시간만 알려주시면 즉시 가능 매니저와 ETA를 안내드립니다.</p>
<a class="btn btn-primary" href="tel:{SITE['phone_raw']}">📞 {SITE['phone_display']}</a></div>
<div class="step reveal"><span class="n">·</span><h3>이메일</h3>
<p style="margin-bottom:18px">예약·환불·후기 신고·제휴 문의. 영업일 기준 24시간 내 회신.</p>
<a class="btn btn-ghost" href="mailto:{SITE['email']}">{SITE['email']}</a></div>
<div class="step reveal"><span class="n">·</span><h3>운영 시간</h3>
<p style="margin-bottom:18px">{SITE['hours']}. 본사 디스패처가 365일 상주합니다.</p>
<span class="chip">현재 디스패처 1명 상시</span></div>
</div>
{note_card(1,"문의 전 확인 부탁드립니다",[
    "위치(행정구·동), 인원수(1인/2인 동시), 희망 코스와 길이, 가능한 시작 시간 — 4가지만 알려주시면 즉시 안내드립니다.",
    "외국인 손님은 'English manager please' 또는 '日本語マネージャー' 등으로 말씀해주시면 됩니다.",
    "법인·세금계산서·단체 예약은 사전 1일 이상 여유를 두고 이메일로 부탁드립니다.",
])}
{note_card(2,"호텔·오피스텔",[
    "프론트 통화 없이 객실까지 직접 도착합니다.",
    "일부 호텔은 자체 정책으로 출장 제한이 있을 수 있으니 콜 시점에 호텔명을 알려주시면 가능 여부를 미리 확인해드립니다.",
])}
{note_card(3,"환불·민원",[
    "환불 요청은 이메일·전화 모두 가능합니다.",
    "매니저 응대·시술 품질에 문제가 있었다면 즉시 본사로 연락 부탁드립니다.",
    "민원은 24시간 내 책임자 대면 또는 통화로 보고드립니다.",
])}
{note_card(4,"제휴·언론",[
    "호텔·오피스텔·기업 복지·언론 인터뷰 등의 문의는 이메일 부탁드립니다.",
    "보도자료·이미지 자료는 요청 시 24시간 내 제공해드립니다.",
])}
</section>{cta_band()}"""
    title = f"문의·예약 — 마사지꾼 24시 고객센터"
    desc = f"전화 {SITE['phone_display']} 24시 응답. 호텔·오피스텔 직접 도착, 다국어 매니저 가능."
    return page(title, desc, "/contact/", body, ld_objs=[organization_ld(), breadcrumb_ld([("홈","/"),("문의","/contact/")])])


# ---------- /policy/* ----------

def privacy_page():
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("정책","/policy/privacy/")])}{section_head("PRIVACY","개인정보처리방침","최종 개정: 2026-05-20")}
{note_card(1,"수집 항목",[
    "예약 시: 전화번호, 이름(또는 호칭), 시술 주소.",
    "후기 수집 시: SMS 응답 내용, 응답 시각.",
    "결제 시: 계좌이체 입금자명(현금 결제 시 미수집).",
    "민감정보·주민등록번호는 일체 수집하지 않습니다.",
])}
{note_card(2,"수집·이용 목적",[
    "매니저 배차 및 도착 안내.",
    "시술 후 후기 수집 및 품질 관리.",
    "환불·민원 처리.",
])}
{note_card(3,"보유 기간",[
    "예약 정보: 시술 완료일로부터 5년 (전자상거래법).",
    "후기 정보: 게재 동의 철회 시 즉시 삭제.",
    "민원 처리 기록: 3년 (소비자보호법).",
])}
{note_card(4,"제3자 제공",[
    "원칙적으로 제공하지 않습니다.",
    "법령에 따라 수사기관·법원의 적법한 요청이 있는 경우에만 제공됩니다.",
    "외부 결제대행사·홍보 대행사·해외 서버에 위탁·이전하지 않습니다.",
])}
{note_card(5,"이용자 권리",[
    f"열람·정정·삭제·처리정지 요구는 {SITE['email']} 또는 {SITE['phone_display']}로 요청 가능합니다.",
    "요청 접수 후 10일 이내에 처리하며, 결과를 동일 채널로 회신해드립니다.",
])}
{note_card(6,"개인정보보호책임자",[
    f"성명: {SITE['company']['privacy_officer']}",
    f"연락처: {SITE['phone_display']} / {SITE['email']}",
    f"소속: {SITE['company']['legal_name']} (사업자등록번호 {SITE['company']['biz_no']})",
])}
</section>{cta_band(title='무엇이든 편하게 문의해주세요.', desc='개인정보 관련 요청도 24시간 응답해드립니다.')}"""
    title = "개인정보처리방침 — 마사지꾼"
    desc = f"마사지꾼 개인정보 수집·이용·보유·제3자 제공·이용자 권리 안내."
    return page(title, desc, "/policy/privacy/", body, ld_objs=[organization_ld(), breadcrumb_ld([("홈","/"),("개인정보처리방침","/policy/privacy/")])])


def terms_page():
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("정책","/policy/terms/")])}{section_head("TERMS","이용약관","최종 개정: 2026-05-20")}
{note_card(1,"제1조 (목적)",[
    f"본 약관은 {SITE['company']['legal_name']}(이하 '회사')이 제공하는 출장마사지 서비스 '{SITE['brand_full']}'(이하 '서비스')의 이용 조건을 정합니다.",
    "이용자는 본 약관에 동의한 것으로 간주되며, 본 약관에 동의하지 않는 경우 서비스를 이용할 수 없습니다.",
])}
{note_card(2,"제2조 (서비스 내용)",[
    "회사는 출장 형태의 마사지·이완·건강관리 서비스를 제공합니다.",
    "본 서비스는 의료 행위가 아니며, 통증·질환의 치료를 목적으로 하지 않습니다.",
    "19세 미만 청소년은 본 서비스를 이용할 수 없습니다.",
])}
{note_card(3,"제3조 (예약·결제)",[
    "예약은 전화·이메일로 접수되며, 회사의 가용성 확인 후 확정됩니다.",
    "결제는 시술 시작 전 현금·계좌이체로 진행됩니다.",
    "회사는 사전 결제·구독·연회비를 청구하지 않습니다.",
])}
{note_card(4,"제4조 (환불·취소)",[
    "매니저 도착 전 취소: 100% 환불.",
    "시술 시작 전 취소: 100% 환불.",
    "시술 중단: 진행 시간 비례 환불.",
    "매니저 귀책 사유로 인한 중단: 100% 환불 + 동일 코스 무료 재예약.",
])}
{note_card(5,"제5조 (이용자의 의무)",[
    "이용자는 시술 환경(청결·온도·조명·소음)을 합리적으로 유지할 의무가 있습니다.",
    "매니저에 대한 부적절한 요구·언행·신체 접촉이 있을 경우 회사는 즉시 시술을 중단하고 전액 비환불 조치할 수 있습니다.",
    "음주 후 시술 요청은 안전상 거절될 수 있습니다.",
])}
{note_card(6,"제6조 (회사의 의무)",[
    "회사는 매니저의 자격·교육·안전을 관리할 책임이 있습니다.",
    "회사는 시술 중 발생한 사고에 대해 자체 보험 한도 내에서 책임을 부담합니다.",
    "회사는 본 약관·관련 법령을 위반하지 않는 범위에서 서비스를 제공합니다.",
])}
{note_card(7,"제7조 (분쟁 해결)",[
    "본 약관과 관련된 분쟁은 회사 본사 소재지 관할 법원을 1심 법원으로 합니다.",
    "민원·환불 분쟁은 우선 회사 고객센터를 통해 협의로 해결합니다.",
])}
</section>{cta_band()}"""
    title = "이용약관 — 마사지꾼"
    desc = f"마사지꾼 서비스 내용·예약·결제·환불·이용자·회사 의무·분쟁 해결 절차."
    return page(title, desc, "/policy/terms/", body, ld_objs=[organization_ld(), breadcrumb_ld([("홈","/"),("이용약관","/policy/terms/")])])


def youth_page():
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("정책","/policy/youth/")])}{section_head("YOUTH PROTECTION","청소년보호정책","최종 개정: 2026-05-20")}
{note_card(1,"제1조 (목적)",[
    f"본 정책은 {SITE['brand_full']}이 청소년(만 19세 미만)을 유해 환경으로부터 보호하기 위해 마련된 기준입니다.",
])}
{note_card(2,"제2조 (이용 제한)",[
    "본 서비스는 만 19세 이상에게만 제공되며, 청소년은 어떠한 경우에도 이용할 수 없습니다.",
    "예약 시 본인 확인이 필요한 경우 신분증을 요청할 수 있습니다.",
])}
{note_card(3,"제3조 (청소년 유해 정보 차단)",[
    "회사는 사이트 내에 청소년에게 유해한 이미지·표현·언어를 사용하지 않습니다.",
    "외부 광고·배너·팝업을 게재하지 않으며, 외부 결제 페이지로 이동시키지 않습니다.",
])}
{note_card(4,"제4조 (청소년보호책임자)",[
    f"성명: {SITE['company']['privacy_officer']}",
    f"연락처: {SITE['phone_display']} / {SITE['email']}",
    "청소년 유해 정보 발견 시 즉시 신고 부탁드립니다. 24시간 내 처리합니다.",
])}
{note_card(5,"제5조 (신고 채널)",[
    f"메일: {SITE['email']}",
    f"전화: {SITE['phone_display']}",
    "방송통신심의위원회 신고: 1377",
])}
</section>{cta_band()}"""
    title = "청소년보호정책 — 마사지꾼"
    desc = f"마사지꾼 청소년 이용 제한·유해 정보 차단·청소년보호책임자 안내."
    return page(title, desc, "/policy/youth/", body, ld_objs=[organization_ld(), breadcrumb_ld([("홈","/"),("청소년보호정책","/policy/youth/")])])
