"""Utils file to aid unit testing."""
import json
import requests

def hit_auth_api(payload):
    """Hit the locahost API and return the response dictionary."""
    URL = 'http://localhost:8000/api/auth/login/'

    response = requests.post(
        URL,
        data=payload
    )

    return json.loads(response.text)
