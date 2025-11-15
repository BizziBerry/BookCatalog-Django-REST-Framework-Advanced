import requests
import json

response = requests.post(
    'http://127.0.0.1:8000/api/categories/',
    json={'name': 'Тест', 'description': 'Тест'},
    timeout=5
)
print('Status:', response.status_code)
print('Text:', response.text)