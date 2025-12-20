import os
import pytest
from dotenv import load_dotenv
from core.api_client import ApiClient
from playwright.sync_api import Browser, Page


@pytest.fixture(scope="session")
def settings():
    load_dotenv()
    back_end_url = os.getenv('BACK_END_URL')
    front_end_url = os.getenv('FRONT_END_URL')
    login = os.getenv('TEST_LOGIN')
    password = os.getenv('TEST_PASSWORD')
    state_path = os.getenv('STORAGE_STATE_PATH')

    return dict(back_end_url=back_end_url, login=login,
                password=password, state_path=state_path,
                front_end_url=front_end_url)

@pytest.fixture
def perform_login(settings):
    def _perform_login(page: Page):

        page.get_by_role("textbox", name="Логин").fill(settings["login"])
        page.get_by_role("textbox", name="Пароль").fill(settings["password"])
        page.get_by_role("button", name="Войти").click()

    return _perform_login

@pytest.fixture #(scope="session")
def logged_page(browser: Browser, settings, perform_login):
    base_url = settings['front_end_url']
    # To keep session active
    storage_path = settings["state_path"]
    if not os.path.exists(storage_path):
        os.makedirs(os.path.dirname(storage_path), exist_ok=True)
        with open(storage_path, "w") as f:
            f.write("{}")

    context = browser.new_context(storage_state=storage_path)
    page = context.new_page()

    page.goto(base_url, timeout=60000)


    # if already logged-in, return the page
    if page.url == f"{base_url}/users":
        return page

    # page.set_viewport_size({"width": 1920, "height": 1080})
    # page.set_default_timeout(60_000)
    # page.set_default_navigation_timeout(60_000)

    perform_login(page)

    # save storage state
    context.storage_state(path=storage_path)

    return page

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
