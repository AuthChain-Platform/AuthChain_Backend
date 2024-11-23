from fastapi import APIRouter, HTTPException, UploadFile
from app.services import process_qr_code

router = APIRouter()

@router.post("/scan")
async def scan_qr(image: UploadFile = None):
    try:
        if image:
            image_bytes = await image.read()
            result = process_qr_code(image_bytes=image_bytes)
        else:
            result = process_qr_code()

        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])

        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def setup_routes(app):
    app.include_router(router)
