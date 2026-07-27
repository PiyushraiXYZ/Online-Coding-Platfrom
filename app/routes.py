from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.database import get_db
from app.models import (
    Problem,
    TestSession,
    TestSessionQuestion
)

from app.schemas import (
    CodeRequest,
    SubmissionRequest
)

from app.judge import judge_submission
from app.docker_executor import execute_python_docker

router = APIRouter()

_LAST_EXECUTED_CODE = {"code": "", "language": "python"}


def store_executed_code(code, language):
    _LAST_EXECUTED_CODE["code"] = code
    _LAST_EXECUTED_CODE["language"] = language


def resolve_submission_payload(payload):
    problem_id = payload.get("problem_id")
    language = payload.get("language") or _LAST_EXECUTED_CODE["language"]
    code = payload.get("code") or _LAST_EXECUTED_CODE["code"]

    if problem_id is None:
        raise HTTPException(status_code=422, detail="Expected problem_id")

    pid = int(problem_id)

    # Fallback: if no code provided, try the built-in solutions list
    if not code:
        try:
            from app import solutions as built_solutions

            for s in built_solutions.SOLUTIONS:
                if s.get("problem_id") == pid and s.get("language") == language:
                    code = s.get("code")
                    break
        except Exception:
            # If anything fails, keep code as None to trigger the error below
            pass

    if not code:
        raise HTTPException(status_code=422, detail="No code available to submit")

    return pid, str(language), str(code)


# =====================================
# Home
# =====================================

@router.get("/")
def home():
    return {
        "message": "Online Coding Platform API Running"
    }


# =====================================
# Health Check
# =====================================

@router.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "online-coding-platform"
    }



# =====================================
# Start Random Test
# =====================================

@router.post("/start-test")
def start_test(
    db: Session = Depends(get_db)
):

    session = TestSession(
        total_questions=3,
        score=0
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    questions = (
        db.query(Problem)
        .order_by(func.random())
        .limit(3)
        .all()
    )

    for question in questions:

        session_question = TestSessionQuestion(
            session_id=session.id,
            problem_id=question.id
        )

        db.add(session_question)

    db.commit()

    return {
        "session_id": session.id,
        "total_questions": len(questions),
        "questions": [
            {
                "id": q.id,
                "title": q.title,
                "description": q.description,
                "difficulty": q.difficulty,
                "sample_input": q.sample_input,
                "sample_output": q.sample_output
            }
            for q in questions
        ]
    }


# =====================================
# Get Existing Test
# =====================================

@router.get("/test/{session_id}")
def get_test(
    session_id: int,
    db: Session = Depends(get_db)
):

    mappings = (
        db.query(TestSessionQuestion)
        .filter(
            TestSessionQuestion.session_id == session_id
        )
        .all()
    )

    questions = []

    for mapping in mappings:

        problem = (
            db.query(Problem)
            .filter(
                Problem.id == mapping.problem_id
            )
            .first()
        )

        if problem:

            questions.append({
                "id": problem.id,
                "title": problem.title,
                "description": problem.description,
                "difficulty": problem.difficulty,
                "sample_input": problem.sample_input,
                "sample_output": problem.sample_output
            })

    return {
        "session_id": session_id,
        "questions": questions
    }


# =====================================
# Execute Code
# =====================================

@router.get("/execute")
def execute_code_get():
    return {
        "message": "Use POST /execute with {\"language\": \"python\", \"code\": \"...\", \"input_data\": \"\"}" 
    }


@router.post("/execute")
def execute_code(
    request: CodeRequest
):

    output = execute_python_docker(
        request.code,
        request.input_data
    )

    store_executed_code(request.code, request.language)

    return {
        "output": output
    }


# =====================================
# Submit Solution
# =====================================

@router.get("/submit")
def submit_code_get():
    return {
        "message": "Use POST /submit with {\"language\": \"python\", \"code\": \"...\"}" 
    }


@router.post("/submit")
async def submit_code(request: Request):
    try:
        payload = await request.json()
    except Exception:
        payload = {}

    problem_id, language, code = resolve_submission_payload(payload)

    result = judge_submission(problem_id, code)

    store_executed_code(code, language)

    return result