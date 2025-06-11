from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from datetime import datetime
import shutil
import os

# from app.model.utils import load_model_and_predict  # You will create this function

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_image(file: UploadFile = File(...)):
    # Save file to disk
    file_ext = os.path.splitext(file.filename)[1]
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    saved_filename = f"img_{timestamp}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, saved_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run CSRNet model to predict count
    # count = load_model_and_predict(file_path)  # You’ll implement this in utils.py
    count = 42  # Placeholder for now

    # TODO: Store in DB here

    return JSONResponse(content={
        "filename": saved_filename,
        "people_count": count,
        "timestamp": timestamp
    })
