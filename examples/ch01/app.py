"""Ch.1-2 검증용 — Spring Boot 대응물을 FastAPI로."""
from functools import lru_cache
from typing import Annotated, Literal

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# @ConfigurationProperties / application.yml 대응
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env", extra="ignore")

    project_id: str = "local-dev"
    location: str = "us-central1"
    model: str = "gemini-2.5-flash"
    max_output_tokens: int = Field(default=1024, ge=1, le=65535)


@lru_cache  # @Singleton — 앱 생애주기 동안 1회만 생성
def get_settings() -> Settings:
    return Settings()


SettingsDep = Annotated[Settings, Depends(get_settings)]


# DTO — Bean Validation 대응. 런타임에 실제로 검증된다
class AskRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    style: Literal["short", "detailed"] = "short"


class AskResponse(BaseModel):
    answer: str
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float


app = FastAPI(title="ch12-verify")


@app.get("/healthz")
def healthz(s: SettingsDep) -> dict[str, str]:
    return {"status": "ok", "project": s.project_id, "model": s.model}


# gemini-2.5-flash 공개 가격 (USD per 1M tokens)
PRICE_IN, PRICE_OUT = 0.30, 2.50


def estimate_cost(input_tokens: int, output_tokens: int) -> float:
    return round(input_tokens / 1e6 * PRICE_IN + output_tokens / 1e6 * PRICE_OUT, 8)


@app.post("/ask", response_model=AskResponse)
async def ask(req: AskRequest, s: SettingsDep) -> AskResponse:
    if req.style == "detailed" and len(req.question) < 5:
        raise HTTPException(status_code=422, detail="detailed 모드는 질문이 더 길어야 함")
    # 실제 호출부는 Ch.2에서. 여기서는 계측 경로만 검증한다
    in_tok, out_tok = len(req.question.split()), 42
    return AskResponse(
        answer=f"[stub:{req.style}] {req.question}",
        model=s.model,
        input_tokens=in_tok,
        output_tokens=out_tok,
        cost_usd=estimate_cost(in_tok, out_tok),
    )
