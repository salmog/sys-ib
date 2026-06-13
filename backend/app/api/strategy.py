from typing import List

from fastapi import APIRouter
from app.models.core import Strategy

router = APIRouter(
    prefix="/strategies",
    tags=["Strategies"]
)

strategies: List[Strategy] = []


@router.get("/")
def list_strategies():
    return strategies


@router.post("/")
def create_strategy(strategy: Strategy):
    strategies.append(strategy)
    return {
        "message": "Strategy created",
        "strategy": strategy
    }
