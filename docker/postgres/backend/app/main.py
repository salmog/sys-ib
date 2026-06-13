from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine

app = FastAPI(title="sys-ib")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"db": "connected", "result": [row[0] for row in result]}
