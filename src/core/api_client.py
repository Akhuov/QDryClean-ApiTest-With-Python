import allure
import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()  # хранит токен и общие заголовки
        self.access_token = None

    def set_token(self, token: str):
        self.access_token = token
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    @allure.step("GET {path}")
    def get(self, path, **kwargs):
        return self.session.get(self.base_url + path, **kwargs)

    @allure.step("POST {path}")
    def post(self, path, json=None, **kwargs):
        return self.session.post(self.base_url + path, json=json, **kwargs)

    @allure.step("PUT {path}")
    def put(self, path, json=None, **kwargs):
        return self.session.put(self.base_url + path, json=json, **kwargs)
