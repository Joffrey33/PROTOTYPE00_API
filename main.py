from fastapi import FastAPI, Header, HTTPException
from binance.client import Client
import config

app = FastAPI()

SECRET_TOKEN = "PROTOTYPE00_SECRET"

# Connexion à Binance (lecture seule)
client = Client(config.API_KEY, config.API_SECRET)

def verify_token(authorization: str = Header(None)):
    if authorization != f"Bearer {SECRET_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/")
async def root():
    return {"message": "PROTOTYPE 00 API en ligne - Simulation Only"}

@app.get("/rsi")
async def get_rsi(authorization: str = Header(None)):
    verify_token(authorization)
    return {"rsi": 28.5, "status": "SIMULATION"}

@app.get("/balance")
async def get_balance(authorization: str = Header(None)):
    verify_token(authorization)
    try:
        balances = client.get_account()
        usdt_balance = next((b for b in balances['balances'] if b['asset'] == 'USDT'), None)
        return {
            "asset": "USDT",
            "free": usdt_balance['free'],
            "locked": usdt_balance['locked']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
