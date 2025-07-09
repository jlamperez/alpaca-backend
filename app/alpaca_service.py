import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.historical.stock import StockHistoricalDataClient
from alpaca.data.requests import StockLatestTradeRequest

load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
IS_PAPER = os.getenv("ALPACA_PAPER", "True") == "True"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=IS_PAPER)
data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

def get_account():
    return trading_client.get_account().__dict__

def buy_stock(symbol):
    order = MarketOrderRequest(
        symbol=symbol,
        notional=1,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY,
    )
    return trading_client.submit_order(order_data=order).__dict__

def get_latest_price(symbol):
    request = StockLatestTradeRequest(symbol_or_symbols=symbol)
    trade = data_client.get_stock_latest_trade(request)
    return trade[symbol].__dict__