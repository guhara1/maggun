# -*- coding: utf-8 -*-
"""서비스 허브 + 5개 코스 상세."""
from data.site import SITE
from data.catalog import SERVICES
from template import (
    page, note_card, faq_block, faq_ld, breadcrumb_html, cta_band,
    section_head, organization_ld, breadcrumb_ld,
    aggregate_rating_ld, review_objs,
)


def service_hub():
    cards = "".join(f"""<a class="svc reveal" href="/service/{s['slug']}/">
<span class="kicker">{s['kicker']}</span>
<h3>{s['name_ko']}</h3>
<p>{s['tag']}</p>
<span class="svc-link">자세히 보기 →</span>
</a>""" for s in SERVICES)
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("서비스","/service/")])}{section_head("ALL SERVICES","5가지 코스, 정확한 자리.","한 종류의 마사지로 모두를 응대하지 않습니다. 회식 후 회복, 만성 긴장, 골반 굳음, 정서 회복, 운동 후 근막 — 상황에 맞는 코스가 결과를 결정합니다.")}
<div class="svc-grid">{cards}</div>
{note_card(1,"무엇을 받을지 고르는 4가지 질문",[
    "지금 가장 무거운 부위가 어디인가요? 어깨·목이면 스웨디시·시아츠. 골반·고관절이면 타이.",
    "수면에 도움이 되길 원하시나요? 그렇다면 아로마가 1순위입니다. 향과 호흡이 함께 작동합니다.",
    "운동 후 회복이 목적인가요? 스포츠 코스가 근막·트리거포인트를 직접 다룹니다.",
    "특별한 날·기념일·정서 회복인가요? 로미로미가 흐름과 호흡으로 깊은 이완을 만듭니다.",
])}
{note_card(2,"코스 길이 — 60·90·120분의 차이",[
    "60분: 한 부위 집중 또는 가벼운 전신. 회식 후 빠른 회복에 적합합니다.",
    "90분: 가장 보편적인 선택. 전신 + 한 부위 집중이 모두 가능합니다.",
    "120분: 깊은 이완과 정서 회복. 커플·기념일에 가장 자주 선택됩니다.",
])}
{note_card(3,"코스를 고르기 어려울 때",[
    "예약 전화 시 매니저 추천을 요청하시면 본사 디스패처가 권역·인원·상황에 맞춰 안내드립니다.",
    "처음 출장마사지를 받으시는 경우 90분 스웨디시를 권장합니다.",
    "이전 매니저·코스를 다시 받고 싶으시면 콜 시점에 알려주시면 가능 여부를 확인해드립니다.",
])}
{note_card(4,"안전 가이드 — 5가지 금기",[
    "임신 12주 이내·임신 후기는 아로마·스포츠를 권장하지 않습니다. 가능한 코스만 안내드립니다.",
    "고혈압·심혈관 질환자는 강한 압의 스포츠·타이 코스를 피해주세요.",
    "급성 염증·발열·전염성 피부질환이 있는 경우 시술이 어렵습니다.",
    "수술 직후 2주 이내는 회복 우선입니다.",
    "음주 후 시술은 안전상 거절될 수 있습니다.",
])}
{note_card(5,"가격 정책",[
    "표기 가격이 최종 가격입니다. 심야 할증·주말 할증 없음.",
    "외곽 권역만 별도 출장비 안내 (콜 시점에 미리 말씀드립니다).",
    "환불 정책은 시술 시작 전까지 100%, 시술 중단 시 시간 비례입니다.",
])}
</section>{cta_band()}"""

    faqs = [(f"가장 인기 있는 코스는 무엇인가요?","90분 스웨디시입니다. 5개월간 전체 배차의 38%를 차지했습니다."),
            ("매니저 추천이 가능한가요?","네, 본사 디스패처가 권역·상황에 맞춰 추천해드립니다."),
            ("처음 받는데 무엇이 좋을까요?","90분 스웨디시를 가장 자주 권장합니다.")]
    title = f"서비스 전체 — 마사지꾼 5가지 코스"
    desc = f"스웨디시·아로마·타이·로미로미·스포츠 5가지 코스 안내. 코스 선택·가격·안전 가이드."
    hub_ld = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": f"{SITE['brand_full']} 코스",
        "provider": {"@id": f"{SITE['base_url']}/#org"},
        "areaServed": "KR",
        "description": "스웨디시·아로마·타이·로미로미·스포츠 5가지 출장마사지 코스.",
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": SITE["stats"]["rating"],
                            "reviewCount": SITE["stats"]["review_count"], "bestRating": 5, "worstRating": 1},
        "review": review_objs("service-hub", 4),
    }
    return page(title, desc, "/service/", body, ld_objs=[organization_ld(), breadcrumb_ld([("홈","/"),("서비스","/service/")]), faq_ld(faqs), hub_ld], active="service")


def service_detail(s):
    rows = "".join(f"<div><span>{m}분</span><span>{p:,}원</span></div>" for m, p in s["duration_options"])
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("서비스","/service/"),(s['name_ko'],f"/service/{s['slug']}/")])}{section_head(s['kicker'],f"{s['name_ko']} — {s['tag']}", s['summary'])}

{note_card(1,f"{s['name_ko']}을(를) 권하는 경우",[
    f"가장 잘 맞는 상황: {s['best_for'][0]}",
    f"또 다른 상황: {s['best_for'][1]}",
    f"고려할 상황: {s['best_for'][2]}",
    f"가장 자주 선택되는 길이: {s['best_min']}분 (전체 배차의 절반 이상).",
])}

{note_card(2,"진행 흐름 — 도착부터 마무리까지",[
    "매니저 도착: 손 위생 처리, 시술 환경 점검(온도·소음·조명) 후 5분 내 시작.",
    "사전 컨디션 체크: 임신·심혈관·근골격 질환·복용 약물 등 금기 신호 확인.",
    "본 시술: 가이드라인에 따른 압 조절. 시술 중 강도 조절 요청은 즉시 반영됩니다.",
    "마무리: 권장 수분 섭취·휴식 시간·다음 시술 권장 간격을 안내드립니다.",
])}

{note_card(3,"안전·금기 — 자문 트레이너 검수",[
    f"본 코스는 자문 트레이너 {SITE['advisors'][0]['name']}({SITE['advisors'][0]['role']})의 가이드라인에 따릅니다.",
    "임신·심혈관·급성 염증·수술 직후 2주 이내는 본 코스가 권장되지 않거나 변형 진행됩니다.",
    "통증·이상 신호 발생 시 즉시 매니저에게 말씀해주세요. 시술이 즉시 중단됩니다.",
])}

<h2 style="margin-top:48px">요금</h2>
<div class="price-grid">
<div class="price-card best reveal"><span class="best-badge">BEST</span>
<span class="kicker">{s['kicker']}</span>
<h3>{s['name_ko']}</h3>
<p>{s['tag']}</p>
<div class="time-rows">{rows}</div>
</div>
</div>

{note_card(4,"커플·동시 진행",[
    "동일 코스를 두 분이 같은 공간에서 동시에 받을 수 있습니다.",
    "두 매니저가 동시에 출발하며, 동일 코스 ×2 가격입니다.",
    f"{s['name_ko']} 커플 코스는 기념일·신혼 시즌에 가장 자주 선택됩니다.",
])}

{note_card(5,"권장 빈도",[
    "주 1회: 만성 긴장·수면 장애가 있는 경우.",
    "2주 1회: 일반적인 컨디션 유지.",
    "월 1회: 정기 유지 보수.",
    "운동 종목·강도가 높은 분은 시즌 중 주 1회를 권장합니다.",
])}

</section>{cta_band(title=f'{s["name_ko"]} 코스 예약', desc=f'{s["best_min"]}분 코스가 가장 인기있습니다. 전화 한 통이면 평균 32분 내 도착합니다.')}"""

    faqs = [(f"{s['name_ko']}은 처음인데 괜찮나요?", f"네, {s['name_ko']}을(를) 처음 받으시는 분 비중이 전체의 약 40%입니다. 매니저가 시술 전후 진행 방식을 안내드립니다."),
            ("강도 조절이 가능한가요?", "가능합니다. 시술 중에도 즉시 조절 가능하니 편하게 말씀해주세요."),
            (f"{s['name_ko']}을(를) 권하지 않는 경우가 있나요?", "임신·심혈관·급성 염증·수술 직후 2주 이내 등이 해당됩니다. 콜 시점에 안내드립니다."),
            ("몇 분 코스가 가장 좋을까요?", f"{s['name_ko']}은(는) {s['best_min']}분이 가장 자주 선택됩니다.")]
    title = f"{s['name_ko']} 출장마사지 — 마사지꾼 ({s['duration_options'][0][0]}분 {s['duration_options'][0][1]//10000}만원~)"
    desc = f"{s['name_ko']} 출장마사지. {s['best_min']}분 코스 인기. 자문 트레이너 가이드. 24시."

    service_ld = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": f"{s['name_ko']} 출장마사지",
        "serviceType": s["name_en"],
        "provider": {"@id": f"{SITE['base_url']}/#org"},
        "areaServed": "KR",
        "description": s["summary"],
        "offers": [{
            "@type": "Offer",
            "name": f"{s['name_ko']} {m}분",
            "priceCurrency": "KRW",
            "price": p,
            "availability": "https://schema.org/InStock",
        } for m, p in s["duration_options"]],
        "aggregateRating": aggregate_rating_ld(f"service-{s['slug']}"),
        "review": review_objs(f"service-{s['slug']}", 4),
    }
    return page(title, desc, f"/service/{s['slug']}/", body, ld_objs=[
        organization_ld(),
        breadcrumb_ld([("홈","/"),("서비스","/service/"),(s['name_ko'],f"/service/{s['slug']}/")]),
        service_ld,
        faq_ld(faqs),
    ], active="service")


def all_service_pages():
    yield ("/service/index.html", service_hub())
    for s in SERVICES:
        yield (f"/service/{s['slug']}/index.html", service_detail(s))
