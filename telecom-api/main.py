
import os

import httpx
from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Telecom API")

Instrumentator().instrument(app).expose(app)

NETWORK_URL = os.getenv(
    "NETWORK_URL",
    "http://localhost:8001"
)


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/clients/{client_id}/connection")
async def get_connection(client_id: int):
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            response = await client.get(
                f"{NETWORK_URL}/network/{client_id}"
            )

            response.raise_for_status()
            return response.json()

    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="Network service timeout"
        )

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Upstream HTTP error: {exc.response.status_code}"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="Network service connection failed"
        )
