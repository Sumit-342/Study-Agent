from fastapi import UploadFile , File ,APIRouter
import os 
import fitz

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



    return{"text" : text}

