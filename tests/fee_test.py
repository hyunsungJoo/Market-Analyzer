import os
import ccxt
from dotenv import load_dotenv
from pathlib import Path

# .env 로드
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

access = os.getenv("UPBIT_ACCESS_KEY")
secret = os.getenv("UPBIT_SECRET_KEY")

if not access or not secret:
    raise RuntimeError("UPBIT_ACCESS_KEY / UPBIT_SECRET_KEY가 .env에 없습니다.")

# 업비트 연결
exchange = ccxt.upbit({
    "apiKey": access,
    "secret": secret,
    "enableRateLimit": True,
})

symbol = "BTC/KRW"

# 수수료 조회
fee = exchange.fetch_trading_fee(symbol)

print("=== 업비트 BTC/KRW 수수료 정보 ===")
print(f"Market: {symbol}")

maker = fee.get("maker")
taker = fee.get("taker")

if maker is not None:
    print(f"Maker 수수료: {maker * 100:.4f}%")
else:
    print("Maker 수수료: 조회 불가")

if taker is not None:
    print(f"Taker 수수료: {taker * 100:.4f}%")
else:
    print("Taker 수수료: 조회 불가")

print("원본 응답:", fee)
