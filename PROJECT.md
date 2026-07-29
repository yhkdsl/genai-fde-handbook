# PROJECT.md — 이 프로젝트의 헌법

> 이 문서는 모든 작업의 기준이다. 챕터를 쓰거나 프로젝트를 만들 때 여기에 어긋나면 그 작업이 틀린 것이다.

---

## 1. 목표

**9년차 백엔드 엔지니어(Java/Kotlin/Spring Boot/K8s)를 GenAI Forward Deployed Engineer로 전환한다.**

목표는 "합격"이 아니라 **"그 일을 실제로 할 수 있는 상태"** 다.
그 상태에 도달하면 Google, OpenAI 외에 Anthropic, Microsoft, AWS, Palantir 등에도 동일하게 통한다.

## 2. 타겟 (우선순위 확정)

| 순위 | 포지션 | 근거 | JD 원문 |
|---|---|---|---|
| **1** | Google Cloud — GenAI FDE, Seoul (Korean/English) | 경력 게이트가 **2+ yrs Python**. 연차 요건 이미 초과. 관문이 "만들어본 것"이라 통제 가능. 한국어 요구가 경쟁 풀을 좁힘 | [google-fde-genai-seoul.md](jd/google-fde-genai-seoul.md) |
| **2** | OpenAI — Forward Deployed Engineer, Seoul | 5+ yrs 엔지니어링 요건 충족. Google FDE와 교집합 큼. 추가 필요분은 풀스택 + OpenAI 스택 | [openai-fde-seoul.md](jd/openai-fde-seoul.md) |
| 3 | OpenAI — AI Deployment Engineer, Seoul | **6+ yrs technical consulting** 요구 → 공부로 못 메움. FDE 경유 후 내부 이동이 현실적 | [openai-ade-seoul.md](jd/openai-ade-seoul.md) |
| — | OpenAI — ADE Codex, Korea | 8+ yrs post-sales. 지원 대상 아님. 단 "AI 코딩툴 파워유저" 항목은 차별화 소재로 재활용 | [openai-ade-codex-korea.md](jd/openai-ade-codex-korea.md) |

## 3. 세 JD의 교집합 — 여기에 자원을 몰아넣는다

1. **프로덕션에 실제 배포된** LLM 시스템 (로컬 데모는 증거가 아님)
2. RAG — 정형 + 비정형, 하이브리드 검색, 벡터 DB
3. 에이전트 + MCP
4. **Evaluation / Observability** — 세 JD 전부에 명시. 가장 저평가되어 있고 가장 차별화됨
5. 레거시 연동 · 보안 경계 · 인증 · 네트워크 ← **9년 백엔드가 그대로 무기가 되는 유일한 칸**
6. 비용/지연 계측 (cost-per-request, tokens/sec, p95 latency)
7. 고객 대면 서사 — discovery → ROI → 이해관계자 커뮤니케이션

## 4. 원칙

### 원칙 1 — 증거만 카운트한다
읽은 것은 증거가 아니다. **배포된 URL, 커밋 히스토리, 측정된 수치, 머지된 PR**만 증거다.
챕터를 다 읽어도 배포된 게 없으면 진도는 0이다.

### 원칙 2 — JD에 없는 것은 만들지 않는다
Transformer 내부 구조, Attention 수식, Python 문법 80페이지는 세 JD 어디에도 없다.
분량 욕심이 아니라 **JD 매핑표**가 목차를 결정한다.
새 챕터를 추가하려면 "어느 JD의 어느 문장에 대응하는가"를 답할 수 있어야 한다.

### 원칙 3 — 9년차는 문법이 아니라 판단을 배운다
Java/Spring 자산을 버리고 새로 배우는 게 아니라 **매핑**한다.
그리고 "어떻게 만드나"보다 **"왜 그 선택을 했나"** 를 훈련한다. 면접 루프가 그것을 본다.

### 원칙 4 — Provider-portable
Google(Gemini/Vertex/ADK)과 OpenAI 양쪽을 노리므로, 모든 프로젝트는 얇은 어댑터 층 위에 올린다.
이건 타협이 아니라 **Google JD "architecting AI systems on cloud platforms"** 와
**OpenAI JD "codify working patterns into reusable building blocks"** 에 동시에 부합하는 설계다.
면접에서 "왜 이렇게 설계했나"에 답이 나오는 구조 = 실제 엔터프라이즈의 벤더 락인 회피 전략.

### 원칙 5 — 코드는 실행해서 검증한 것만 싣는다
돌려보지 않은 예제 코드는 이 저장소에 들어가지 않는다.

### 원칙 6 — 살아있는 문서
API와 채용공고는 변한다. `jd/` 의 원문은 수집일을 박아 보존하고, 변경 시 갱신하고 CHANGELOG에 남긴다.

## 5. 비목표 (하지 않는 것)

- 모델 학습 / 파인튜닝 연구 — FDE는 배포하는 사람이지 학습시키는 사람이 아니다
- Transformer 내부 수학 심화
- LeetCode 알고리즘 훈련 — FDE 루프는 알고리즘 중심이 아니다
- 분량을 위한 분량. **500페이지 목표 같은 것은 없다**
- AI가 생성한 학습 노트를 포트폴리오라고 부르는 것

## 6. 산출물 구조

**저장소를 분리한다.** 학습 기록과 포트폴리오는 독자가 다르다.

| 저장소 | 성격 | 공개 |
|---|---|---|
| `genai-fde-handbook` (이 저장소) | 학습 자료 + 로드맵 + JD 근거 + 진행 로그. GitHub Pages | public |
| `project-a-*` | 하이브리드 RAG. **이력서에 링크되는 것** | public |
| `project-b-*` | 멀티에이전트 + MCP + Observability | public |
| `project-c-*` | provider-portable 어댑터 (A/B에서 추출) | public |

> 포트폴리오 프로젝트를 학습 저장소 안에 묻으면 포트폴리오로 읽히지 않는다.

## 7. 스택 결정

| 영역 | 선택 | 이유 |
|---|---|---|
| 언어 | Python 3.12 | 세 JD 모두 Python 명시 |
| 패키지 | `uv` | 이미 설치됨, 빠름 |
| 웹 | FastAPI | Spring Boot 대응물, 타입 기반 |
| 1차 클라우드 | **GCP** (Cloud Run, Vertex AI) | Google JD min ③ 직접 대응 |
| 2차 | OpenAI API | OpenAI FDE 대응 |
| 에이전트 | **ADK** 우선, LangGraph 병행 | Google pref에 ADK 명시 |
| 관측 | OpenTelemetry | 벤더 중립 |
| 프론트 | 최소한의 실사용 UI | OpenAI FDE "full-stack" 요건 |

## 8. 언어 정책

- **학습 자료(docs/)**: 한국어 — 이해 속도 우선
- **포트폴리오 저장소 README / 코드 / 커밋**: **영어** — 심사자가 읽는 것
- Google JD가 한국어+영어를 모두 요구하므로 양쪽 산출물이 다 필요하다

## 9. 투입 예산

**주 10시간 × 18주 = 약 180시간.** (2026-08-03 ~ 2026-12-06)
이 예산을 넘기는 계획은 계획이 아니라 희망이다. 자세한 배분은 [ROADMAP.md](ROADMAP.md).

## 10. 지원 시점

**준비 완료를 기다리지 않는다.** Phase 2(Project A 배포) 종료 시점인 **2026년 10월 중순에 1차 지원**한다.
- 채용 공고는 닫힌다. 완벽한 준비를 기다리면 문이 사라진다
- 탈락해도 면접 루프 자체가 최고 품질의 데이터다
- 재지원은 가능하고, 그때는 실제 면접 경험을 갖고 들어간다
