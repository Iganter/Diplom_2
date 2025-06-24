import allure
import requests

from data import Endpoints


class ApiClient:
    def __init__(self, timeout: float = 5.0):
        self.session = requests.Session()
        self.timeout = timeout

    @allure.step("Register user")
    def register(self, user_data: dict) -> requests.Response:
        url = Endpoints.REGISTER
        return self.session.post(url, json=user_data, timeout=self.timeout)

    @allure.step("Login user")
    def login(self, email: str, password: str) -> requests.Response:
        url = Endpoints.LOGIN
        return self.session.post(url, json={"email": email, "password": password}, timeout=self.timeout)

    @allure.step("Delete user")
    def delete_user(self, token: str) -> requests.Response:
        url = Endpoints.USER
        headers = {"Authorization": f"Bearer {token}"}
        return self.session.delete(url, headers=headers, timeout=self.timeout)

    @allure.step("Get ingredients list")
    def get_ingredients(self) -> requests.Response:
        url = Endpoints.INGREDIENTS
        return self.session.get(url, timeout=self.timeout)

    @allure.step("Create order")
    def create_order(self, ingredients: list, token: str = None) -> requests.Response:
        url = Endpoints.ORDERS
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return self.session.post(url, json={"ingredients": ingredients}, headers=headers, timeout=self.timeout)
