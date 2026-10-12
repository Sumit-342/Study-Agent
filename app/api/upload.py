from fastapi import UploadFile , File ,APIRouter
import os 
import fitz
from app.services.syllabus_parser import parse_syllabus
from app.db.crud import save_syllabus

router = APIRouter()

UPLOAD_DIR = "data/uploads"



@router.post("/upload")
async def upload_file(file:UploadFile = File(...)):

    #folder check 
    os.makedirs(UPLOAD_DIR,exist_ok=True)

    # file path
    file_path = os.path.join(UPLOAD_DIR,file.filename)

    # save
    with open(file_path,"wb") as f :
        content = await file.read()
        f.write(content)

    # open

    doc = fitz.open(file_path)
    text = ""

    for page in doc :
        text+=page.get_text()
    doc.close()



    #  Parse
    syllabus_data = parse_syllabus(text)

    #  Save
    saved = save_syllabus(
        subject=syllabus_data.subject,
        units=[u.model_dump() for u in syllabus_data.units],
        filename=file.filename,
    )

    return {
        "saved": True,
        "id": saved.id,
        "subject": saved.subject,
        "units_count": len(saved.units),
    }

