import pytest
from pathlib import Path
import os
import allure
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


@pytest.fixture(scope = "session")
def base_url():
    try:
        with open("test/url.txt", "r") as file:
            base_url = file.read().strip()

            if not base_url:
                pytest.fail("Файл url.txt пуст!")

            return base_url
        
    except FileNotFoundError:
        pytest.fail("Файл url.txt не найден!")

@pytest.fixture
def check_status():
    """Простая фикстура для проверки статус-кода"""
    def _check(response, expected):
        with allure.step(f"Проверка статус-кода: ожидается {expected}"):
            actual = response.status_code
            assert actual == expected, f"Статус {actual} != {expected}"
            allure.attach(f"✅ Статус {actual} соответствует ожидаемому", 
                         name="Результат")
    return _check
