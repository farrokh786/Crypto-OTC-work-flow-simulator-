from price_aggregator import aggregate_prices

def build_quote(size_btc, spread_bps=8):
    bid_avg, ask_avg = aggregate_prices()
    mid = (bid_avg + ask_avg) / 2
    spread = mid * spread_bps / 10000

    return {
        "size": size_btc,
        "mid": round(mid, 2),
        "bid": round(mid - spread, 2),
        "ask": round(mid + spread, 2)
    }

if __name__ == "__main__":
    q = build_quote(200)
    print("Two-way quote for 200 BTC:")
    print(q)
