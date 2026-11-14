import asyncio
import random

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Network Service")

@app.get("/health")
def health():
    return {"status": "health"}

@app.get("/network/{client_id}")
async def get_network_status(client_id: int):
    await asyncio.sleep(random.uniform(0.05, 0.3)) #simula a latencia de uma consulta a rede

    if random.random() < 0.05:
        raise HTTPException(
            status_code=503,
            detail="Network service unavailable"
        )

    return{
        "client_id": client_id,
        "connection": "online",
        "signal_dbm": -65,
        "latency_ms": 25
    }



