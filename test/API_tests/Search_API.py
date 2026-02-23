import requests
import allure
import pytest
"""
Токен для авторизации API-запросов.
Словарь со списком необходимых заголовков.
"""
# token = "ed4d4651-cd8e-453b-b3e5-a3e50b64de6c"
# my_headers = {
#     "X-API-KEY": token,
#     "Content-Type": "application/json"
# }


@allure.epic("API-тесты")
class Search_API:

    def __init__(self, url):
        self.url = url
        """
        Конструктор класса Search_API.

        :param driver: url https://kinopoiskapiunofficial.tech/api/v2.2/ (Сайт онлайн-кинотеатра Кинопоиск)
        """

    @allure.step("API-запрос на получение списка фильмов онлайн-кинотеатра Кинопоиск")
    def get_films(self, api_headers):
        """Отправляет get-запрос.
        Возвращает json со списком фильмов онлайн-кинотеатра Кинопоиск.
        :param my_headers: словарь со списком необходимых заголовков(токен, content-type)
        """
        resp = requests.get(url="https://kinopoiskapiunofficial.tech/api/v2.2/" + f'/films/', headers = api_headers)
        return resp.json()
    
    @allure.step("API-запрос на получение списка фильмов с неправильным методом post")
    def get_films_post(self, api_headers):
        """Отправляет get-запрос.
        Возвращает сообщение об ошибке.
        :param my_headers: словарь со списком необходимых заголовков(токен, content-type)
        """
        resp = requests.post(url="https://kinopoiskapiunofficial.tech/api/v2.2/" + f'/films/', headers = api_headers)
        return resp
    
    @allure.step("API-запрос на получение фильма по id")
    def get_film_id(self, film_id, api_headers):
        """
        Отправляет get-запрос.
        Возвращает json с описанием фильма по заданному id.
        В случае неправильного или несуществующего id возвращает сообщение об ошибке.
        
        :param my_headers: словарь со списком необходимых заголовков(токен, content-type)
        :param film_id: id фильма
        """
        resp = requests.get(url = f"https://kinopoiskapiunofficial.tech/api/v2.2/films/{film_id}", headers = api_headers)
        return resp
    
    @allure.step("Проверка статус-кода ответа")
    def assert_status_code(self, response, expected_code, message=""):
        """Проверяет статус-код и логирует в Allure"""
        actual = response.status_code
        
        allure.attach(
            f"Ожидаемый статус: {expected_code}\nФактический статус: {actual}\n{message}",
            name="Результат проверки статуса",
            attachment_type=allure.attachment_type.TEXT
        )
        
        assert actual == expected_code, \
            f"❌ Статус {actual} != {expected_code}. {message}"
        
        return True
        

    