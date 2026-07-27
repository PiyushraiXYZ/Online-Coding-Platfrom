from app.database import SessionLocal
from app.models import Solution
from app.solutions import SOLUTIONS

db = SessionLocal()

for s in SOLUTIONS:

    db.add(
        Solution(
            
            language=s["language"],
            code=s["code"],
            input=s["input"]
        )
    )

db.commit()

print("Solutions Inserted")



