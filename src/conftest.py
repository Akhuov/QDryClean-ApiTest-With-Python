import os
import pytest
from dotenv import load_dotenv
from core.api_client import ApiClient


@pytest.fixture
def logged_client():
    load_dotenv()

    base_url = os.getenv('BASE_URL')
    login = os.getenv('TEST_LOGIN')
    password = os.getenv('TEST_PASSWORD')
    
    payload = {
        "logIn": login,
        "password": password
    }

    client = ApiClient(base_url)
    response = client.post("/auth", payload)

    assert response.status_code == 200, response.text
    assert response.json()["token"] is not None, "response is None"

    client.set_token(response.json()["token"])

    return client
