from fastapi import APIRouter
from app.services.buffer import get_buffer_status, flush_buffer

router = APIRouter(prefix="/api/buffer", tags=["buffer"])

@router.get("/status")
def buffer_status():
    return get_buffer_status()

@router.post("/flush")
def buffer_flush():
    return flush_buffer()
