from app.db.database import Base, engine
from app.db import models  

# Tables create
Base.metadata.create_all(bind=engine)

# Phir test
from app.db.crud import save_syllabus, get_all_syllabus

result = save_syllabus(
    subject="C++",
    units=[{"unit": 1, "title": "Basics", "topics": ["Variables", "Loops"]}],
    filename="test.pdf",
)

print("ID:", result.id)
print("Subject:", result.subject)

all_syl = get_all_syllabus()
print("Total:", len(all_syl))