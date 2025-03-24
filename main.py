from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "PROTOTYPE 00 API en ligne - Simulation Only"}

@app.get("/rsi")
async def get_rsi():
    # Ici on mettra la vraie lecture Binance plus tard
    return {"rsi": 28.5, "status": "SIMULATION"}
