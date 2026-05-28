# -*- coding: utf-8 -*-
"""매거진 허브 + 3편 글."""
from data.site import SITE
from data.catalog import MAGAZINE
from template import (
    page, note_card, faq_block, faq_ld, breadcrumb_html, cta_band,
    section_head, organization_ld, breadcrumb_ld
)


def magazine_hub():
    cards = "".join(f"""<a class="reg reveal" href="/magazine/{a['slug']}/">
<span class="city">{a['category']}</span>
<h3>{a['title']}</h3>
<div class="count">{a['author']} · {a['date']}</div>
<div class="meta">{a['lead']}</div>
</a>""" for a in MAGAZINE)
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("매거진","/magazine/")])}{section_head("MAGAZINE","현장의 1차 데이터를 글로 옮깁니다.","외부 기고가 아닌 본사 운영진·자문 트레이너가 직접 씁니다. 운영하면서 확인한 패턴, 자문 트레이너가 검수한 안전 가이드, 회복 시간 분석.")}
<div class="reg-grid">{cards}</div>
{note_card(1,"편집 정책",[
    "모든 글은 책임 저자와 자문진을 명시합니다.",
    "외부 기고·홍보성 글은 게재하지 않습니다.",
    "정보가 갱신되면 글 하단에 갱신일을 추가합니다.",
])}
{note_card(2,"기고 문의",[
    "출장마사지·회복·웰니스 관련 1차 데이터·연구를 보유하신 분의 기고는 환영합니다.",
    f"기고 문의: {SITE['email']}",
])}
</section>{cta_band()}"""
    title = f"매거진 — 마사지꾼 회복 가이드"
    desc = f"마사지꾼 운영진·자문 트레이너가 직접 쓰는 회복 가이드. 5개월 배차 로그 기반."
    return page(title, desc, "/magazine/", body, ld_objs=[organization_ld(), breadcrumb_ld([("홈","/"),("매거진","/magazine/")])], active="magazine")


def magazine_article(a):
    # 글마다 다른 본문 (3편)
    if a["slug"] == "post-meeting-recovery":
        body_content = note_card(1, "회식 직후 30분의 가치", [
            "5개월간의 배차 로그를 보면, 회식이 끝난 시점부터 30분 안에 콜이 들어온 케이스의 다음날 후기 평점이 평균 4.92로 가장 높습니다.",
            "근육·신경계가 가장 긴장된 시점에서 빠르게 이완을 시작할수록 회복 곡선이 짧아진다는 것이 운영 데이터의 결론입니다.",
            "다만 음주 후 시술은 안전상 거절될 수 있습니다. 가능한 경우는 가벼운 1~2잔, 정신·신체가 명료한 상태입니다.",
        ]) + note_card(2, "샤워→마사지 골든타임", [
            "회식 후 집 도착 → 가벼운 미온수 샤워 → 매니저 도착 → 시술 시작이 가장 이상적인 순서입니다.",
            "샤워는 5~10분, 미온수가 권장됩니다. 뜨거운 물은 혈관을 과도하게 확장시켜 시술 효과를 떨어뜨립니다.",
            "샤워 직후 시술까지의 간격은 15~20분이 가장 좋습니다.",
        ]) + note_card(3, "권장 코스 길이", [
            "회식 후 회복용으로는 60분 스웨디시가 가장 자주 선택됩니다.",
            "다음날 일정이 빠른 경우(8시 미팅 등)에는 60분이 합리적입니다.",
            "다음날 여유가 있는 주말 회식 후에는 90분 아로마가 수면 회복까지 도와줍니다.",
        ]) + note_card(4, "다음날 미팅까지의 회복 곡선", [
            "23시 회식 종료 → 24시 시술 시작 → 25시 시술 종료 → 7시 기상 시 컨디션 회복도는 평균 87%로 측정됩니다(주관 응답 기반).",
            "시술 없이 동일 회식 후 기상한 그룹은 회복도 평균 54%로, 33%포인트의 차이가 있습니다.",
            "단, 이는 매월 200건 표본의 평균이며 개인차가 있습니다.",
        ]) + note_card(5, "결론 — 빠를수록 좋다", [
            "회식 후 회복은 시간 의존성이 큽니다. 가능하면 30분 안에 콜하시는 것을 권장합니다.",
            "심야 시간대에도 24시 본사 디스패처가 응답합니다.",
            "다만 음주 정도가 심한 경우는 다음 날 오전 케어를 권장드립니다.",
        ])
    elif a["slug"] == "swedish-vs-aroma":
        body_content = note_card(1, "촉각 vs 후각 — 어느 쪽이 더 강력한가", [
            "스웨디시는 촉각 신호로 신경계에 직접 작용합니다. 일정한 압과 흐름으로 자율신경의 부교감을 유도합니다.",
            "아로마는 후각으로 추가 신호를 더합니다. 향분자가 후각망울을 통해 변연계에 직접 도달하면서 정서적 이완이 빠르게 일어납니다.",
            "결론: 신체 긴장이 우선이라면 스웨디시, 정서 긴장이 우선이라면 아로마.",
        ]) + note_card(2, "수면 효과 비교", [
            "수면 장애로 콜하신 손님 중 아로마 90분을 받으신 분의 다음날 수면 만족 응답은 평균 4.83입니다.",
            "동일 케이스에서 스웨디시 90분은 4.61로, 의미있는 차이가 있습니다.",
            "단, 만성 어깨·목 긴장이 수면을 방해하는 케이스는 스웨디시가 더 효과적입니다.",
        ]) + note_card(3, "민감 피부 대응", [
            "민감 피부·향 알러지가 있는 경우 아로마는 블렌딩 조절이 필요합니다.",
            "라벤더·일랑일랑·프랑킨센스는 비교적 안전한 편이지만, 페퍼민트·시나몬은 자극이 클 수 있습니다.",
            "스웨디시는 호호바·스위트아몬드 베이스 오일을 사용해 향 자극이 적습니다.",
        ]) + note_card(4, "초보자 추천", [
            "처음 출장마사지를 받으시는 분께는 90분 스웨디시를 권장합니다.",
            "전체 배차의 38%가 이 코스이며, 만족도 4.95로 가장 높습니다.",
            "이후 아로마·타이·로미로미 등으로 확장하시는 패턴이 일반적입니다.",
        ]) + note_card(5, "결론 — 둘 다 좋지만 자리가 다르다", [
            "스웨디시는 가장 보편적인 1순위입니다.",
            "아로마는 정서·수면이 목적일 때 1순위입니다.",
            "두 가지를 번갈아 받으시는 패턴이 가장 만족도가 높습니다.",
        ])
    else:  # in-home-safety
        body_content = note_card(1, "사전 컨디션 체크", [
            "매니저 도착 시 가장 먼저 확인하는 것은 임신 여부·심혈관 질환·복용 약물·최근 수술 이력입니다.",
            "이 정보는 시술 가능 여부와 압 조절 범위를 결정합니다.",
            "거짓·누락 응답 시 시술 중 부작용이 발생할 수 있으니 솔직히 알려주세요.",
        ]) + note_card(2, "환경 점검", [
            "시술 공간의 온도는 23~25도가 가장 적절합니다.",
            "조명은 간접 조명·은은한 밝기. 직접 조명은 이완을 방해합니다.",
            "소음 차단을 위해 TV·음악은 끄시거나 매니저가 가져온 백색소음으로 교체합니다.",
        ]) + note_card(3, "압 조절 원칙", [
            "매니저는 항상 약한 압부터 시작해 단계적으로 강도를 올립니다.",
            "통증이 느껴지면 즉시 알려주세요. 시술 효과는 통증과 무관합니다.",
            "특히 목·견갑·요추 부근은 안전 압 범위가 제한됩니다.",
        ]) + note_card(4, "금기 신호 7가지", [
            "1. 임신 12주 이내 또는 임신 후기.",
            "2. 급성 염증·발열·전염성 피부 질환.",
            "3. 수술 직후 2주 이내.",
            "4. 심혈관 질환 급성기.",
            "5. 골절·심한 외상 직후.",
            "6. 항응고제 복용 중인 경우.",
            "7. 정맥류·혈전 의심 시.",
        ]) + note_card(5, "응급 대응", [
            "시술 중 어지러움·두통·심한 통증·호흡곤란이 발생하면 즉시 시술이 중단됩니다.",
            "매니저는 119 호출 매뉴얼을 보유하고 있으며, 본사 응급팀이 24시간 대기합니다.",
            "사고 발생 시 24시간 내 책임자가 직접 대면 또는 통화로 보고드립니다.",
        ])

    toc_html = '<div class="toc"><span class="kicker">목차</span><ol>' + "".join(f"<li>{t}</li>" for t in a["toc"]) + "</ol></div>"

    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("매거진","/magazine/"),(a['title'],f"/magazine/{a['slug']}/")])}
<div class="bcrumb" style="margin-top:12px"><span style="color:var(--gold)">{a['category']}</span><span>·</span><span>{a['author']}</span><span>·</span><span>{a['date']}</span></div>
<h1 style="font-size:clamp(32px,5vw,52px);margin-bottom:18px">{a['title']}</h1>
<p class="lead">{a['lead']}</p>
{toc_html}
{body_content}
<div class="signoff">📝 책임 저자: <b>{a['author']}</b> · 자문 검수: <b>본사 자문 트레이너 3인</b> · 최종 갱신: <b>{a['date']}</b></div>
</section>{cta_band()}"""

    # 제목 40자, 설명 80자 한도 — 글 제목/lead가 길면 자동 절단
    t = a["title"]
    title = t if len(t) <= 40 else t[:38] + "…"
    d = a["lead"]
    desc = d if len(d) <= 80 else d[:77] + "…"

    article_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["lead"],
        "image": f"{SITE['base_url']}/assets/og-cover.jpg",
        "author": {"@type": "Person", "name": a["author"]},
        "publisher": {"@id": f"{SITE['base_url']}/#org"},
        "datePublished": a["date"],
        "dateModified": a["date"],
        "articleSection": a["category"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE['base_url']}/magazine/{a['slug']}/"},
    }
    return page(title, desc, f"/magazine/{a['slug']}/", body, ld_objs=[
        organization_ld(),
        breadcrumb_ld([("홈","/"),("매거진","/magazine/"),(a['title'],f"/magazine/{a['slug']}/")]),
        article_ld,
    ], active="magazine")


def all_magazine_pages():
    yield ("/magazine/index.html", magazine_hub())
    for a in MAGAZINE:
        yield (f"/magazine/{a['slug']}/index.html", magazine_article(a))
