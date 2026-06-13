from fastapi import FastAPI
from app.api.strategy import router as strategy_router

app = FastAPI(
    title="SYS-IB",
    version="0.1.0"
)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


app.include_router(strategy_router)
