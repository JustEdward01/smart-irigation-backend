from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.settings import SystemConfig
from app.services.settings import get_config, set_config, run_self_test, get_system_info

router = APIRouter(prefix="/api/settings", tags=["settings"])

@router.get("/export-config", response_model=SystemConfig)
def export_config():
    return get_config()

@router.post("/import-config")
async def import_config(file: UploadFile = File(...)):
    content = await file.read()
    try:
        config = SystemConfig.parse_raw(content)
        set_config(config)
        return {"message": "Configurația a fost importată cu succes"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Fișier invalid: {e}")

@router.post("/self-test")
def post_self_test():
    results = run_self_test()
    return results

@router.get("/system-info")
def get_sysinfo():
    return get_system_info()
