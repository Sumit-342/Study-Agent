from fastapi import FastAPI 
from app.api import health,upload

app = FastAPI()


app.include_router(health.router)
app.include_router(upload.router)