import os
import pytest
from core.api_client import ApiClient
from dotenv import load_dotenv


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
    response = client.post("/Auth", payload)

    assert response.status_code == 200, response.text
    assert response.json()["token"] is not None, "response is None"

    return client
