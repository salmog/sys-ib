from fastapi import FastAPI
from sqlalchemy import text

from app.api.strategy import router as strategy_router
from app.db.session import SessionLocal

app = FastAPI(
    title="SYS-IB",
    version="0.1.0"
)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/db-test")
def db_test():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))
        return {
            "db": "connected"
        }
    finally:
        db.close()


app.include_router(strategy_router)
