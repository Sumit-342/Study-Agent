from sqlalchemy import Column , Integer , String , JSON , DateTime
from datetime import datetime,timezone
from app.db.database import Base


class Syllabus(Base) : 

    __tablename__ = "syllabus" 

    id = Column(Integer,primary_key=True,index= True)
    user_id = Column(String,default="default",index=True)
    subject = Column(JSON,nullable=False)
    units = Column(JSON,nullable=False)
    source_filename = Column(String)
    created_at = Column(DateTime,default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))