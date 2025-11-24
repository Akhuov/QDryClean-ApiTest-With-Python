from utils.allure_utils import attach_response


def test_test(logged_client):
    client = logged_client

    response = client.get(f"/Users/1")
    assert response.status_code == 200
    assert response.json() != []

    attach_response(response)