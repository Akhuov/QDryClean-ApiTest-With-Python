import os
import pytest
from playwright.sync_api import Browser, Page
from ui.components.navigation import Navigation


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
def navigation(logged_page: Page):
    nav = Navigation(logged_page)
    yield nav
    #post condition -> Close browser
    logged_page.close()