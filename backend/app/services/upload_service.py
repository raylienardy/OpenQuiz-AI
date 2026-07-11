"""
Service layer for handling file uploads.
"""

from fastapi import UploadFile, HTTPException # type: ignore
from ..utils.file_utils import validate_file


def handle_upload(file: UploadFile) -> dict:
    """
    Validate the uploaded file and return its metadata.

    Args:
        file: The uploaded file.

    Returns:
        dict: Metadata containing filename, content_type, and size.

    Raises:
        HTTPException: If validation fails or an unexpected error occurs.
    """
    if not file:
        raise HTTPException(status_code=400, detail="No file provided.")

    # Validate the file
    try:
        validate_file(file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Extract metadata (file is kept in memory; no disk storage)
    filename = file.filename
    content_type = file.content_type or "application/octet-stream"
    size = file.size if file.size is not None else 0

    return {
        "filename": filename,
        "content_type": content_type,
        "size": size,
    }