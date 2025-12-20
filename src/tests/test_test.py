from utils.allure_utils import attach_response


def test_test(logged_client):
    client = logged_client

    payload = {
        "firstName": "string",
        "lastName": "string",
        "phoneNumber": "11",
        "additionalPhoneNumber": "test1",
        "points": 0
    }

    response = client.post("/customers", payload)

    if response.json():
        print(response.json())
        attach_response(response)

    assert response.status_code == 201
    assert response.json() != []
