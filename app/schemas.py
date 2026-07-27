from pydantic import BaseModel
from typing import List

class CodeRequest(BaseModel):
    language: str
    code: str
    input_data: str = ""

class TestCase(BaseModel):
    input: str
    expected_output: str

class SubmitRequest(BaseModel):
    language: str
    code: str
    test_cases: List[TestCase]

class SubmissionRequest(BaseModel):
    problem_id: int
    language: str
    code: str    