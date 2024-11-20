from fastapi import APIRouter, HTTPException
from app.services import process_qr_code

router = APIRouter()

@router.post("/scan")
def scan_qr(image_data: dict):
    try:
        result = process_qr_code(image_data.get("image"))
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def setup_routes(app):
    app.include_router(router)
