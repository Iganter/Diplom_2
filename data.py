from urls import Urls


class Endpoints:
    REGISTER = f'{Urls.BASE_URL}/api/auth/register'
    LOGIN = f'{Urls.BASE_URL}/api/auth/login'
    USER = f'{Urls.BASE_URL}/api/auth/user'
    ORDERS = f'{Urls.BASE_URL}/api/orders'
    INGREDIENTS = f'{Urls.BASE_URL}/api/ingredients'


class StatusCodes:
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    INTERNAL_ERROR = 500


class ResponseMessages:
    USER_ALREADY_EXISTS = 'User already exists'
    MISSING_REG_FIELDS = 'Email, password and name are required fields'
    LOGIN_INVALID_CREDS = 'email or password are incorrect'
    NO_INGREDIENTS = 'Ingredient ids must be provided'


class TestData:
    INVALID_LOGIN_CREDENTIALS = [
        ("wrong@example.com", "Password123!"),
        ("", "")
    ]
