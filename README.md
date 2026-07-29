# GenAI FDE Handbook

**Senior Backend Engineer → GenAI Forward Deployed Engineer**
18주 · 180시간 전환 계획과 학습 자료. 2026-08-03 → 2026-12-06.

---

## 이게 뭔가

9년차 백엔드 엔지니어(Java/Kotlin/Spring Boot/Kubernetes)가 GenAI Forward Deployed Engineer로
전환하기 위한 **학습 저장소이자 실행 계획**이다.

일반적인 로드맵과 다른 점은 하나다. **모든 항목이 실제 채용 공고 원문에 근거한다.**
"AI 엔지니어가 되려면 이런 걸 배워야 한다더라"가 아니라, 서울에 실제로 열려 있는 공고 4건을
문장 단위로 분해해서 거기 있는 것만 다룬다. 거기 없는 것은 의도적으로 뺀다.

## 시작하기

1. **[docs/index.html](docs/index.html)** — 목차와 진행 상황
2. **[PROJECT.md](PROJECT.md)** — 이 프로젝트의 헌법. 원칙, 타겟, 비목표
3. **[ROADMAP.md](ROADMAP.md)** — 18주 주차별 계획과 시간 배분
4. **[jd/](jd/)** — 근거가 되는 채용 공고 원문 4건 (수집일 명시)

바로 읽을 것: **[Chapter 0 — Forward Deployed Engineer라는 직무](docs/ch00-role-analysis.html)**

## 타겟

| 순위 | 포지션 | 핵심 경력 요건 | 근거 |
|---|---|---|---|
| **1** | Google Cloud — GenAI FDE, Seoul (Korean/English) | Python 개발 **2년** | [원문](jd/google-fde-genai-seoul.md) |
| 2 | OpenAI — Forward Deployed Engineer, Seoul | 엔지니어링·기술 배포 **5년+** | [원문](jd/openai-fde-seoul.md) |
| 3 | OpenAI — AI Deployment Engineer, Seoul | technical consulting **6년+** | [원문](jd/openai-ade-seoul.md) |
| — | OpenAI — ADE, Codex \| Korea | post-sales **8년+** | [원문](jd/openai-ade-codex-korea.md) |

Google FDE가 1순위인 이유는 **경력 연차가 아니라 "무엇을 만들어봤는가"로 게이트를 걸기 때문**이다.
연차는 만들 수 없지만 만들어본 것은 만들 수 있다.

## 구성

```
genai-fde-handbook/
├── PROJECT.md          # 헌법 — 원칙, 타겟, 비목표, 스택 결정
├── ROADMAP.md          # 18주 계획, 시간 배분, 진행 로그
├── STYLE_GUIDE.md      # 챕터 작성 규격
├── jd/                 # 채용 공고 원문 (근거 보존)
├── docs/               # GitHub Pages — 챕터 HTML
│   ├── index.html
│   ├── ch00-role-analysis.html
│   └── assets/
└── work/               # 과제 결과물 (갭 분석, 경력 매핑 등)
```

## 포트폴리오 프로젝트는 여기 없다

**의도적으로 분리했다.** 학습 기록과 포트폴리오는 읽는 사람이 다르다.
프로젝트 A·B·C는 각각 독립 저장소로 만들고, 이력서에는 그쪽이 링크된다.
학습 저장소 안에 묻힌 프로젝트는 포트폴리오로 읽히지 않는다.

| 프로젝트 | 내용 | 상태 |
|---|---|---|
| A. Enterprise Hybrid RAG | 정형+비정형 하이브리드 RAG, 권한 필터, eval, GCP 배포 | 예정 (W5–10) |
| B. Multi-Agent + MCP | ADK 위계 위임 에이전트, 자작 MCP 서버, OTel 트레이싱 | 예정 (W11–16) |
| C. Provider Adapter | OpenAI/Vertex 양립 어댑터 (A·B에서 추출) | 부산물 |

## 원칙

1. **증거만 카운트한다** — 배포된 URL, 커밋, 측정된 수치, 머지된 PR. 읽은 것은 증거가 아니다
2. **JD에 없는 것은 만들지 않는다** — 새 챕터는 "어느 공고의 어느 문장인가"에 답할 수 있어야 한다
3. **9년차는 문법이 아니라 판단을 배운다** — 기존 자산을 버리지 않고 매핑한다
4. **Provider-portable** — Google·OpenAI 양쪽을 노리므로 어댑터 층 위에 올린다
5. **실행해서 검증한 코드만 싣는다**
6. **살아있는 문서** — 공고와 API는 변한다. 수집일을 박고 갱신한다

## 버전

`v0.1` (2026-07-29) — 저장소 구성, JD 근거 4건 수집, Chapter 0 완성
