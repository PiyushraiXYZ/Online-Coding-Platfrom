from app.database import SessionLocal
from app.models import TestCase, Submission
from app.docker_executor import execute_python_docker


def judge_submission(problem_id, code):

    db = SessionLocal()

    try:

        test_cases = db.query(TestCase).filter(
            TestCase.problem_id == problem_id
        ).all()

        passed = 0

        for tc in test_cases:

            output = execute_python_docker(
                code,
                tc.input_data
            )

            if output.strip() == tc.expected_output.strip():
                passed += 1

        total = len(test_cases)

        if total == 0:
            score = 0
            verdict = "No Test Cases"
        else:
            score = int((passed / total) * 100)

            if passed == total:
                verdict = "Accepted"
            elif passed > 0:
                verdict = "Partially Accepted"
            else:
                verdict = "Wrong Answer"

        submission = Submission(
            problem_id=problem_id,
            language="python",
            code=code,
            verdict=verdict,
            score=score
        )

        db.add(submission)
        db.commit()

        return {
            "verdict": verdict,
            "score": score,
            "passed": passed,
            "total": total
        }

    finally:
        db.close()