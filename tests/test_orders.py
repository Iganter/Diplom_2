import allure

from data import StatusCodes, ResponseMessages


@allure.story("Создание заказа")
class TestOrders:

    @allure.title("С авторизацией и ингредиентами → 200")
    def test_order_with_auth(self, api_client, registered_user):
        _, token = registered_user
        ings = api_client.get_ingredients().json()["data"]
        ids = [ings[0]["_id"], ings[1]["_id"]]
        resp = api_client.create_order(ids, token=token)
        assert resp.status_code == StatusCodes.OK
        body = resp.json()
        assert body["success"] is True
        order_num = body["order"]["number"]
        assert isinstance(order_num, int) and order_num > 0

    @allure.title("Без авторизации → 401")
    def test_order_without_auth(self, api_client):
        ings = api_client.get_ingredients().json()["data"]
        resp = api_client.create_order([ings[0]["_id"]])
        assert resp.status_code == StatusCodes.UNAUTHORIZED

    @allure.title("Без ингредиентов → 400")
    def test_order_no_ingredients(self, api_client, registered_user):
        _, token = registered_user
        resp = api_client.create_order([], token=token)
        assert resp.status_code == StatusCodes.BAD_REQUEST
        assert resp.json()["message"] == ResponseMessages.NO_INGREDIENTS

    @allure.title("С неверным хешем ингредиентов → 500")
    def test_order_invalid_hash(self, api_client, registered_user):
        _, token = registered_user
        resp = api_client.create_order(["invalid_hash"], token=token)
        assert resp.status_code == StatusCodes.INTERNAL_ERROR
