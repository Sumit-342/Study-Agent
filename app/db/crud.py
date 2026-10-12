from app.db.database import SessionLocal
from app.db.models import Syllabus


def save_syllabus(subject: str, units: list, filename: str, user_id: str = "default"):
    db = SessionLocal()
    try:
        syllabus = Syllabus(
            user_id=user_id,
            subject=subject,
            units=units,
            source_filename=filename,
        )
        db.add(syllabus)
        db.commit()
        db.refresh(syllabus)
        return syllabus
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def get_syllabus_by_id(syllabus_id: int):
    db = SessionLocal()
    try:
        return db.query(Syllabus).filter(Syllabus.id == syllabus_id).first()
    finally:
        db.close()


def get_all_syllabus(user_id: str = "default"):
    db = SessionLocal()
    try:
        return db.query(Syllabus).filter(Syllabus.user_id == user_id).all()
    finally:
        db.close()