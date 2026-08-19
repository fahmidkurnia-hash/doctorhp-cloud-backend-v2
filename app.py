import os
from typing import Optional, Dict, Any

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field

app = FastAPI(
    title="DoctorHP Cloud Backend V2",
    version="2.0.0"
)

security = HTTPBearer(auto_error=False)


class Unit(BaseModel):
    brand: str
    model: str
    revision: Optional[str] = None


class AnalyzeRequest(BaseModel):
    provider: str = Field(pattern="^(ChatGPT)$")
    unit: Unit
    complaint: str
    measurements: Dict[str, Any] = {}
    voltage_reference: Dict[str, Any] = {}
    boardview_context: Dict[str, Any] = {}


def auth(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)
):
    expected = os.getenv("DOCTORHP_SERVER_TOKEN", "").strip()

    if not expected:
        raise HTTPException(
            status_code=503,
            detail="DOCTORHP_SERVER_TOKEN not configured"
        )

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    if credentials.credentials.strip() != expected:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return credentials.credentials


@app.get("/")
async def root():
    return {
        "ok": True,
        "service": "DoctorHP Cloud Backend V2"
    }


@app.get("/health")
async def health():
    return {
        "ok": True,
        "service": "DoctorHP Cloud Backend V2",
        "version": "2.0.0"
    }


@app.post("/v1/doctorhp/analyze")
async def analyze(
    r: AnalyzeRequest,
    _token: str = Depends(auth)
):
    return {
        "ok": True,
        "message": "Authentication berhasil",
        "provider": r.provider,
        "unit": {
            "brand": r.unit.brand,
            "model": r.unit.model,
            "revision": r.unit.revision
        },
        "complaint": r.complaint
    }
