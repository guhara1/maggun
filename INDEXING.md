# 검색엔진 색인 가이드 (maggun.netlify.app)

본 파일은 마사지꾼 사이트가 Google·Naver·Bing 등 주요 검색엔진에 빠르게 색인되도록 설정된 모든 파일과 절차를 정리합니다.

**도메인**: https://maggun.netlify.app

## 생성된 파일

| 파일 | 목적 |
|---|---|
| `sitemap.xml` | 사이트맵 인덱스 (9개 sub-sitemap 포함) |
| `sitemap-main.xml` | 메인·About·정책 등 |
| `sitemap-services.xml` | 서비스 6 페이지 |
| `sitemap-therapists.xml` | 관리사 7 페이지 |
| `sitemap-magazine.xml` | 매거진 4 페이지 |
| `sitemap-locations.xml` | 광역+자치구 86 페이지 |
| `sitemap-dongs-seoul.xml` | 서울 244 행정동 |
| `sitemap-dongs-gyeonggi.xml` | 경기 369 행정동 |
| `sitemap-dongs-incheon.xml` | 인천 83 행정동 |
| `sitemap-dongs-busan.xml` | 부산 108 행정동 |
| `sitemap-news.xml` | Google News 사이트맵 (매거진 3편) |
| `rss.xml` | RSS 2.0 피드 |
| `atom.xml` | Atom 1.0 피드 |
| `robots.txt` | 크롤러 정책 |
| `a8f3c2d9b54e7f1c6d3a8b2e5f9c4d7a.txt` | IndexNow 인증 키 |
| `humans.txt` | 사람 작성 명시 |
| `netlify.toml` | Netlify 빌드·헤더·리다이렉트 설정 |
| `_headers` | 보안·캐시 헤더 |
| `_redirects` | URL 리다이렉트 (trailing slash 정규화) |

## 중요 — 새 도메인에서 재설정 필요

이전 메인에 들어있던 `google-site-verification` / `naver-site-verification` 토큰은 다른 속성에 발급된 것입니다. **새 도메인(maggun.netlify.app)에서는 새 토큰을 발급받아 교체해야 인증됩니다.**

`build/template.py`의 `head()` 함수 내 두 줄을 새 토큰으로 교체 후 `python3 build.py` 재실행:
```python
'<meta name="google-site-verification" content="새_GSC_토큰">\n'
'<meta name="naver-site-verification" content="새_네이버_토큰">\n'
```

## 배포 후 절차

### 1. Netlify 배포 확인
```bash
# 정적 파일을 그대로 Netlify에 푸시 → 자동 배포됨
# Netlify 사이트 설정: maggun.netlify.app
# Publish directory: . (루트)
# Build command: (없음 — 사전 빌드된 정적 파일)
```

### 2. Google Search Console (필수)
1. https://search.google.com/search-console 접속
2. 속성 추가 → URL 접두어 → `https://maggun.netlify.app`
3. 인증 방법: HTML 태그 → 받은 토큰을 `build/template.py`에 삽입 → 재빌드 → 배포 → "확인" 클릭
4. 좌측 메뉴 → Sitemaps → `sitemap.xml` 제출
5. URL 검사 → 핵심 페이지 5~10개 "색인 요청" 클릭

### 3. Naver Search Advisor (필수)
1. https://searchadvisor.naver.com 접속
2. 웹마스터도구 → 사이트 추가 → `https://maggun.netlify.app`
3. 인증 방법: HTML 태그 → 받은 토큰을 `build/template.py`에 삽입 → 재빌드 → 배포 → "확인" 클릭
4. 좌측 메뉴 → 요청 → 사이트맵 제출 → `sitemap.xml`
5. 좌측 메뉴 → 요청 → RSS 제출 → `rss.xml`
6. 좌측 메뉴 → 요청 → 웹페이지 수집 → 핵심 페이지 5~10개 수동 요청

**참고**: Naver는 netlify.app 같은 서브도메인도 등록 가능합니다. 단 자체 도메인 연결(maggun.co.kr 등)이 장기 SEO에는 더 유리합니다.

### 4. Bing Webmaster Tools (IndexNow 자동 연동)
1. https://www.bing.com/webmasters 접속
2. 사이트 추가 → `https://maggun.netlify.app`
3. Google Search Console 가져오기 옵션 사용 가능
4. Sitemap 제출 → `sitemap.xml`

### 5. IndexNow 즉시 색인 (배포할 때마다 실행 권장)
```bash
python3 ping_search_engines.py            # 핵심 30개 페이지 일괄 핑
python3 ping_search_engines.py /magazine/new-article/   # 단일 URL 핑
```

IndexNow 한 번 호출 → Bing·Yandex·Naver Yeti·Seznam 동시 전파.

## 빠른 색인을 위한 핵심 신호 (적용 완료)

| 신호 | 상태 |
|---|---|
| Sitemap index + 분할 sub-sitemap | ✓ 9개 분할 |
| lastmod 날짜 명시 | ✓ 매 URL에 추가 |
| Image sitemap (image:image) | ✓ og-cover 첨부 |
| Google News sitemap | ✓ 매거진 3편 |
| RSS 2.0 + Atom 1.0 | ✓ HTML head에 자동 발견 링크 |
| robots.txt — Yeti·NaverBot·Daum 명시 | ✓ Crawl-delay 0 |
| JSON-LD Organization/LocalBusiness/Article/FAQ | ✓ 모든 페이지 |
| og:image (1200×630) + preferred image | ✓ secure_url/alt/type 추가 |
| IndexNow 키 파일 (32자 hex) | ✓ 루트 배포 |
| 단일 H1 + Breadcrumb + Canonical | ✓ 914 페이지 전부 |
| 모바일 친화 + HTTPS + INP 최적화 | ✓ 인라인 CSS, JS 최소화 |
| hreflang ko-KR + x-default | ✓ |
| Netlify 보안 헤더 (X-Content-Type-Options, X-Frame-Options 등) | ✓ _headers |

## 색인 속도 예상 (netlify.app 기준)

| 검색엔진 | 첫 색인 | 전체 색인 완료 |
|---|---|---|
| Bing (IndexNow 연동) | 즉시~수 시간 | 1~3일 |
| Naver Yeti (IndexNow + RSS) | 1~3일 | 2~3주 (서브도메인 패널티 약간 있음) |
| Google | 1~7일 (URL 검사 시 즉시) | 3~8주 (서브도메인 평가 기간 포함) |
| Daum | 1~2주 | 2~4주 |

## 자체 도메인 권장

netlify.app 서브도메인은 임시 운영에는 충분하지만, 장기 SEO 점수·검색엔진 신뢰도 측면에서 **자체 도메인 연결**을 권장합니다:

1. 도메인 구매 (가비아·후이즈 등)
2. Netlify → Domain settings → Add custom domain
3. DNS 설정 (Netlify 안내대로 CNAME 또는 A record)
4. `build/data/site.py`의 `base_url`·`domain` 교체 → 재빌드
5. GSC/Naver에 새 속성 등록 → 인증 토큰 교체

## 색인 속도 가속 팁

1. **외부 도메인 백링크 1~2개 확보** — Google이 가장 빠르게 발견하는 신호
2. **GSC URL 검사 → 색인 요청을 매일 5~10개씩 분산 클릭** (일일 약 10건 한도)
3. **RSS 피드를 Feedly·Inoreader 등에 직접 등록** → 외부 크롤러 신호
4. **Naver Search Advisor → 요청 → 웹페이지 수집** 매일 5건 한도 적극 활용
5. **소셜 미디어 공유** (X, 카카오톡 오픈채팅 등) → 외부 신호
6. **배포 직후 `python3 ping_search_engines.py` 실행** → IndexNow 즉시 알림
