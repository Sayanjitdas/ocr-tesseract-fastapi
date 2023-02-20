import shutil
from fastapi import FastAPI,File,UploadFile
import pytesseract

app = FastAPI()

@app.post("/ocr")
def ocr(image: UploadFile = File(...)):
    filePath = f"ocr-images/{image.filename}"
    with open(filePath,"w+b") as buffer:
        shutil.copyfileobj(image.file,buffer)
    return pytesseract.image_to_string(filePath,lang='eng')
