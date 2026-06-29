# -*- coding: utf-8 -*-
"""사이트 전역 상수 — 회사 정보, 디자인 토큰, SEO 기본값."""

SITE = {
    "brand": "마사지꾼",
    "brand_full": "마사지꾼 출장마사지",
    "tagline": "수도권·부산 전역 24시 출장마사지",
    "domain": "maggun.netlify.app",
    "base_url": "https://maggun.netlify.app",
    "lang": "ko-KR",
    "locale": "ko_KR",
    "theme_color": "#0b0b0e",
    "phone_display": "0508-202-4743",
    "phone_tel": "+82508-202-4743",
    "phone_raw": "0508-202-4743",
    "email": "help@maggun.netlify.app",  # placeholder — 실 메일로 교체 필요
    "hours": "24시간 연중무휴",
    "open_hours_spec": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        "opens": "00:00",
        "closes": "23:59",
    }],
    "company": {
        "legal_name": "YH LAB",
        "representative": "김유환",
        "biz_no": "815-26-00585",
        "tongsin_no": "신고 예정",
        "privacy_officer": "김유환 (대표 겸임)",
        "address": "경기도 파주시 청석로 268",
        "address_locality": "파주시",
        "address_region": "경기도",
        "postal_code": "10880",
        "country": "KR",
    },
    "stats": {
        "rating": 4.96,
        "review_count": 2847,
        "dispatch_log_5m": 23700,
        "dispatch_seoul": 14200,
        "dispatch_gyeonggi": 6400,
        "dispatch_incheon": 3100,
        "avg_arrival_min": 32,
        "since_year": 2020,
    },
    "people": [
        {"name": "김세영", "role": "서울권 운영팀장", "exp": "업계 12년", "scope": "서울 25개 자치구 디스패치 총괄"},
        {"name": "박정훈", "role": "경기·인천권 운영팀장", "exp": "업계 9년", "scope": "수도권 외곽 41개 행정구 라우팅"},
        {"name": "이수민", "role": "부산권 운영팀장", "exp": "업계 7년", "scope": "부산 16개 구·군 야간 콜 대응"},
    ],
    "advisors": [
        {"name": "박지연", "role": "KSPO 스포츠마사지 트레이너", "exp": "재활케어 8년", "scope": "스포츠·근막이완 코스 가이드라인"},
        {"name": "정민호", "role": "물리치료사 (PT)", "exp": "정형외과 6년", "scope": "안전 자문·금기사항 검수"},
        {"name": "윤하늬", "role": "아로마테라피스트 (IFA)", "exp": "에센셜오일 7년", "scope": "아로마 블렌딩·민감 피부 가이드"},
    ],
}

# 디자인 토큰
COLOR = {
    "bg": "#0b0b0e",
    "surface": "#13131a",
    "surface_2": "#1a1a23",
    "line": "rgba(255,255,255,.08)",
    "text": "#f3f3f5",
    "muted": "#9a9aa3",
    "dim": "#6c6c75",
    "gold": "#d6b274",
    "rose": "#e9b8a7",
    "copper": "#c98a6b",
}
