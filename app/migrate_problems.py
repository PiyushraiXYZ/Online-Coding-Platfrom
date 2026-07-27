from app.models import Problem, TestCase
from app.problems import PROBLEMS


def migrate_problems(db):
    try:
        for p in PROBLEMS:
            existing = db.query(Problem).filter(
                Problem.id == p["id"]
            ).first()

            if existing:
                print(f"Problem {p['id']} already exists")
                continue

            problem = Problem(
                id=p["id"],
                title=p["title"],
                description=p["description"],
                difficulty=p["level"],
                sample_input=(
                    p["test_cases"][0]["input"]
                    if len(p["test_cases"]) > 0
                    else ""
                ),
                sample_output=(
                    p["test_cases"][0]["output"]
                    if len(p["test_cases"]) > 0
                    else ""
                )
            )

            db.add(problem)
            db.flush()

            for tc in p["test_cases"]:
                testcase = TestCase(
                    problem_id=p["id"],
                    input_data=tc["input"],
                    expected_output=tc["output"],
                    is_hidden=False
                )
                db.add(testcase)

            db.commit()
            print(f"Inserted Problem {p['id']}")

        print("Migration Completed Successfully")

    except Exception as e:
        db.rollback()
        print("Error:", e)
        raise