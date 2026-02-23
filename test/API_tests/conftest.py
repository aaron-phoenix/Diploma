import pytest
@pytest.fixture(scope = "session")
def api_token():
    try:
        with open("test/token.txt", "r") as file:
            token = file.read().strip()

            if not token:
                pytest.fail("Файл token.txt пуст!")

            return token
        
    except FileNotFoundError:
        pytest.fail("Файл token.txt не найден!")


@pytest.fixture(scope = "session")
def api_headers(api_token):
    return {
        "X-API-KEY" : api_token,
        "Content-Type" : "application/json"
    }
