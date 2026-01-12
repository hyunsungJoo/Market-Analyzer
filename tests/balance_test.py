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

exchange = ccxt.upbit({
    "apiKey": access,
    "secret": secret,
    "enableRateLimit": True,
})

# 1️⃣ 현재 비트코인 가격 (원화)
ticker = exchange.fetch_ticker("BTC/KRW")
btc_price = ticker["last"]

# 2️⃣ 잔고 조회
balance = exchange.fetch_balance()

krw = balance["KRW"]["total"]
btc = balance["BTC"]["total"]

# 3️⃣ BTC → 원화 환산
btc_value = btc * btc_price
total_value = krw + btc_value

# 4️⃣ 보기 좋게 출력
print(f"현재 BTC 가격: {btc_price:,.0f}원")
print(f"보유 원화: {krw:,.0f}원")
print(f"보유 BTC: {btc:.6f} BTC (약 {btc_value:,.0f}원)")
print(f"총 자산: 약 {total_value:,.0f}원")
