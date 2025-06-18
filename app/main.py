from dotenv import load_dotenv
load_dotenv()

import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.db_service import supabase

# Import router health separat
from app.routers.health import router as health_router

# Import restul routerelor
from app.routers import (
    sensor_data_router,
    plant_info_router,
    predict_router,
    diagnose_photo_router,
    manual_water_router,
    system_status_router,
    diagnostic_logs_router,
    history_router,
    settings,
    buffer,
    logs,
    wifi,
)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

API_SECRET = os.getenv("API_SECRET", "supersecret123")

app = FastAPI()

# Middleware CORS (exemplu)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # sau ["*"] pentru testare
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routerul health
app.include_router(health_router)

# Include restul routerelor
app.include_router(settings.router)
app.include_router(buffer.router)
app.include_router(logs.router)
app.include_router(wifi.router)
app.include_router(sensor_data_router.router)
app.include_router(plant_info_router.router)
app.include_router(predict_router.router)
app.include_router(diagnose_photo_router.router)
app.include_router(manual_water_router.router)
app.include_router(system_status_router.router)
app.include_router(diagnostic_logs_router.router)
app.include_router(history_router.router)
