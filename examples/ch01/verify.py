"""Ch.1 예제 검증 — 챕터에 실린 주장이 실제로 성립하는지 직접 확인한다.

실행:  uv run python verify.py
"""
import asyncio
import time

from fastapi.testclient import TestClient

from app import app, estimate_cost


def check_fastapi() -> None:
    print("── FastAPI / Pydantic ──")
    c = TestClient(app)

    r = c.get("/healthz")
    assert r.status_code == 200, r.text
    print(f"  healthz : {r.status_code} {r.json()}")

    r = c.post("/ask", json={"question": "what is RAG", "style": "short"})
    assert r.status_code == 200, r.text
    print(f"  ask     : {r.status_code} cost_usd={r.json()['cost_usd']}")

    # Field(min_length=1) 이 Bean Validation 처럼 실제로 동작하는가
    r = c.post("/ask", json={"question": "", "style": "short"})
    assert r.status_code == 422 and r.json()["detail"][0]["type"] == "string_too_short"
    print(f"  빈 문자열: {r.status_code} {r.json()['detail'][0]['type']}")

    # Literal 이 enum 처럼 동작하는가
    r = c.post("/ask", json={"question": "hi", "style": "weird"})
    assert r.status_code == 422 and r.json()["detail"][0]["type"] == "literal_error"
    print(f"  잘못된 enum: {r.status_code} {r.json()['detail'][0]['type']}")


def check_cost() -> None:
    print("── 비용 계산 ──")
    # 입력 1M + 출력 1M = 0.30 + 2.50
    got = estimate_cost(1_000_000, 1_000_000)
    assert got == 2.80, got
    print(f"  1M in + 1M out = ${got}  (기대 $2.80)")


async def check_async() -> None:
    print("── asyncio ──")

    async def io(sec: float) -> None:
        await asyncio.sleep(sec)

    t = time.perf_counter()
    await io(0.3)
    await io(0.3)
    await io(0.3)
    seq = time.perf_counter() - t

    t = time.perf_counter()
    await asyncio.gather(io(0.3), io(0.3), io(0.3))
    par = time.perf_counter() - t

    print(f"  순차 await     : {seq:.2f}s")
    print(f"  asyncio.gather : {par:.2f}s")
    assert par < seq * 0.5, "gather 가 순차보다 유의미하게 빨라야 한다"

    try:
        async with asyncio.timeout(0.1):
            await io(5)
        raise AssertionError("TimeoutError 가 발생했어야 한다")
    except TimeoutError:
        print("  asyncio.timeout: TimeoutError 정상 발생")


if __name__ == "__main__":
    check_fastapi()
    check_cost()
    asyncio.run(check_async())
    print("\n✅ 모든 검증 통과")
