import pytest
import allure

from data import StatusCodes, ResponseMessages, TestData


@allure.story("Авторизация пользователя")
class TestLogin:

    @allure.title("Успешный вход существующего пользователя → 200")
    def test_login_success(self, api_client, registered_user):
        user, _ = registered_user
        resp = api_client.login(user["email"], user["password"])

        assert resp.status_code == StatusCodes.OK
        data = resp.json()
        assert data["success"] is True
        assert data["accessToken"].startswith("Bearer ")

    @allure.title("Вход с неверными данными → 401")
    @pytest.mark.parametrize("email,password", TestData.INVALID_LOGIN_CREDENTIALS)
    def test_login_invalid(self, api_client, email, password):
        resp = api_client.login(email, password)

        assert resp.status_code == StatusCodes.UNAUTHORIZED
        assert resp.json()["message"] == ResponseMessages.LOGIN_INVALID_CREDS
