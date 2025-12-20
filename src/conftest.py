import os
import pytest
from dotenv import load_dotenv

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