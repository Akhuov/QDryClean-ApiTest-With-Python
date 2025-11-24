import allure
import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("GET {path}")
    def get(self, path, **kwargs):
        return requests.get(self.base_url + path, **kwargs)

    @allure.step("POST {path}")
    def post(self, path, json=None, **kwargs):
        return requests.post(self.base_url + path, json=json, **kwargs)

    @allure.step("PUT {path}")
    def put(self, path, json=None, **kwargs):
        return requests.post(self.base_url + path, json=json, **kwargs)