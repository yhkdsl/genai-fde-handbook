# ROADMAP — 18주 / 180시간

- **기간**: 2026-08-03 (월) ~ 2026-12-06 (일)
- **예산**: 주 10시간 × 18주 = **180시간**
- **1차 지원 시점**: **2026년 10월 중순** (W10 종료 직후). 준비 완료를 기다리지 않는다.

> 예산을 넘기는 계획은 계획이 아니라 희망이다. 아래 시간 배분은 전부 합쳐 180h를 넘지 않는다.
> 밀리면 **범위를 줄이지 말고 Phase 3의 스코프를 줄인다.** Phase 2(Project A)는 절대 축소하지 않는다 — Google JD min ③④가 여기 걸려 있다.

---

## 전체 배분

| Phase | 기간 | 주차 | 시간 | 산출물(증거) |
|---|---|---|---|---|
| **0. 기반** | 08-03 ~ 08-16 | W1–W2 | 20h | GCP 프로젝트 가동, FastAPI 서비스 1개 배포 |
| **1. LLM 실무 핵심** | 08-17 ~ 08-30 | W3–W4 | 20h | 구조화 출력·툴콜링 동작 코드, 비용 계측기 |
| **2. Project A — Hybrid RAG** | 08-31 ~ 10-11 | W5–W10 | 60h | **GCP에 배포된 RAG 서비스 + eval 리포트** |
| ⟶ **1차 지원** | 10월 중순 | — | — | 이력서 + 프로젝트 A 링크 |
| **3. Project B — Agents + MCP** | 10-12 ~ 11-22 | W11–W16 | 60h | 멀티에이전트 + MCP 서버 + 트레이싱 대시보드 |
| **4. 포트폴리오·기여·면접** | 11-23 ~ 12-06 | W17–W18 | 20h | Cookbook PR, 케이스스터디, 면접 대본 |

> W8(09-21~09-27)은 추석 연휴가 걸린다. **버퍼 주차로 잡고 계획에서 이미 할인**했다.

---

## Phase 0 — 기반 (W1–W2, 20h)

**목표**: Java 자산을 Python으로 옮기고, GCP에 뭔가를 실제로 띄운다.

문법 학습이 아니다. 9년차에게 필요한 것은 매핑 테이블과 "돌아가는 것 하나"다.

| 주차 | 시간 | 할 일 | 완료 증거 |
|---|---|---|---|
| W1 | 10h | Python 실무 전환 (`uv`, 타입힌트, `async`, Pydantic) / Java↔Python 매핑 정리 | 매핑 문서 + 로컬 FastAPI 실행 |
| W2 | 10h | GCP 계정·과금·IAM 셋업, Cloud Run에 FastAPI 배포, Vertex AI에서 Gemini 첫 호출 | **공개 URL 하나** + Gemini 응답 로그 |

**핵심 매핑** (Ch.1에서 상세)

| Java/Spring | Python |
|---|---|
| Spring Bean / DI | FastAPI `Depends` |
| `@RestController` | `APIRouter` |
| `@Configuration` / `application.yml` | Pydantic `BaseSettings` |
| `CompletableFuture` | `asyncio` / `await` |
| Hibernate / JPA | SQLAlchemy 2.0 |
| Maven / Gradle | `uv` + `pyproject.toml` |
| Bean Validation | Pydantic 모델 |

**통과 기준**: 인터넷에서 접근 가능한 Cloud Run URL이 Gemini 응답을 반환한다. 안 되면 다음으로 못 넘어간다.

---

## Phase 1 — LLM 실무 핵심 (W3–W4, 20h)

**목표**: JD에 걸린 것만 판다. Transformer 내부는 건너뛴다.

| 주차 | 시간 | 할 일 | 완료 증거 |
|---|---|---|---|
| W3 | 10h | 토큰·컨텍스트 윈도우·temperature / 임베딩 실측 / **구조화 출력(Structured Output)** | 임베딩 유사도 실험 노트북 |
| W4 | 10h | **툴 콜링**, 비용·지연 계측 래퍼 작성 (cost-per-request, tokens/sec, p95) | 계측 미들웨어 코드 + 측정 수치 |

W4의 계측 래퍼는 버리는 코드가 아니다. **Project A와 B가 이걸 그대로 쓴다.**
Google JD preferred의 *"LLM-native metrics (tokens/sec, cost-per-request)"* 가 여기서 나온다.

**통과 기준**: "이 질문 1건 처리에 얼마 들고 몇 초 걸리는가"를 숫자로 답할 수 있다.

---

## Phase 2 — Project A: Enterprise Hybrid RAG (W5–W10, 60h) ★ 최우선

> **Google JD minimum qualification ③④를 직접 겨냥한다. 이 프로젝트가 지원 가능 여부를 결정한다.**
> min③ *production-grade AI, conception to launch, architecting on GCP*
> min④ *pipelines for **structured and unstructured** data using **both vector databases and RAG-like architectures**, enterprise*

### 도메인 (권장)

**금융 리서치 어시스턴트** — 이미 갖고 있는 MoneyFlow SEC 데이터를 재활용한다.

- **정형**: 13F 기관 보유 종목 (포지션, 평가액, 분기 변동) → SQL / 집계
- **비정형**: SEC 공시 문서 본문 → 벡터 검색
- 질문 예: *"버크셔가 지난 분기 비중 늘린 종목 중, 최근 공시에서 리스크 요인이 언급된 곳은?"*
  → 라우터가 **정형 조회 + 비정형 검색을 둘 다** 태워야 답이 나온다. 이게 min④의 핵심.

대안 도메인: 사내 위키(비정형) + 이슈트래커(정형). 데이터가 없으면 공공 조달 공고로 대체.

### 주차 계획

| 주차 | 시간 | 할 일 |
|---|---|---|
| W5 | 10h | 데이터 파이프라인 — 정형 적재(Postgres/BigQuery), 비정형 청킹 전략 결정·측정 |
| W6 | 10h | 벡터 검색 구축 (Vertex AI Vector Search 또는 pgvector) + **하이브리드 검색 (BM25 + dense)** |
| W7 | 10h | **쿼리 라우터** — 정형/비정형/양쪽 분기. Reranker 도입 및 효과 측정 |
| W8 | 5h | (추석 버퍼) 권한 필터 — row-level 접근제어. **엔터프라이즈 RAG의 진짜 난제이자 백엔드 강점 칸** |
| W9 | 15h | **Eval 파이프라인** — 골든셋 50문항, 정확도/근거율/환각률 측정. 최소 UI |
| W10 | 10h | GCP 배포, 비용·지연 계측 연결, README(영문) 작성, 아키텍처 다이어그램 |

### 완료 기준 (전부 충족해야 함)

- [ ] 공개 URL에서 동작한다 (로컬 데모 ❌)
- [ ] 정형·비정형을 **함께** 쓰는 질문에 답한다
- [ ] 하이브리드 검색 + reranker 적용, **적용 전후 수치가 있다**
- [ ] eval 골든셋 결과가 리포트로 있다
- [ ] 사용자 권한에 따라 검색 결과가 달라진다
- [ ] 요청당 비용과 p95 지연이 대시보드에 뜬다
- [ ] 영문 README에 **아키텍처 결정과 그 이유**가 적혀 있다

> **W10 종료 = 1차 지원.** 이 시점의 이력서에는 "AI 공부 중"이 아니라
> "정형+비정형 하이브리드 RAG를 GCP에 배포하고 eval로 검증함"이 적힌다.

---

## Phase 3 — Project B: Multi-Agent + MCP (W11–W16, 60h)

> Google JD responsibility ①③, preferred(ADK/LangGraph, ReAct, self-reflection, hierarchical delegation) 대응
> OpenAI FDE JD의 full-stack / building blocks 대응

| 주차 | 시간 | 할 일 |
|---|---|---|
| W11 | 10h | **자작 MCP 서버** — Project A의 RAG를 MCP 툴로 노출 (A와 B가 연결된다) |
| W12 | 10h | **ADK** 기반 에이전트 1개 → ReAct 루프 |
| W13 | 10h | **위계 위임(hierarchical delegation)** — supervisor → worker 멀티에이전트 |
| W14 | 10h | **self-reflection** 패턴, 상태 관리(state management), 실패 복구 |
| W15 | 10h | **OpenTelemetry granular tracing** + 관측 대시보드 (accuracy / safety / latency) |
| W16 | 10h | 에이전트 eval 파이프라인, **ROI 계산 문서**, 프론트엔드 UI, 배포 |

### 완료 기준

- [ ] MCP 서버가 표준 클라이언트(Claude Desktop 등)에서 붙는다
- [ ] supervisor가 worker에게 실제로 위임하고 그 과정이 트레이스에 남는다
- [ ] 에이전트 실패 케이스를 잡아내는 eval이 있다
- [ ] "이 시스템이 사람 대비 몇 시간/얼마를 아끼는가"가 숫자로 적혀 있다
- [ ] 트레이스 UI에서 한 요청의 전 구간(툴 호출·토큰·비용·지연)이 보인다

### Project C (부산물, 별도 시간 배정 없음)

A/B를 만들다 보면 provider 어댑터 층이 자연히 추출된다. 이걸 별도 저장소로 분리해 공개한다.
→ OpenAI FDE JD *"Codify working patterns into tools, playbooks, or building blocks that others can use."* 직결.

---

## Phase 4 — 포트폴리오 · 기여 · 면접 (W17–W18, 20h)

| 주차 | 시간 | 할 일 |
|---|---|---|
| W17 | 10h | **오픈소스 기여** — OpenAI Cookbook 또는 GoogleCloudPlatform/generative-ai에 PR 1건. 영문 이력서 |
| W18 | 10h | 디스커버리 세션 대본, 케이스스터디 훈련, 영어 기술 면접 리허설 |

### 왜 Cookbook 기여인가 (추측 아님, JD 인용)

- OpenAI ADE: *"Contribute to our open-source developer and enterprise resources"*, *"publishing notebooks to our internal and external repositories"*
- OpenAI ADE Codex: *"Contribute technical content ... to the OpenAI Cookbook"*
- Google FDE: *"converting them into reusable modules or formal product feature requests"*

**세 회사가 문서로 명시한 업무다.** 머지된 PR 1건은 지원자 대부분이 못 가진 증거다.

### 면접 루프 대비 (조사된 FDE 루프 구조 기준)

1. 프로덕션 엔지니어링 기술 스크린 (알고리즘 아님)
2. **Deployment case study — 모호하게 주어진 고객 시나리오 스코핑** ← 가장 배점 큼
3. LLM 시스템 실전 경험 심층
4. 이해관계자 커뮤니케이션 (비기술 청중 대상 설명)
5. 가치·판단 대화

→ 2번은 암기로 안 된다. **"문서 몇 건? 갱신 주기? 정확도 목표? PII? 예산? 지연 한계? 평가 기준? 누가 검수?"**
   를 반사적으로 묻는 훈련을 W18에 반복한다.

---

## 진행 로그

| 주차 | 계획 시간 | 실제 | 산출물 | 상태 |
|---|---|---|---|---|
| W1 | 10h | — | — | ⬜ |
| W2 | 10h | — | — | ⬜ |
| W3 | 10h | — | — | ⬜ |
| W4 | 10h | — | — | ⬜ |
| W5 | 10h | — | — | ⬜ |
| W6 | 10h | — | — | ⬜ |
| W7 | 10h | — | — | ⬜ |
| W8 | 5h | — | — | ⬜ |
| W9 | 15h | — | — | ⬜ |
| W10 | 10h | — | — | ⬜ |
| W11 | 10h | — | — | ⬜ |
| W12 | 10h | — | — | ⬜ |
| W13 | 10h | — | — | ⬜ |
| W14 | 10h | — | — | ⬜ |
| W15 | 10h | — | — | ⬜ |
| W16 | 10h | — | — | ⬜ |
| W17 | 10h | — | — | ⬜ |
| W18 | 10h | — | — | ⬜ |
