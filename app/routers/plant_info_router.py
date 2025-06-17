# app/routers/plant_info_router.py

from fastapi import APIRouter, HTTPException
from app.services.plant_info_service import load_plant_info

router = APIRouter(tags=["Plant Info"])

@router.get("/api/plant-info")
def get_plant_info(plant_type: str = None):
    info = load_plant_info(plant_type)
    if not info:
        raise HTTPException(status_code=404, detail="Informații despre plantă negăsite.")
    return info
