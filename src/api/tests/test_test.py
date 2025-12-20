from core.allure.allure_utils import attach_response
from core.utils.faker_utils import generate_random_text


def test_test(logged_client):
    client = logged_client

    payload = {
        "firstName": "string",
        "lastName": "string",
        "phoneNumber": generate_random_text('test'),
        "additionalPhoneNumber": generate_random_text('test'),
        "points": 0
    }

    response = client.post("/customers", payload)

    if response.json():
        print(response.json())
        attach_response(response)

    assert response.status_code == 201
    assert response.json() != []
