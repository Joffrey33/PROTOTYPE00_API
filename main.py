from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# Ton token secret à modifier si tu veux
SECRET_TOKEN = "PROTOTYPE00_SECRET"

# Fonction de vérification du token
def verify_token(authorization: str = Header(None)):
    if authorization != f"Bearer {SECRET_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/")
async def root():
    return {"message": "PROTOTYPE 00 API en ligne - Simulation Only"}

@app.get("/rsi")
async def get_rsi(authorization: str = Header(None)):
    verify_token(authorization)
    # Ici, plus tard, on récupérera la vraie valeur Binance
    return {"rsi": 28.5, "status": "SIMULATION"}
