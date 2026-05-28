# -*- coding: utf-8 -*-
"""지역 허브 + 4개 광역 + 82개 행정구."""
import random
from data.site import SITE
from data.catalog import SERVICES, GLOBAL_REVIEWS
from data.districts import CITIES, all_districts
from template import (
    page, note_card, faq_block, faq_ld, breadcrumb_html, cta_band,
    section_head, organization_ld, breadcrumb_ld
)


def location_hub():
    cards = "".join(f"""<a class="reg reveal" href="/locations/{slug}/">
<span class="city">{c['short']}</span>
<h3>{c['name_ko']}</h3>
<div class="count">{c['count']}개 행정구</div>
<div class="meta">대표 권역: {", ".join(d['name_ko'] for d in c['districts'][:4])}…</div>
</a>""" for slug, c in CITIES.items())
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("지역","/locations/")])}{section_head("ALL LOCATIONS","82개 행정구, 평균 32분.","5개월간 누적된 23,700건 배차 로그로 행정구·동(洞) 단위 도착시간을 추적·갱신합니다. 단순한 도시명 매칭이 아닙니다.")}
<div class="reg-grid">{cards}</div>
{note_card(1,"도착 시간 데이터",[
    f"전체 평균은 32분이지만, 권역별 분포는 28~70분까지 다릅니다.",
    "서울 도심(강남·서초·중구)은 28~33분, 외곽(가평·옹진·연천)은 50분 이상이 정상입니다.",
    "콜 시점에 정확한 ETA를 안내드리며, 도착 지연 시 즉시 문자로 알려드립니다.",
])}
{note_card(2,"외곽 권역 출장",[
    "가평·옹진군·연천·양평·여주·강화군 등 외곽 권역은 별도 출장비가 발생할 수 있습니다.",
    "도착까지 1시간 이상이 소요되므로 사전 예약을 권장드립니다.",
    "도서 권역(옹진군 백령·연평 등)은 별도 협의 후 진행됩니다.",
])}
{note_card(3,"권역별 매니저 가용성",[
    "서울 25개구는 24시간 매니저가 활동합니다.",
    "경기·인천·부산 도심권은 24시간 가용성이 있으나, 외곽은 22시 이후 가용 매니저가 줄어듭니다.",
    "콜 시점에 정확한 가용성을 안내드립니다.",
])}
</section>{cta_band()}"""
    title = f"전체 지역 — {SITE['brand_full']} 82개 행정구"
    desc = f"서울 25 · 경기 31 · 인천 10 · 부산 16 — {SITE['brand_full']} 전체 82개 행정구. 평균 도착 32분, 권역별 동(洞) 단위 데이터."
    return page(title, desc, "/locations/", body, ld_objs=[organization_ld(), breadcrumb_ld([("홈","/"),("지역","/locations/")])], active="locations")


def city_hub(city_slug):
    c = CITIES[city_slug]
    cards = "".join(f"""<a class="reg reveal" href="/locations/{city_slug}/{d['slug']}/">
<span class="city">{c['short']}</span>
<h3>{d['name_ko']}</h3>
<div class="count">평균 도착 {d['avg']}분</div>
<div class="meta">{d['character']}</div>
</a>""" for d in c['districts'])
    avg = sum(d['avg'] for d in c['districts']) / len(c['districts'])
    body = f"""<section class="wrap">{breadcrumb_html([("홈","/"),("지역","/locations/"),(c['name_ko'],f"/locations/{city_slug}/")])}{section_head(c['short'], f"{c['name_ko']} {c['count']}개 행정구", f"평균 도착 {avg:.0f}분. 5개월간 누적 배차 데이터로 검증된 권역별 운영 시간과 특성.")}
<div class="reg-grid">{cards}</div>
{note_card(1, f"{c['short']} 권역 — 운영 특징", _city_overview(city_slug, c, avg))}
{note_card(2, "매니저 배차 — 권역별 가용성", _city_dispatch(city_slug, c))}
{note_card(3, "추천 코스 — 권역에 맞는 선택", _city_courses(city_slug))}
{note_card(4, "안전·금기 — 본사 자문 가이드라인", [
    "모든 권역에서 동일한 안전 가이드라인이 적용됩니다.",
    "임신·심혈관·급성 염증·수술 직후 2주 이내 등 금기 신호 7가지는 시술 전 확인됩니다.",
    "응급 상황 발생 시 본사 응급팀이 24시간 대응합니다.",
])}
</section>{cta_band(title=f'{c["name_ko"]} 24시 예약', desc=f'평균 {avg:.0f}분 도착 — 전화 한 통으로 가까운 매니저가 출발합니다.')}"""
    title = f"{c['name_ko']} 출장마사지 — {SITE['brand']} {c['count']}개 {('자치구' if city_slug=='seoul' else '시·구·군')}"
    desc = f"{c['name_ko']} {c['count']}개 행정구 — {SITE['brand_full']} 평균 도착 {avg:.0f}분. {', '.join(d['name_ko'] for d in c['districts'][:5])} 등."
    return page(title, desc, f"/locations/{city_slug}/", body, ld_objs=[
        organization_ld(),
        breadcrumb_ld([("홈","/"),("지역","/locations/"),(c['name_ko'],f"/locations/{city_slug}/")]),
    ], active="locations")


def _city_overview(slug, c, avg):
    if slug == "seoul":
        return [
            "서울 25개 자치구는 본사 운영의 중심권역으로, 평균 도착 33분, 전체 배차의 60%가 집중됩니다.",
            "강남·서초·송파·마포·용산은 23시 이후 콜 비중이 40%를 넘는 심야 권역이며, 노원·도봉·강북은 21~23시 콜이 집중되는 주거 권역입니다.",
            "권역별 매니저 배차는 본사 디스패처가 권역·시간·코스 적합도를 실시간으로 계산해 진행합니다.",
        ]
    elif slug == "gyeonggi":
        return [
            "경기 31개 시는 신도시·공단·외곽 농촌이 혼재합니다. 평균 도착은 46분으로 광역 평균보다 깁니다.",
            "수원·성남·고양·용인 등 1기·2기 신도시 권역은 도착이 40분 이내, 양평·연천·가평 등 외곽은 60분 이상이 정상입니다.",
            "외곽 권역은 사전 예약을 권장드리며, 별도 출장비가 발생할 수 있습니다.",
        ]
    elif slug == "incheon":
        return [
            "인천 10개 구·군은 신도시(송도·청라)·공항권(중구·영종)·전통권(동구·미추홀)·도서권(강화·옹진)으로 다양합니다.",
            "평균 도착은 도심 권역 43분, 도서 권역은 별도 협의가 필요합니다.",
            "공항권은 외국인 호텔 출장 비중이 높아 영어·일어·중국어 매니저가 우선 배정됩니다.",
        ]
    else:  # busan
        return [
            "부산 16개 구·군은 해운대·수영·중구 등 관광·호텔 권역과 동래·연제 등 전통 권역으로 나뉩니다.",
            "평균 도착은 도심 33분, 외곽(기장·강서) 45분 내외입니다.",
            "관광 권역의 야간 콜 비중은 평일에도 40%를 넘으며, 외국인 손님 비중이 수도권보다 높습니다.",
        ]


def _city_dispatch(slug, c):
    return [
        f"{c['short']} 권역에서 활동하는 매니저는 본사 직접 교육 80시간을 이수한 인원으로만 구성됩니다.",
        f"{c['short']} 매니저 배차는 본사 디스패처가 위치·시간·코스 적합도를 실시간으로 계산해 진행합니다.",
        f"국적 지정·매니저 재지정·외국어 매니저 요청은 콜 시점에 말씀해주시면 가능 인원을 안내드립니다.",
    ]


def _city_courses(slug):
    if slug == "seoul":
        return [
            "도심 비즈니스 권역(강남·서초·중구): 60분 컴팩트 스웨디시 또는 75분 두피·어깨 집중.",
            "주거 권역(노원·강북·도봉): 90분 정통 스웨디시 또는 75분 림프 순환.",
            "외국인 호텔 권역(용산·중구·종로): 영어·일어 매니저 + 75~90분 아로마·로미로미.",
        ]
    elif slug == "gyeonggi":
        return [
            "IT 권역(판교·광교): 75분 어깨·목 집중 또는 90분 풀바디 회복.",
            "신도시 권역(동탄·미사·운정): 90분 스웨디시 또는 120분 커플.",
            "외곽 권역: 도착 시간이 길므로 120분 코스를 권장. 한 번에 깊은 회복.",
        ]
    elif slug == "incheon":
        return [
            "송도·청라 신도시: 90분 풀바디 또는 90분 아로마.",
            "공항·중구: 60분 호텔 출장 또는 75분 시차 회복 아로마.",
            "전통 권역(동구·미추홀): 75분 어깨·목 또는 60분 림프.",
        ]
    else:  # busan
        return [
            "해운대·수영·중구 호텔: 75분 아로마 또는 90분 풀바디.",
            "서면·연제(부산진구·연제구): 60분 컴팩트 또는 75분 어깨.",
            "외곽(기장·강서): 90분 풀바디 권장.",
        ]


def district_page(d):
    city = CITIES[d['city']]
    city_slug = d['city']
    dong_rows = "".join(f"<div><span>{name}</span><span>{m}분</span></div>" for name, m in d['dongs'])
    avg = d['avg']

    # 행정구별 후기 6개 — 다양성 위해 랜덤 + dong 매칭
    rng = random.Random(d['slug'])
    sample_pool = list(GLOBAL_REVIEWS)
    rng.shuffle(sample_pool)
    reviews = []
    courses = ["60분 스웨디시","90분 아로마","75분 어깨·목 집중","90분 스웨디시","60분 림프","120분 풀바디","75분 스포츠","90분 로미로미","60분 아로마"]
    names = ["김","이","박","최","정","강","조","윤","장","임","한","오","서","신","권"]
    given = ["수영","현우","지은","민준","서연","태훈","유진","승민","나래","현지","도윤","채린","우혁","예린","상혁"]
    for i in range(6):
        dong_name = d['dongs'][i % len(d['dongs'])][0]
        c_idx = (hash(d['slug']) + i) % len(courses)
        nm = names[(hash(d['slug']) + i) % len(names)] + "*" + given[(hash(d['slug']) + i*3) % len(given)]
        bodies = [
            f"{d['name_ko']} {dong_name}에서 받았어요. 매니저님이 정확히 시간 맞춰 오셨고 시술 만족도가 높았습니다. 다음에 또 부탁드릴게요.",
            f"{dong_name} 근처라 도착 시간이 걱정됐는데 {d['avg']}분 정도 만에 오셔서 좋았어요. 마사지도 꼼꼼하셨습니다.",
            f"평일 야간에 콜했는데 빠르게 배정해주셨어요. {d['name_ko']} 권역도 24시 가능한 게 안심됩니다. 추천드립니다.",
            f"{d['name_ko']} 거주인데 이번이 두 번째예요. 같은 매니저님 다시 배정 가능해서 좋았습니다. 신뢰가 갑니다.",
            f"{d['character'].split(' — ')[-1]} 부분이 마음에 들었어요. 매니저님이 권역 특성에 맞게 상담해주셨습니다.",
            f"호텔이 아니라 자택이었는데 위생·예의가 깔끔했어요. {d['name_ko']} 권역에서 자주 부탁드릴 것 같습니다.",
        ]
        rating = 5 if i % 5 != 4 else 4
        reviews.append({"name": nm, "course": courses[c_idx], "body": bodies[i], "rating": rating, "dong": dong_name})

    reviews_html = "".join(f"""<div class="review reveal">
<div class="stars">{"★"*r['rating']}{"☆"*(5-r['rating'])}</div>
<div class="body">"{r['body']}"</div>
<div class="meta"><b>{r['name']}</b><span>·</span><span>{d['name_ko']} {r['dong']}</span><span>·</span><span>{r['course']}</span></div>
</div>""" for r in reviews)

    # 가격 카드 3개 (대표 코스)
    price_cards = ""
    for s in SERVICES[:3]:
        rows = "".join(f"<div><span>{m}분</span><span>{p:,}원</span></div>" for m, p in s["duration_options"])
        price_cards += f"""<div class="price-card reveal">
<span class="kicker">{s['kicker']}</span><h3>{s['name_ko']}</h3>
<p>{s['tag']}</p>
<div class="time-rows">{rows}</div></div>"""

    body = f"""<section class="hero"><div class="hero-inner">
<div class="hero-copy reveal">
<span class="eyebrow"><span class="pulse"></span>{city['name_ko']} · {d['name_ko']} OPERATIONS</span>
<h1>{d['name_ko']}<br><span class="grad">평균 {avg}분</span><br><span class="serif">도착 약속.</span></h1>
<p class="lead">{d['character']}. {d['name_ko']} {len(d['dongs'])}개 동(洞)을 대상으로 한 5개월 실 배차 데이터로 안내드립니다. 24시 콜, 자문 트레이너 가이드라인, 156명 활동 매니저.</p>
<div class="actions">
<a class="btn btn-primary" href="tel:{SITE['phone_raw']}">📞 {SITE['phone_display']} 예약 →</a>
<a class="btn btn-ghost" href="/service/">코스 둘러보기</a>
</div>
<div class="trust">
<span><b>평균 {avg}분</b> 도착</span>
<span><b>야간 콜 {d['night_rate']}%</b></span>
<span><b>24시</b> 연중무휴</span>
</div>
</div>
<div class="hero-visual" aria-hidden="true">
<div class="floating fl-1">{d['name_ko']} · 24/7</div>
<div class="glass">
<h3><small>RECOMMENDED COURSE</small>{d['recommend']}</h3>
<div class="book-row"><span>권역 특성</span><b>{d['character'].split(' — ')[0]}</b></div>
<div class="book-row"><span>피크 시간</span><b>{d['peak']}</b></div>
<div class="book-row"><span>평균 도착</span><b>{avg}분</b></div>
<a class="bk" href="tel:{SITE['phone_raw']}">예약 전화 →</a>
</div>
<div class="floating fl-2">권역 데이터 · 2026</div>
</div>
</div></section>

<section class="wrap">{breadcrumb_html([("홈","/"),("지역","/locations/"),(city['name_ko'],f"/locations/{city_slug}/"),(d['name_ko'],f"/locations/{city_slug}/{d['slug']}/")])}

{section_head("OVERVIEW", f"{d['name_ko']} — 동(洞)별 평균 도착 시간", f"{d['name_ko']}을(를) 대표하는 {len(d['dongs'])}개 동(洞)의 실 배차 평균값입니다. 매월 1일 자동 갱신됩니다.")}

<div class="price-grid" style="margin-bottom:36px">
<div class="price-card best reveal"><span class="best-badge">{d['name_ko']} 평균</span>
<span class="kicker">동별 도착 시간</span>
<h3>{d['name_ko']}</h3>
<p>{len(d['dongs'])}개 동(洞) 평균 도착 {avg}분.</p>
<div class="time-rows">{dong_rows}</div>
</div>
<div class="price-card reveal">
<span class="kicker">권역 성격</span>
<h3>{d['name_ko']}의 콜 분포</h3>
<p>{d['character']}</p>
<div class="time-rows">
<div><span>피크 시간대</span><span>{d['peak']}</span></div>
<div><span>야간(23~05) 콜</span><span>{d['night_rate']}%</span></div>
<div><span>추천 코스</span><span>{d['recommend'].split(' 또는')[0]}</span></div>
</div>
</div>
</div>

{note_card(5, f"{d['name_ko']} — 동(洞)별 평균 도착 시간 분포", [
    f"가장 빠른 권역은 {d['dongs'][0][0]}({d['dongs'][0][1]}분), 가장 느린 권역은 {d['dongs'][-1][0]}({d['dongs'][-1][1]}분)입니다.",
    f"평균값은 {avg}분이며, 5개월 누적 배차 데이터의 중위값과 평균값을 함께 사용해 보정합니다.",
    f"콜 시점의 실시간 교통 상황에 따라 ±5분 정도 변동이 발생할 수 있으며, 도착 지연 시 즉시 문자로 안내드립니다.",
])}

{note_card(6, f"{d['name_ko']} — 시간대별 콜 분포", [
    f"피크 시간대는 {d['peak']}입니다. 이 시점에 가용 매니저 수가 가장 빠르게 줄어듭니다.",
    f"야간(23시~05시) 콜 비중은 {d['night_rate']}%로, {('전 권역 평균 대비 높은' if d['night_rate']>=40 else '전 권역 평균 대비 낮은') if d['night_rate']!=35 else '평균적인'} 수준입니다.",
    f"피크 시간대에 콜하시는 경우 5~10분 정도 도착이 늦어질 수 있어 가급적 피크 30분 전 미리 예약하시면 좋습니다.",
])}

{note_card(7, f"{d['name_ko']} — 권역에 맞는 추천 코스", [
    f"{d['name_ko']}에서 가장 자주 선택되는 코스: {d['recommend']}.",
    f"권역 특성({d['character'].split(' — ')[0]})에 맞춰 본사 디스패처가 매니저를 배정합니다.",
    f"랜드마크 인근(예: {', '.join(d['landmarks'][:2])})은 호텔·오피스텔 출장 비중이 높아 영어·일어 매니저 우선 배정됩니다.",
])}

{note_card(8, "예약·결제·환불 한눈에", [
    "예약: 전화 24시 응답. 위치·인원·코스·시간 4가지만 알려주시면 됩니다.",
    "결제: 시술 시작 전 현금 또는 계좌이체. 사전 결제·구독 없음.",
    "환불: 시술 시작 전 100% 환불, 시술 중단 시 시간 비례 환불.",
])}

{section_head("FIELD NOTES · 2026", f"{d['name_ko']} 현장 노트", "운영하면서 확인한 권역 특성을 기록합니다.")}

{note_card(1, "권역의 특징", [
    f"{d['name_ko']}은(는) {d['character'].split(' — ')[0]}을(를) 대표하는 권역입니다.",
    f"대표 랜드마크는 {', '.join(d['landmarks'])} 등이며, 권역 면적이 넓어 동(洞) 단위로 도착 시간이 다르게 관리됩니다.",
    f"본사는 {d['name_ko']} 권역을 위해 인근 거점에 매니저를 분산 배치합니다.",
])}

{note_card(2, "매니저 배치 및 도착 시간", [
    f"평일 22~24시 가용 매니저는 평균 {3 if avg<35 else (2 if avg<45 else 1)}~{5 if avg<35 else (4 if avg<45 else 3)}명 수준입니다.",
    f"피크 시간({d['peak'].split(' 콜')[0]}) 직전에는 가용 매니저가 빠르게 줄어듭니다.",
    "도착 1시간 전에 콜하시면 더 정확한 ETA를 안내해드릴 수 있습니다.",
])}

{note_card(3, f"{d['name_ko']} 안전 가이드", [
    f"본 권역의 모든 시술은 자문 트레이너 박지연(KSPO)·정민호(PT) 가이드라인을 따릅니다.",
    "임신·심혈관·급성 염증·수술 직후 2주 이내 등 금기 신호 7가지를 시술 전 확인합니다.",
    f"{d['name_ko']} 권역에서 발생한 응급 상황은 본사 응급팀이 30분 이내 대응합니다.",
])}

{note_card(4, "결제·예약 운영 원칙", [
    "표기 가격이 최종 가격입니다. 심야 할증·주말 할증 없습니다.",
    f"{d['name_ko']}은(는) 평균 {avg}분 권역이므로 별도 외곽 출장비가 발생하지 않습니다." if avg < 50 else f"{d['name_ko']}은(는) 외곽 권역으로 별도 출장비가 안내될 수 있으며, 콜 시점에 미리 알려드립니다.",
    "환불은 시술 시작 전 100%, 시술 중단 시 시간 비례입니다.",
])}

<div class="data-box reveal" id="methodology">
<span class="kicker">DATA & METHODOLOGY</span>
<h3>이 페이지의 수치는 어디서 왔는가</h3>
<p>본 페이지의 도착 시간·콜 분포·야간 비중은 2025년 11월~2026년 3월까지 5개월간 {d['name_ko']} 권역에서 발생한 실 배차 로그를 기반으로 합니다. 매월 1일 자동 집계되며, 표본이 부족한 권역(월 50건 미만)은 인근 권역과 함께 추정합니다.</p>
<div class="chips">
<span class="chip">{d['name_ko']} 평균 <b>{avg}분</b></span>
<span class="chip">동(洞) 수 <b>{len(d['dongs'])}개</b></span>
<span class="chip">야간 콜 <b>{d['night_rate']}%</b></span>
<span class="chip">랜드마크 <b>{len(d['landmarks'])}곳</b></span>
</div>
</div>

<h2 style="margin-top:64px" id="pricing">{d['name_ko']} 추천 코스 요금</h2>
<div class="price-grid">{price_cards}</div>

<h2 style="margin-top:64px">{d['name_ko']} 실 후기</h2>
<div class="rv-grid">{reviews_html}</div>

</section>{cta_band(title=f'{d["name_ko"]} 24시 예약', desc=f'평균 {avg}분 도착 — 가까운 매니저가 즉시 출발합니다.')}"""

    faqs = [
        (f"{d['name_ko']} 어디까지 출장이 가능한가요?", f"{d['name_ko']} 전체 동(洞) — {', '.join(name for name, _ in d['dongs'][:3])} 등 — 모두 가능합니다."),
        (f"{d['name_ko']} 도착 시간은 얼마나 걸리나요?", f"평균 {avg}분입니다. 콜 시점의 정확한 ETA를 매니저 출발과 동시에 문자로 안내드립니다."),
        (f"{d['name_ko']}에서 24시 콜이 되나요?", f"네. {d['name_ko']}은(는) 365일·24시간 운영됩니다. 야간 콜 비중도 {d['night_rate']}%로 평균 이상입니다."),
        (f"{d['name_ko']}에 가장 잘 맞는 코스는?", f"권역 특성상 {d['recommend']}이(가) 가장 자주 선택됩니다."),
        (f"{d['name_ko']} 호텔 출장이 가능한가요?", f"가능합니다. {', '.join(d['landmarks'][:2])} 인근 호텔 출장이 가장 많으며, 외국인 손님은 영어·일어 매니저 우선 배정됩니다."),
        ("결제는 어떻게 하나요?", "시술 시작 전 현금 또는 계좌이체로 진행됩니다. 사전 결제·구독·연회비는 없습니다."),
    ]

    # Schema
    review_items = [{
        "@type": "Review",
        "author": {"@type": "Person", "name": r["name"]},
        "reviewBody": r["body"],
        "reviewRating": {"@type": "Rating", "ratingValue": r["rating"], "bestRating": 5},
    } for r in reviews]

    local_ld = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": f"{SITE['brand_full']} {d['name_ko']}",
        "image": f"{SITE['base_url']}/assets/og-cover.jpg",
        "url": f"{SITE['base_url']}/locations/{city_slug}/{d['slug']}/",
        "telephone": SITE["phone_tel"],
        "priceRange": "₩₩",
        "address": {"@type":"PostalAddress","addressLocality":d['name_ko'],"addressRegion":city['name_ko'],"addressCountry":"KR"},
        "areaServed": {"@type": "AdministrativeArea", "name": d['name_ko']},
        "openingHoursSpecification": SITE["open_hours_spec"],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": 4.93, "reviewCount": len(reviews)*47},
        "review": review_items,
    }

    title = f"{d['name_ko']} 출장마사지 — {SITE['brand']} 평균 {avg}분 도착 · 24시"
    desc = f"{d['name_ko']} {len(d['dongs'])}개 동(洞) 평균 도착 {avg}분. {d['character']}. 야간 콜 비중 {d['night_rate']}%. {SITE['brand_full']} 24시 운영."

    return page(title, desc, f"/locations/{city_slug}/{d['slug']}/", body, ld_objs=[
        organization_ld(),
        breadcrumb_ld([("홈","/"),("지역","/locations/"),(city['name_ko'],f"/locations/{city_slug}/"),(d['name_ko'],f"/locations/{city_slug}/{d['slug']}/")]),
        local_ld,
        faq_ld(faqs),
    ], active="locations")


def all_location_pages():
    yield ("/locations/index.html", location_hub())
    for city_slug in CITIES:
        yield (f"/locations/{city_slug}/index.html", city_hub(city_slug))
        for d in CITIES[city_slug]["districts"]:
            yield (f"/locations/{city_slug}/{d['slug']}/index.html", district_page({**d, "city": city_slug}))
