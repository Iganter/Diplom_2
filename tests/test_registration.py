import pytest
import allure

from data import StatusCodes, ResponseMessages
from helpers import generate_user_data


@allure.story("Регистрация пользователя")
class TestRegistration:

    @allure.title("Уникальный пользователь → 200 OK")
    def test_register_unique(self, api_client):
        user = generate_user_data()
        resp = api_client.register(user)
        assert resp.status_code == StatusCodes.OK
        assert resp.json()["success"] is True

    @allure.title("Повторная регистрация существующего пользователя → 403")
    def test_register_existing(self, api_client, registered_user):
        user, _ = registered_user
        resp = api_client.register(user)
        assert resp.status_code == StatusCodes.FORBIDDEN
        assert resp.json()["message"] == ResponseMessages.USER_ALREADY_EXISTS

    @allure.title("Регистрация без обязательного поля → 403")
    @pytest.mark.parametrize("missing", ["email", "password", "name"])
    def test_register_missing_field(self, api_client, missing):
        user = generate_user_data()
        user.pop(missing)
        resp = api_client.register(user)
        assert resp.status_code == StatusCodes.FORBIDDEN
        assert resp.json()["message"] == ResponseMessages.MISSING_REG_FIELDS
