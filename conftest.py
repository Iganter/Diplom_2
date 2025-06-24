import pytest

from api_client import ApiClient
from helpers import generate_user_data
from data import StatusCodes


@pytest.fixture(scope="session")
def api_client():
    return ApiClient()


@pytest.fixture
def registered_user(api_client):

    user = generate_user_data()
    resp = api_client.register(user)
    assert resp.status_code == StatusCodes.OK, resp.text

    token = resp.json()["accessToken"].split("Bearer ")[1]
    yield user, token

    api_client.delete_user(token)
