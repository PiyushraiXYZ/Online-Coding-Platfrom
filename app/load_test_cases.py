from app.database import SessionLocal
from app.problems import PROBLEMS
from app.models import TestCase

db = SessionLocal()

try:
    count = 0

    for problem in PROBLEMS:

        problem_id = problem["id"]

        for tc in problem["test_cases"]:

            testcase = TestCase(
                problem_id=problem_id,
                input_data=tc["input"],
                expected_output=tc["output"],
                is_hidden=False
            )

            db.add(testcase)
            count += 1

    db.commit()

    print(f"{count} test cases inserted successfully")

except Exception as e:
    db.rollback()
    print("Error:", e)

finally:
    db.close()