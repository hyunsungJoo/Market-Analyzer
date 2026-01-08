import os
import ccxt
from dotenv import load_dotenv
from pathlib import Path

# 프로젝트 루트 기준 .env 경로
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

print("ENV PATH:", env_path)
print("ENV EXISTS:", env_path.exists())

load_dotenv(env_path)

access = os.getenv("UPBIT_ACCESS_KEY")
secret = os.getenv("UPBIT_SECRET_KEY")

print("ACCESS KEY LOADED:", bool(access))
print("SECRET KEY LOADED:", bool(secret))

if not access or not secret:
    raise RuntimeError("UPBIT_ACCESS_KEY / UPBIT_SECRET_KEY가 .env에 없습니다.")

exchange = ccxt.upbit({
    "apiKey": access,
    "secret": secret,
    "enableRateLimit": True,
})

balance = exchange.fetch_balance()

for coin in ["KRW", "BTC", "ETH", "XRP", "USDT"]:
    info = balance.get(coin)
    if info and info.get("total", 0) > 0:
        print(f"{coin}: total={info['total']}, free={info['free']}")
