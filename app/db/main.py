from fastapi import FastAPI
from app.api import health, upload
from app.db.database import Base, engine
from app.db import models


# Tables create
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Study Agent")

app.include_router(health.router)
app.include_router(upload.router)
