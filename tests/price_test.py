import ccxt

exchange = ccxt.upbit({
    "enableRateLimit": True
})

symbol = "BTC/KRW"

ticker = exchange.fetch_ticker(symbol)
price = ticker["last"]

print(f"현재 비트코인 가격: {price:,} KRW")

