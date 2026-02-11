import requests
from statistics import mean

EXCHANGES = {
    "binance": "https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT",
    "coinbase": "https://api.exchange.coinbase.com/products/BTC-USD/ticker",
    "okx": "https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT"
}

def get_binance():
    r = requests.get(EXCHANGES["binance"]).json()
    return float(r["bidPrice"]), float(r["askPrice"])

def get_coinbase():
    r = requests.get(EXCHANGES["coinbase"]).json()
    return float(r["bid"]), float(r["ask"])

def get_okx():
    r = requests.get(EXCHANGES["okx"]).json()["data"][0]
    return float(r["bidPx"]), float(r["askPx"])

def aggregate_prices():
    bids, asks = [], []
    for fn in [get_binance, get_coinbase, get_okx]:
        bid, ask = fn()
        bids.append(bid)
        asks.append(ask)
    return mean(bids), mean(asks)
