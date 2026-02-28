from API_tests.Search_API import Search_API
from API_tests.conftest import api_headers, api_token, base_url
import allure
import pytest


@pytest.mark.api
@pytest.mark.positive
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоик")
@allure.title("Получение списка фильмов онлайн-кинотеатра Кинопоиск")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках API-запросов на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("API-тестирование")
def test_get_films_positive(api_headers, base_url):
    """Тест проверяет адекватное поведение системы при позитивных get-запросах на получение списка фильмов онлайн-кинотеатра Кинопоиск.
    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param my_headers: словарь с необходимыми заголовками.
    :param base_url: базовый url
    """
    api = Search_API(base_url)
    with allure.step("API-запрос на получение списка фильмов онлайн-кинотеатра Кинопоиск"):
        resp = api.get_films(api_headers)
    
    with allure.step("Проверка статус-кода ответа"):
        api.assert_status_code(resp, 200)
    body = resp.json()
    assert len(body) > 0

@pytest.mark.api
@pytest.mark.positive
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоик")
@allure.title("Получение фильма по id")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках API-запросов на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("API-тестирование")
def test_get_film_id_positive(api_headers, base_url):
    """
    Тест проверяет адекватное поведение системы при позитивных get-запросах на получение фильма по id.
    :param film_id: id фильма
    :param my_headers: словарь с необходимыми заголовками.
    :param base_url: базовый url
    """
    api = Search_API(base_url)
    with allure.step("API-запрос на получение фильма по id"):
        film_id = 464963
        headers = api_headers
        resp = api.get_film_id(film_id, headers)
        assert resp.json()["nameRu"] == 'Игра престолов'

        with allure.step("Проверка статус-кода ответа"):
            api.assert_status_code(resp, 200)

@pytest.mark.api
# @pytest.mark.negative
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоик")
@allure.title("Получение фильма с id=0")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках API-запросов на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("API-тестирование")
def test_get_film_id_negative(api_headers, base_url):
    """
    Тест проверяет адекватное поведение системы при негативных get-запросах на получение фильма с несуществующим id.
    :param film_id: id фильма
    :param my_headers: словарь с необходимыми заголовками.
    :param base_url: базовый url
    """
    api = Search_API(base_url)
    with allure.step("API-запрос на получение фильма по id"):
        film_id = 0
        headers = api_headers
        resp = api.get_film_id(film_id, headers)
        assert resp.json()["message"] == "kinopoisk id should be more than or equal to 1"

        with allure.step("Проверка статус-кода ответа"):
            api.assert_status_code(resp, 400)

@pytest.mark.api
@pytest.mark.negative
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоик")
@allure.title("Получение фильма с id со строковым значением")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках API-запросов на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("API-тестирование")
def test_get_film_id_str_negative(api_headers, base_url):
    """
    Тест проверяет адекватное поведение системы при негативных get-запросах на получение фильма с id со строковым значением.
    :param film_id: id фильма
    :param my_headers: словарь с необходимыми заголовками.
    :param base_url: базовый url
    """
    api = Search_API(base_url)
    with allure.step("API-запрос на получение фильма по id"):
        film_id = "game"
        headers = api_headers
        resp = api.get_film_id(film_id, headers)
        expected = "Method parameter 'kinopoiskFilmId': Failed to convert value of type 'java.lang.String' to required type 'int'; For input string: \"game\""
        assert resp.json()["message"] == expected

        with allure.step("Проверка статус-кода ответа"):
            api.assert_status_code(resp, 400)

@pytest.mark.api
@pytest.mark.negative
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоик")
@allure.title("Получение списка фильмов с неправильным методом post")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках API-запросов на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("API-тестирование")
def test_get_films_negative(api_headers, base_url):
    """
    Тест проверяет адекватное поведение системы при негативных get-запросах на получение фильма неправильным методом post.
    :param my_headers: словарь с необходимыми заголовками.
    :param base_url: базовый url
    """
    api = Search_API(base_url)
    with allure.step("API-запрос на получение списка фильмов с неправильным методом post"):
        resp = api.get_films_post(api_headers)
        assert resp.json()["message"] == "something went wrong."

        with allure.step("Проверка статус-кода ответа"):
            api.assert_status_code(resp, 500)