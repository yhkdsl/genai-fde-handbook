# STYLE_GUIDE.md — 챕터 작성 규격

모든 챕터는 이 규격을 따른다. 새 챕터를 만들 때 이 문서를 먼저 읽는다.

---

## 0. 챕터를 추가해도 되는지 판단하는 기준

**단 하나의 질문에 답할 수 있어야 한다.**

> 이 챕터는 `jd/` 의 어느 공고, 어느 문장에 대응하는가?

답하지 못하면 그 챕터는 쓰지 않는다. 예외 없다.
이 기준 때문에 Transformer 내부 구조, Attention 수식, Python 문법 심화는 제외되었다.

## 1. 챕터 구조 (고정)

```
챕터 헤더    — kicker(Phase) / 제목 / 부제 / 메타(소요시간·선행지식·산출물)
§ x.1        — 이 챕터를 읽는 이유          [note.signal]
§ x.2        — 아무것도 모르는 사람 기준 설명
§ x.3        — 개념 · 원리 (왜 이렇게 되어 있는가)
§ x.4        — Java/Spring 대응 매핑         (해당 시)
§ x.5        — 실행 검증된 코드
§ x.6        — 엔터프라이즈 관점 / FDE처럼 생각하기
§ x.7        — 체크리스트 (progress bar 연동)
§ x.8        — 과제 (배정 시간 안에 끝나는 크기)
챕터 네비게이션
```

`§ x.6`은 생략 불가다. **"어떻게 만드나"가 아니라 "왜 그 선택인가"** 를 다루는 자리이며,
면접 루프에서 배점이 가장 큰 부분이 여기다.

## 2. 문체

- **경어체를 쓰지 않는다.** "~한다", "~이다" 로 통일. 교재 문체
- 아무것도 모르는 사람이 읽는다고 가정하되, **9년차가 아는 것은 반복하지 않는다**
  - ❌ "HTTP는 요청과 응답으로 이루어진 프로토콜입니다"
  - ✅ "임베딩은 문장을 숫자 배열로 바꾼 것이다. 왜 그게 검색에 쓰이는지가 핵심이다"
- 추측을 사실처럼 쓰지 않는다. 근거가 없으면 "확인 필요"라고 적는다
- 분량을 늘리기 위한 문장을 넣지 않는다

## 3. 근거 표기

공고를 인용할 때는 **원문 그대로**, `<blockquote>` 또는 `<em>` 으로 표시하고 출처를 밝힌다.
번역만 싣지 않는다 — 면접은 영어로 진행될 수 있고, 원문 표현 자체가 암기 대상이다.

```html
<blockquote>"Architect and code the connective tissue between Google's AI products
and customer's live infrastructure"</blockquote>
```

## 4. 코드

- **실행해서 검증한 것만 싣는다.** 미검증 코드는 저장소에 들어가지 않는다
- Python 3.12 / `uv` / 타입힌트 필수
- 코드 주변에 "왜 이 방식인가"를 한 줄이라도 적는다
- 예제는 짧게. 전체 구현은 프로젝트 저장소에 두고 링크한다

## 5. HTML 규격

### 파일

- `docs/chNN-slug.html` — 두 자리 번호 + 영문 슬러그
- `<html lang="ko">`, UTF-8, viewport 메타 필수
- `assets/handbook.css` 와 `assets/handbook.js` 만 참조. 챕터별 CSS 파일을 만들지 않는다

### 사용 가능한 컴포넌트

| 클래스 | 용도 |
|---|---|
| `.note` | 일반 보조 설명 |
| `.note.signal` | 핵심 · 전략적 판단 (주황) |
| `.note.evidence` | 검증된 사실 · 통과 기준 (청록) |
| `.note.warn` | 주의 · 함정 (황색) |
| `.table-scroll > table` | 표. **반드시 `.table-scroll` 로 감싼다** (모바일 가로 스크롤) |
| `.diagram` | ASCII 다이어그램. `white-space: pre` |
| `.stats > .stat` | 숫자 요약 스트립 |
| `.checklist` | 체크리스트. localStorage에 자동 저장됨 |
| `.progress[data-progress-for="id"]` | 진행률 바. 해당 id 안의 checklist를 집계 |
| `.pill.p1/.p2/.p3/.px` | 우선순위 배지 |
| `.cards > .card` | 목차 카드. 미완성은 `.card.pending` |

### 체크리스트 + 진행률 연동

```html
<div class="progress" data-progress-for="ch5-check">
  <div class="progress-bar"><div class="progress-fill"></div></div>
  <div class="progress-label">0 / 0 완료 · 0%</div>
</div>
<div id="ch5-check">
  <ul class="checklist">
    <li><label><input type="checkbox" data-id="c1"><span>항목</span></label></li>
  </ul>
</div>
```

`data-id` 는 챕터 안에서 고유해야 한다. 체크 상태는 파일명 기준으로 localStorage에 저장되므로
**파일명을 바꾸면 진행 상태가 초기화된다.** 챕터 파일명은 확정 후 바꾸지 않는다.

## 6. 디자인 원칙

18주간 매일 읽는 문서다. **가독성이 최우선이고 화려함은 부채다.**

- 본문 폭 `74ch` 고정 — 긴 줄은 읽기 어렵다
- 라이트/다크 양쪽 모두 지원. 토글은 localStorage에 저장
- 새 색을 도입하지 않는다. CSS 변수 안에서만 쓴다
- 애니메이션은 진행률 바 외에는 넣지 않는다

## 7. 체크리스트 작성 규칙

- **읽었는지가 아니라 할 수 있는지**를 묻는다
  - ❌ "임베딩 섹션을 읽었다"
  - ✅ "임베딩 유사도가 왜 코사인인지 설명할 수 있다"
- 마지막에 반드시 **"다음 챕터로 넘어가도 되는 기준"** 을 `.note.evidence` 로 명시한다
- 그 기준은 2~3개로 좁힌다. 전부 다 하라고 하면 아무것도 안 하게 된다

## 8. 과제 작성 규칙

- 챕터에 배정된 시간 **안에** 끝나는 크기여야 한다. 각 과제에 분 단위 예상 시간을 적는다
- 결과물은 `work/chNN/` 에 남긴다. 머릿속에만 있으면 사라진다
- 가능하면 **이력서·면접에서 재사용되는 형태**로 만든다 (경력 매핑, 디스커버리 질문 등)

## 9. 갱신

공고나 API가 바뀌면:
1. `jd/` 원문 갱신 + 수집일 변경
2. 영향받는 챕터 수정
3. `README.md` 버전 갱신
4. 커밋 메시지에 `docs: update JD — <무엇이 바뀌었는지>`
