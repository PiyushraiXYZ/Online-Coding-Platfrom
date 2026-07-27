import unittest

from app.routes import resolve_submission_payload, store_executed_code


class ResolveSubmissionPayloadTests(unittest.TestCase):
    def setUp(self):
        store_executed_code("", "python")

    def test_uses_explicit_code_from_payload(self):
        payload = {"problem_id": 1, "language": "python", "code": "print('explicit')"}

        problem_id, language, code = resolve_submission_payload(payload)

        self.assertEqual(problem_id, 1)
        self.assertEqual(language, "python")
        self.assertEqual(code, "print('explicit')")

    def test_falls_back_to_last_executed_code(self):
        store_executed_code("print('from execute')", "python")
        payload = {"problem_id": 2, "language": "python"}

        problem_id, language, code = resolve_submission_payload(payload)

        self.assertEqual(problem_id, 2)
        self.assertEqual(language, "python")
        self.assertEqual(code, "print('from execute')")


if __name__ == "__main__":
    unittest.main()
