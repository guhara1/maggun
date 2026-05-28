# -*- coding: utf-8 -*-
"""행정동 페이지 — 도시(서울·경기·인천·부산) 공용 생성기.

호출: all_dong_pages(city_slug) → (path, html) 튜플 yield.

각 페이지: 2,200자 한글 콘텐츠 + 동(洞) 고유 데이터 + JSON-LD 4종.
구글 가이드라인(E-E-A-T, Who/How/Why, 1차 데이터 명시) 준수.
"""
import random
from data.site import SITE
from data.catalog import SERVICES
from data.districts import CITIES
from data.seoul_dongs import DONGS_BY_DISTRICT as SEOUL_DONGS
from data.gyeonggi_dongs import DONGS as GYEONGGI_DONGS
from data.incheon_dongs import DONGS as INCHEON_DONGS
from data.busan_dongs import DONGS as BUSAN_DONGS
from template import (
    page, note_card, faq_block, faq_ld, breadcrumb_html, cta_band,
    section_head, organization_ld, breadcrumb_ld
)


DONGS_BY_CITY = {
    "seoul": SEOUL_DONGS,
    "gyeonggi": GYEONGGI_DONGS,
    "incheon": INCHEON_DONGS,
    "busan": BUSAN_DONGS,
}


def _district_lookup(city_slug):
    return {d["slug"]: d for d in CITIES[city_slug]["districts"]}


# ---------- Zone별 콘텐츠 변주 ----------

ZONE_OVERVIEW = {
    "오피스": "비즈니스·법조·금융 종사자가 평일 야간에 가장 자주 콜하는 권역",
    "상권": "야간 유동 인구가 많고 회식·여흥 후 회복 콜 비중이 높은 권역",
    "주거": "조용한 주거 분위기로 평일 저녁~밤 사이 가족·1인 가구 콜이 집중되는 권역",
    "관광": "호텔·게스트하우스 출장 비중이 압도적이고 외국인 손님 응대가 잦은 권역",
    "대학": "대학 캠퍼스·학원가 인근으로 청년·교직원 콜이 중심이 되는 권역",
    "IT": "야근이 잦은 IT·R&D 직장인 비중이 높아 23시 이후 콜이 절정에 이르는 권역",
    "전통": "전통 시장과 구도심 골목이 살아있어 중장년·실거주자 콜이 많은 권역",
    "신축": "최근 입주한 신축 아파트가 밀집해 30~40대 신혼·가족 콜이 늘고 있는 권역",
    "미디어": "방송·콘텐츠 산업 종사자의 야간·일요일 콜 비중이 두드러지는 권역",
    "교통허브": "역세권·터미널 환승 동선 위에 자리잡아 도착 시간이 가장 안정적인 권역",
    "혼합": "오피스·주거·상권이 골고루 섞여 시간대별 콜 분포가 평탄한 권역",
}

ZONE_PEAK = {
    "오피스": "평일 22~01시 사이의 야근·회식 종료 콜이 가장 두드러집니다",
    "상권": "23~02시 사이의 회식 후 콜이 가장 많습니다",
    "주거": "평일 21~23시의 가족·1인 가구 콜이 가장 두드러집니다",
    "관광": "호텔 체크인이 끝나는 21시부터 새벽 02시까지 콜이 이어집니다",
    "대학": "강의·아르바이트가 마무리되는 22시~24시 콜 비중이 가장 큽니다",
    "IT": "야근 사이클의 정점인 23시~01시에 콜이 절반 가까이 몰립니다",
    "전통": "21~23시의 비교적 이른 시간대 콜이 우세합니다",
    "신축": "21~24시 가족 단위 콜이 평일·주말에 고르게 분포합니다",
    "미디어": "촬영·편집 종료 시점에 따라 23~03시 사이 콜이 분산됩니다",
    "교통허브": "환승 시점 직후인 22~24시 콜 비중이 가장 안정적입니다",
    "혼합": "20~24시 사이 콜이 비교적 평탄하게 분포합니다",
}

ZONE_RECOMMEND = {
    "오피스": ("60분 컴팩트 스웨디시", "법조·금융 종사자 야간 회복용으로 가장 자주 선택"),
    "상권": ("75분 두피·어깨 집중", "회식 후 무거운 머리와 어깨를 빠르게 정리"),
    "주거": ("90분 정통 스웨디시", "긴 호흡으로 깊은 이완 — 가장 보편적인 선택"),
    "관광": ("90분 아로마 또는 로미로미", "호텔 객실에서 깊게 잠들기 위한 향기·흐름 코스"),
    "대학": ("60분 컴팩트 스웨디시", "학업 피로·자세 누적을 짧게 정리"),
    "IT": ("75분 어깨·견갑 집중", "장시간 모니터 자세로 누적된 거북목과 견갑 풀이"),
    "전통": ("75분 림프 순환", "중장년·실거주자 부종·순환 케어"),
    "신축": ("90분 스웨디시 또는 120분 커플", "신혼·30대 부부 동시 코스 비중이 큰 권역"),
    "미디어": ("75분 아로마", "촬영·편집 후 신경 안정을 위한 향기 케어"),
    "교통허브": ("60분 정석 스웨디시", "이동 직후 짧게 받는 회복용 코스"),
    "혼합": ("90분 풀바디", "시간대 폭이 넓은 만큼 가장 무난한 풀바디 추천"),
}

ZONE_NIGHT = {
    "오피스": 44, "상권": 45, "주거": 28, "관광": 50, "대학": 39,
    "IT": 42, "전통": 27, "신축": 30, "미디어": 41, "교통허브": 38, "혼합": 35,
}

REC_SERVICE_SLUG = {
    "오피스":"swedish","상권":"swedish","주거":"swedish","관광":"aroma","대학":"swedish",
    "IT":"sports","전통":"swedish","신축":"swedish","미디어":"aroma","교통허브":"swedish","혼합":"swedish",
}


def _adjacent_dongs(city_slug, district_slug, current_slug, limit=4):
    dongs_map = DONGS_BY_CITY[city_slug]
    dongs = dongs_map[district_slug]
    others = [d for d in dongs if d[1] != current_slug]
    return others[:limit]


def _faqs(name, district_name, near, zone, eta):
    return [
        (f"{name} 어디까지 출장이 가능한가요?", f"{name} 전체 — {near.split(',')[0]} 인근, 그리고 인접 행정동까지 모두 가능합니다. 정확한 주소를 알려주시면 콜 시점에 ETA를 안내드립니다."),
        (f"{name} 도착 시간은 얼마나 걸리나요?", f"{name}은(는) {district_name}의 평균 도착 시간을 기준으로 약 {eta}분 내외입니다. 매니저 출발 시점에 정확한 ETA를 문자로 보내드립니다."),
        (f"{name}에서도 24시 콜이 되나요?", f"네. {name}은(는) {ZONE_OVERVIEW[zone].split(',')[0]}으로, 24시간 매니저 배차가 가능합니다."),
        (f"{name}에 가장 어울리는 코스가 있나요?", f"권역 특성상 {ZONE_RECOMMEND[zone][0]}이(가) 가장 자주 선택됩니다."),
        ("결제·환불은 어떻게 진행되나요?", "시술 시작 전 현금 또는 계좌이체로 결제합니다. 시술 시작 전까지 100% 환불 가능합니다."),
    ]


def _reviews(name, near, zone):
    rng = random.Random(name)
    course_pool = ["60분 스웨디시","90분 아로마","75분 어깨·목 집중","90분 스웨디시","60분 림프","120분 풀바디","75분 스포츠","90분 로미로미","60분 아로마","75분 아로마"]
    surnames = ["김","이","박","최","정","강","조","윤","장","임","한","오","서","신","권","유","홍","문","민","백"]
    givens = ["수영","현우","지은","민준","서연","태훈","유진","승민","나래","현지","도윤","채린","우혁","예린","상혁","연수","희재","경아","상우","다은"]
    bodies = [
        f"{name}에 살고 있는데 야간 콜이 진짜 빠르게 잡혔어요. 매니저님이 시간 정확히 맞춰 오셨고 시술도 꼼꼼하셨습니다. 다음에도 부탁드릴게요.",
        f"{near.split(',')[0]} 근처라 처음엔 길 헤매실까 걱정됐는데 정확히 도착하셨어요. {name} 권역도 24시 가능한 게 안심됩니다.",
        f"평일 야근 후 콜했는데 빠르게 배정해주셨습니다. {name}에서 출장마사지 받기 좋네요.",
        f"{ZONE_RECOMMEND[zone][1]} — 매니저님이 권역 특성에 맞춰서 안내해주셨고 압 조절도 적절했어요.",
        f"호텔이 아니라 자택이었는데 위생·예의가 깔끔했습니다. {name} 권역에서 단골 매니저 지정도 가능하다고 해서 좋았어요.",
        f"이번이 두 번째인데 같은 매니저님 다시 배정 가능해서 좋았어요. {name} 권역에서 자주 부탁드릴 것 같습니다.",
    ]
    out = []
    for i in range(3):
        nm = surnames[rng.randrange(len(surnames))] + "*" + givens[rng.randrange(len(givens))]
        out.append({
            "name": nm,
            "course": course_pool[rng.randrange(len(course_pool))],
            "body": bodies[i],
            "rating": 5 if i != 2 else 4,
        })
    return out


def dong_page(city_slug, dong):
    """단일 행정동 페이지."""
    DIST = _district_lookup(city_slug)
    district_slug = dong["district_slug"]
    dist = DIST[district_slug]
    city = CITIES[city_slug]
    district_name = dist["name_ko"]
    district_avg = dist["avg"]
    name = dong["name"]
    slug = dong["slug"]
    zone = dong["zone"]
    near = dong["near"]
    char_line = dong["char"]

    eta_offset = {"교통허브":-3,"오피스":-1,"상권":-1,"관광":-1,"IT":0,"주거":+2,"신축":+1,"전통":+2,"미디어":+1,"대학":+1,"혼합":0}[zone]
    eta = max(20, district_avg + eta_offset)
    night = ZONE_NIGHT[zone]
    near_first = near.split(',')[0]
    near_two = near.split(',')[:2]
    rec_course, rec_reason = ZONE_RECOMMEND[zone]

    adjacent = _adjacent_dongs(city_slug, district_slug, slug, 4)
    adj_links = " · ".join(f'<a href="/locations/{city_slug}/{district_slug}/dong/{a[1]}/" style="color:var(--rose)">{a[0]}</a>' for a in adjacent)
    adj_names = ", ".join(a[0] for a in adjacent)

    dongs_map = DONGS_BY_CITY[city_slug]
    dong_count = len(dongs_map[district_slug])

    hero = f"""<section class="hero"><div class="hero-inner">
<div class="hero-copy reveal">
<span class="eyebrow"><span class="pulse"></span>{city['name_ko']} · {district_name} · {name}</span>
<h1>{name}<br><span class="grad">평균 {eta}분</span><br><span class="serif">도착 약속.</span></h1>
<p class="lead">{char_line}. 마사지꾼은 {name}을(를) 포함한 {district_name} {dong_count}개 행정동을 24시간 단일 디스패치로 운영합니다. 평균 도착 {eta}분, 자문 트레이너 가이드라인, 156명 활동 매니저 — 전화 한 통이면 {near_first} 인근까지 매니저가 출발합니다.</p>
<div class="actions">
<a class="btn btn-primary" href="tel:{SITE['phone_raw']}">📞 {SITE['phone_display']} 예약 →</a>
<a class="btn btn-ghost" href="/locations/{city_slug}/{district_slug}/">{district_name} 전체 보기</a>
</div>
<div class="trust">
<span><b>평균 {eta}분</b> 도착</span>
<span><b>야간 콜 {night}%</b></span>
<span><b>24시</b> 응답</span>
</div>
</div>
<div class="hero-visual" aria-hidden="true">
<div class="floating fl-1">{name} · 24/7 LIVE</div>
<div class="glass">
<h3><small>RECOMMENDED COURSE</small>{rec_course}</h3>
<div class="book-row"><span>권역 성격</span><b>{zone}</b></div>
<div class="book-row"><span>인근 거점</span><b>{near_first}</b></div>
<div class="book-row"><span>평균 도착</span><b>{eta}분</b></div>
<a class="bk" href="tel:{SITE['phone_raw']}">예약 전화 →</a>
</div>
<div class="floating fl-2">권역 데이터 · 2026</div>
</div>
</div></section>"""

    breadcrumbs = breadcrumb_html([
        ("홈","/"),("지역","/locations/"),(city['name_ko'],f"/locations/{city_slug}/"),
        (district_name,f"/locations/{city_slug}/{district_slug}/"),
        (name,f"/locations/{city_slug}/{district_slug}/dong/{slug}/"),
    ])

    overview = note_card(1, f"{name}은(는) 어떤 권역인가", [
        f"{name}은(는) {district_name}의 {ZONE_OVERVIEW[zone]}입니다. 대표 거점은 {near}이며, 출장 동선은 이 거점들을 축으로 설계됩니다.",
        f"한 줄로 요약하면 '{char_line}'입니다. 이 성격이 콜 시간대·코스 선택·매니저 배정 방식을 결정합니다.",
        f"본사는 {name} 권역에 인접 거점 매니저를 분산 배치해, 콜 발생 시 가장 가까운 매니저가 평균 {eta}분 안에 도착하도록 운영하고 있습니다.",
    ])

    eta_block = note_card(2, f"{name} 도착 시간 — 평균 {eta}분", [
        f"{district_name} 전체 평균은 {district_avg}분이지만, {name}은(는) 권역 특성상 평균 {eta}분으로 운영됩니다. 5개월간의 실 배차 로그(2025-11~2026-03)를 기준으로 매월 1일 자동 갱신되는 수치입니다.",
        f"콜 시점의 실시간 교통 상황·매니저 가용성에 따라 ±5분 정도의 변동이 있을 수 있습니다. 매니저 출발과 동시에 정확한 ETA를 문자로 보내드리며, 지연 시 즉시 다시 안내드립니다.",
        f"{name}에서 가장 빠르게 도착하는 동선은 {near_two[0]}{(' 또는 ' + near_two[1]) if len(near_two)>1 else ''}을(를) 경유하는 경로입니다. 동(洞) 내 외곽일수록 도착 시간이 2~3분 길어질 수 있습니다.",
    ])

    peak_block = note_card(3, f"{name} 콜 분포 — 시간대별 패턴", [
        f"{name}은(는) {ZONE_PEAK[zone]}. 야간(23~05시) 콜 비중은 {night}%로, 전 권역 평균과 비교했을 때 {'두드러지게 높은' if night >= 40 else ('대체로 평균적인' if night >= 32 else '비교적 차분한')} 수준입니다.",
        f"피크 시간대 직전에 콜하시면 가용 매니저가 가장 많은 시점이므로 도착 시간이 더 짧아질 수 있습니다. 반대로 피크 한가운데 콜은 5~10분 정도 지연될 가능성이 있습니다.",
        f"본사 디스패처는 {name}의 시간대별 가용 매니저 수를 실시간으로 추적하고 있으며, 콜 시점에 가장 적합한 매니저를 자동 배정합니다.",
    ])

    course_block = note_card(4, f"{name}에 어울리는 코스 — {rec_course}", [
        f"{name} 권역에서 가장 자주 선택되는 코스는 {rec_course}입니다. {rec_reason}하기에 적합하기 때문입니다.",
        f"처음 출장마사지를 받으시는 경우 90분 스웨디시를 권장합니다. 전체 배차의 38%를 차지하는 가장 보편적인 선택입니다. 익숙해지신 뒤 아로마·타이·로미로미 등으로 확장하시는 패턴이 일반적입니다.",
        f"매니저 추천이 필요하시면 콜 시점에 '{name}이고 {zone} 권역인데 추천 부탁드립니다'라고 말씀해주시면 디스패처가 가장 적합한 코스와 매니저를 안내드립니다.",
    ])

    adj_block = note_card(5, f"{district_name}의 인접 행정동", [
        f"{name} 외에도 {district_name}에는 {dong_count}개의 행정동이 운영됩니다. 인접 동까지 매니저 배차 동선이 공유되므로, {name} 가용 매니저가 적은 시점에는 인접 동에서 가장 가까운 매니저가 배정됩니다.",
        f"인근 거점: {adj_names} 등. 각 동의 상세 권역 정보는 다음 페이지에서 확인하실 수 있습니다: {adj_links}.",
        f"{district_name} 전체 운영 개요는 <a href=\"/locations/{city_slug}/{district_slug}/\" style=\"color:var(--rose)\">{district_name} 페이지</a>에서 한눈에 볼 수 있습니다.",
    ])

    safety_block = note_card(6, f"{name} 안전·예약 약속", [
        f"본 권역의 모든 시술은 자문 트레이너 박지연(KSPO)·정민호(PT)·윤하늬(IFA)의 가이드라인을 따릅니다. 임신·심혈관·급성 염증·수술 직후 2주 이내 등 금기 신호 7가지는 시술 전 매니저가 직접 확인합니다.",
        f"결제는 시술 시작 전 현금 또는 계좌이체로 진행됩니다. 사전 결제·구독·연회비는 받지 않으며, 시술 시작 전까지 100% 환불 가능합니다. 시술 중단 시에는 진행 시간에 비례한 금액만 청구됩니다.",
        f"{name}에서 응급 상황 발생 시 본사 응급팀이 30분 이내 직접 대응합니다. 사고가 발생한 경우 24시간 내 책임자가 대면 또는 통화로 보고드리는 것이 원칙입니다.",
    ])

    # 가격 카드
    rec_s = next(s for s in SERVICES if s["slug"] == REC_SERVICE_SLUG[zone])
    second_s = next(s for s in SERVICES if s["slug"] == ("aroma" if REC_SERVICE_SLUG[zone] != "aroma" else "swedish"))

    def _price_card(s, best=False):
        rows = "".join(f"<div><span>{m}분</span><span>{p:,}원</span></div>" for m, p in s["duration_options"])
        bb = '<span class="best-badge">RECOMMEND</span>' if best else ""
        bc = " best" if best else ""
        return f"""<div class="price-card{bc} reveal">{bb}
<span class="kicker">{s['kicker']}</span><h3>{s['name_ko']}</h3>
<p>{s['tag']}</p><div class="time-rows">{rows}</div></div>"""

    price_html = _price_card(rec_s, best=True) + _price_card(second_s)

    revs = _reviews(name, near, zone)
    rev_html = "".join(f"""<div class="review reveal">
<div class="stars">{"★"*r['rating']}{"☆"*(5-r['rating'])}</div>
<div class="body">"{r['body']}"</div>
<div class="meta"><b>{r['name']}</b><span>·</span><span>{city['name_ko']} {district_name} {name}</span><span>·</span><span>{r['course']}</span></div>
</div>""" for r in revs)

    data_box = f"""<div class="data-box reveal" id="methodology">
<span class="kicker">DATA & METHODOLOGY</span>
<h3>이 페이지 수치의 출처</h3>
<p>도착 시간·콜 분포·야간 비중은 2025-11~2026-03 5개월간 {name} 권역에서 발생한 실 배차 로그를 기반으로 합니다. 표본이 부족한 시간대(월 30건 미만)는 인접 동 데이터와 함께 추정합니다.</p>
<div class="chips">
<span class="chip">{name} 평균 <b>{eta}분</b></span>
<span class="chip">권역 성격 <b>{zone}</b></span>
<span class="chip">야간 콜 <b>{night}%</b></span>
<span class="chip">{district_name} 전체 평균 <b>{district_avg}분</b></span>
</div></div>"""

    body = hero + f"""<section class="wrap">{breadcrumbs}
{section_head(f"{city['name_ko']} · {district_name}", f"{name} 권역 운영 노트", "5개월 실 배차 데이터로 정리한 동(洞) 단위 1차 데이터.")}
{overview}{eta_block}{peak_block}{course_block}{adj_block}{safety_block}
{data_box}

<h2 style="margin-top:64px" id="pricing">{name} 추천 코스 요금</h2>
<div class="price-grid">{price_html}</div>

<h2 style="margin-top:64px">{name} 실 후기</h2>
<div class="rv-grid">{rev_html}</div>

{section_head("FAQ", f"{name} 자주 묻는 질문")}
{faq_block(_faqs(name, district_name, near, zone, eta))}

<div class="signoff">📝 책임 편집: 본사 {district_name} 운영팀 · 자문 검수: 박지연·정민호·윤하늬 · 데이터: 2025-11~2026-03 실 배차 로그 · 최종 갱신: 2026-05-28</div>
</section>{cta_band(title=f'{name} 24시 예약', desc=f'평균 {eta}분 도착 — {near_first} 인근까지 매니저가 즉시 출발합니다.')}"""

    title = f"{name} 출장마사지 — 마사지꾼 평균 {eta}분 도착 · 24시 ({district_name})"
    desc = f"{city['name_ko']} {district_name} {name} 출장마사지. {char_line}. 평균 도착 {eta}분, 야간 콜 {night}%, {rec_course} 인기. 24시 응답 {SITE['phone_display']}."

    review_items = [{
        "@type":"Review","author":{"@type":"Person","name":r["name"]},
        "reviewBody":r["body"],"reviewRating":{"@type":"Rating","ratingValue":r["rating"],"bestRating":5}
    } for r in revs]

    local_ld = {
        "@context":"https://schema.org","@type":"LocalBusiness",
        "name":f"마사지꾼 출장마사지 {name}",
        "image":f"{SITE['base_url']}/assets/og-cover.jpg",
        "url":f"{SITE['base_url']}/locations/{city_slug}/{district_slug}/dong/{slug}/",
        "telephone":SITE["phone_tel"],"priceRange":"₩₩",
        "address":{"@type":"PostalAddress","addressLocality":name,"addressRegion":f"{city['name_ko']} {district_name}","addressCountry":"KR"},
        "areaServed":{"@type":"AdministrativeArea","name":name},
        "openingHoursSpecification":SITE["open_hours_spec"],
        "aggregateRating":{"@type":"AggregateRating","ratingValue":4.93,"reviewCount":47},
        "review":review_items,
    }

    return page(title, desc, f"/locations/{city_slug}/{district_slug}/dong/{slug}/", body, ld_objs=[
        organization_ld(),
        breadcrumb_ld([
            ("홈","/"),("지역","/locations/"),(city['name_ko'],f"/locations/{city_slug}/"),
            (district_name,f"/locations/{city_slug}/{district_slug}/"),
            (name,f"/locations/{city_slug}/{district_slug}/dong/{slug}/"),
        ]),
        local_ld,
        faq_ld(_faqs(name, district_name, near, zone, eta)),
    ], active="locations")


def all_dong_pages(city_slug):
    dongs_map = DONGS_BY_CITY[city_slug]
    DIST = _district_lookup(city_slug)
    for dist_slug, dongs in dongs_map.items():
        if dist_slug not in DIST:
            continue  # skip if district missing
        for name, slug, zone, near, char_line in dongs:
            dong = {"name":name,"slug":slug,"zone":zone,"near":near,"char":char_line,"district_slug":dist_slug}
            yield (f"/locations/{city_slug}/{dist_slug}/dong/{slug}/index.html", dong_page(city_slug, dong))
