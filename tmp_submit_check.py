import requests

payload = {
    "problem_id": 1,
    "language": "python",
    "code": "print('Hello from API')"
}

resp = requests.post('http://localhost:9000/submit', json=payload, timeout=15)
print(resp.status_code)
print(resp.text)
