"""
API endpoint for file upload.
"""

from fastapi import APIRouter, File, UploadFile # type: ignore
from ..services.upload_service import handle_upload

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Receive an uploaded file, validate it, and return its metadata.
    The file is not stored permanently.
    """
    file_info = handle_upload(file)
    return {
        "success": True,
        "message": "File uploaded successfully.",
        "file": file_info,
    }