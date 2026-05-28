# -*- coding: utf-8 -*-
"""관리사 허브 + 6개 국적 상세."""
from data.site import SITE
from data.catalog import THERAPISTS
from template import (
    page, note_card, faq_block, faq_ld, breadcrumb_html, cta_band,
    section_head, organization_ld, breadcrumb_ld
)


def therapist_hub():
    cards = "".join(f"""<a class="svc reveal" href="/therapists/{t['slug']}/">
<span class="kicker">{t['flag']} · {t['exp_avg']}</span>
<h3>{t['name_ko']}</h3>
<p>{t['desc']}</p>
<span class="svc-link">자세히 보기 →</span>
</a>""" for t in THERAPISTS)
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("관리사","/therapists/")])}{section_head("THERAPISTS","6개국 156명, 정확한 배정의 시작.","국적은 단순한 분류가 아니라 손기술의 결을 결정합니다. 한국식 섬세함, 중국식 심부 압, 태국식 스트레칭 — 권역·상황·체형에 맞춰 배정해드립니다.")}
<div class="svc-grid">{cards}</div>
{note_card(1,"매니저 채용·교육",[
    "모든 매니저는 1차 서류·2차 실기·3차 면담을 통과한 후 본사 직접 교육 80시간을 이수합니다.",
    "교육은 자문 트레이너 박지연(KSPO)·정민호(PT)·윤하늬(IFA)가 직접 참여합니다.",
    "정식 배차 전 본사 시뮬레이션 5회를 거쳐 합격해야 배차가 시작됩니다.",
])}
{note_card(2,"배차 알고리즘 — 권역·언어·전문성",[
    "본사 디스패처는 위치·매니저 가용 시간·코스 적합도·언어를 동시에 고려합니다.",
    "외국인 손님은 영어·일어·중국어 가능 매니저를 우선 배정합니다.",
    "단골 매니저 재배차도 가능합니다. 콜 시점에 매니저 이니셜만 알려주시면 됩니다.",
])}
{note_card(3,"매니저 평가·재교육",[
    "매니저별 평점·후기·민원이 실시간으로 본사 시스템에 누적됩니다.",
    "분기마다 상위 10% 우수 매니저에게는 인센티브, 평점 하위는 재교육·시뮬레이션이 진행됩니다.",
    "민원 누적 매니저는 자동으로 배차에서 제외되며, 본사 면담 후 복귀 여부를 결정합니다.",
])}
{note_card(4,"안전·인권",[
    "매니저에 대한 부적절한 요구·언행·신체 접촉이 있을 경우 회사는 즉시 시술을 중단하고 전액 비환불 조치합니다.",
    "매니저는 본사로 SOS 신호를 즉시 보낼 수 있으며, 본사는 24시간 대응 인력을 운영합니다.",
    "외국인 매니저의 경우 한국어가 부족하더라도 본사 통역을 통해 본사와 즉시 연결 가능합니다.",
])}
{note_card(5,"문의 — 매니저 지정",[
    "특정 매니저를 다시 받고 싶으시면 콜 시점에 이전 매니저의 이니셜 또는 시술 일자를 알려주세요.",
    "본사 시스템에서 매칭 후 가능 시간을 안내드립니다.",
    "권역에 따라 특정 매니저가 비활동 중일 수 있습니다.",
])}
</section>{cta_band()}"""
    faqs = [("매니저 국적을 고를 수 있나요?","네, 6개국 매니저 중 권역별 가용 인원을 안내드립니다."),
            ("매니저 재지정이 가능한가요?","가능합니다. 콜 시점에 이전 매니저 이니셜을 알려주세요."),
            ("외국인 매니저는 한국어가 가능한가요?","대부분 기본 한국어가 가능하며, 본사 통역도 24시간 대기합니다.")]
    title = f"관리사 소개 — 마사지꾼 6개국 156명"
    desc = f"한국·중국·태국·베트남·러시아·일본 매니저 156명. 본사 80시간 교육·실시간 평가."
    return page(title, desc, "/therapists/", body, ld_objs=[organization_ld(), breadcrumb_ld([("홈","/"),("관리사","/therapists/")]), faq_ld(faqs)], active="therapists")


def therapist_detail(t):
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("관리사","/therapists/"),(t['name_ko'],f"/therapists/{t['slug']}/")])}{section_head(f"{t['flag']} · {t['exp_avg']}", f"{t['name_ko']} — {t['strength']}", t['desc'])}
{note_card(1,f"{t['name_ko']}의 손기술 특징",[
    f"가장 큰 강점: {t['strength']}.",
    f"평균 경력은 {t['exp_avg']}로 현재 활동 매니저는 {t['count']}명입니다.",
    f"{t['name_ko']}은(는) 권역에 따라 가용성이 다르며, 본사 디스패처가 콜 시점에 정확한 가용 인원을 안내드립니다.",
])}
{note_card(2,"가장 자주 선택되는 코스",[
    f"{t['name_ko']}이(가) 가장 자주 진행하는 코스는 90분 스웨디시와 90분 아로마입니다.",
    "각 매니저의 주특기 코스는 본사 시스템에 기록되어 있어 코스 적합도가 가장 높은 매니저가 배정됩니다.",
    "특정 코스(예: 스포츠·로미로미)는 자격을 보유한 매니저만 진행합니다.",
])}
{note_card(3,"언어·소통",[
    "한국어 기본 의사소통은 모든 매니저가 가능합니다.",
    "외국인 매니저는 본사 통역이 24시간 대기 중이므로 의사소통에 불편이 없습니다.",
    "외국인 손님은 영어·일어·중국어 가능 매니저를 우선 배정합니다.",
])}
{note_card(4,"교육·검수",[
    "모든 매니저는 입사 후 본사 교육 80시간을 이수합니다.",
    "교육 내용은 안전 압 범위, 금기 신호, 자세별 가이드라인, 응급 대응 매뉴얼입니다.",
    "분기별 재교육이 진행되며, 평점 4.7 미만은 자동으로 재교육 대상이 됩니다.",
])}
{note_card(5,"단골 재지정",[
    "이전에 받으셨던 매니저를 다시 받고 싶으시면 콜 시점에 이니셜과 시술 일자를 알려주세요.",
    "본사 시스템에서 매칭 후 가능 시간을 안내드립니다.",
    "단골 매니저 가용성이 없는 경우 동일 강점·경력대의 매니저를 추천해드립니다.",
])}
</section>{cta_band(title=f'{t["name_ko"]} 배정 예약', desc=f'현재 활동 {t["count"]}명 — 권역에 따라 가용성이 다릅니다. 전화로 가능 매니저를 안내드립니다.')}"""
    faqs = [(f"{t['name_ko']} 매니저는 한국어가 가능한가요?","기본 한국어 의사소통은 가능하며, 본사 통역이 24시간 대기 중입니다."),
            (f"{t['name_ko']} 매니저는 어떤 코스를 잘하나요?", f"{t['strength']} 코스에 강점이 있습니다."),
            (f"{t['name_ko']} 매니저를 지정할 수 있나요?","가능합니다. 권역에 따라 가용성이 달라 콜 시점에 안내드립니다.")]
    title = f"{t['name_ko']} 출장마사지 — 마사지꾼 ({t['count']}명)"
    desc = f"{t['name_ko']} 손기술: {t['strength']}. {t['exp_avg']}·활동 {t['count']}명. 24시 출장."
    return page(title, desc, f"/therapists/{t['slug']}/", body, ld_objs=[
        organization_ld(),
        breadcrumb_ld([("홈","/"),("관리사","/therapists/"),(t['name_ko'],f"/therapists/{t['slug']}/")]),
        faq_ld(faqs),
    ], active="therapists")


def all_therapist_pages():
    yield ("/therapists/index.html", therapist_hub())
    for t in THERAPISTS:
        yield (f"/therapists/{t['slug']}/index.html", therapist_detail(t))
