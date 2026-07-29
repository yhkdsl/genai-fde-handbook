# Ch.1 — verified example

Chapter 1에 실린 코드의 실행 가능한 원본. 챕터의 주장을 **직접 돌려서** 확인할 수 있다.

```bash
uv run python verify.py      # 검증 스크립트
uv run uvicorn app:app --reload   # 서버 띄우고 http://127.0.0.1:8000/docs
```

## 무엇을 검증하는가

| 챕터의 주장 | 검증 방법 |
|---|---|
| Pydantic이 Bean Validation처럼 동작한다 | 빈 문자열 → `422 string_too_short` |
| `Literal`이 enum처럼 동작한다 | 잘못된 값 → `422 literal_error` |
| `BaseSettings`가 `@ConfigurationProperties` 대응 | `/healthz`가 설정값을 반환 |
| `asyncio.gather`가 `CompletableFuture.allOf` 대응 | 0.90s → 0.30s |
| `asyncio.timeout`이 `orTimeout` 대응 | `TimeoutError` 발생 |
| 비용 계산식 | 1M in + 1M out = $2.80 |

## 검증 환경

Python 3.12.13 · FastAPI 0.140.13 · Pydantic 2.13.4 · google-genai 2.14.0 (2026-07-29)

가격은 [Vertex AI 공식 가격표](https://cloud.google.com/vertex-ai/generative-ai/pricing) 기준.
`app.py`의 `PRICE_IN` / `PRICE_OUT` 상수는 변경 시 갱신할 것.
