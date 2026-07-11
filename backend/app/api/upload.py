from fastapi import APIRouter, File, UploadFile
from ..services.upload_service import handle_upload, UploadError
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Receive an uploaded file, validate it, and return its metadata.
    """
    try:
        file_info = handle_upload(file)
    except UploadError as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "message": e.message,
                "errors": {"detail": e.message},
            },
        )
    # Sukses
    return {
        "success": True,
        "message": "File uploaded successfully.",
        "data": file_info,
    }