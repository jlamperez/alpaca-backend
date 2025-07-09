from fastapi import APIRouter
from app.alpaca_service import get_account, buy_stock, get_latest_price

router = APIRouter()

@router.get("/account")
def read_account():
    return get_account()

@router.post("/buy/{symbol}")
def buy(symbol: str):
    return buy_stock(symbol)

@router.get("/price/{symbol}")
def price(symbol: str):
    return get_latest_price(symbol)