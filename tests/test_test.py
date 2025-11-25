from utils.allure_utils import attach_response


def test_test(logged_client):
    client = logged_client

    payload = {
        "firstName": "string",
        "lastName": "string",
        "phoneNumber": "1",
        "additionalPhoneNumber": "string",
        "points": 0
    }

    # response = client.get(f"/Users/1")
    response = client.post("/Customers/CreateCustomer", payload)

    assert response.status_code == 201
    assert response.json() != []
    attach_response(response)