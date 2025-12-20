import pytest
from core.http.api_client import ApiClient


@pytest.fixture
def logged_client(settings):

    payload = {
        "logIn": settings["login"],
        "password": settings["password"],
    }

    client = ApiClient(settings["back_end_url"])
    response = client.post("/auth", payload)

    assert response.status_code == 200, response.text
    assert response.json()["token"] is not None, "response is None"

    client.set_token(response.json()["token"])

    return client