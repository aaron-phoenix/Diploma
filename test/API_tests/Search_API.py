import requests
from requests import Response
import allure

@allure.epic("API-тесты")
class Search_API:

    def __init__(self, url) -> None:
        self.url = url
    
        """
        Конструктор класса Search_API.

        :param driver: url
        """

    @allure.step("API-запрос на получение списка фильмов онлайн-кинотеатра Кинопоиск")
    def get_films(self, api_headers) -> Response:
        """Отправляет get-запрос.
        Возвращает полный ответ со списком фильмов онлайн-кинотеатра Кинопоиск.
        :param my_headers: словарь со списком необходимых заголовков(токен, content-type)
        """
        resp = requests.get(self.url, headers = api_headers)
        return resp
    
    @allure.step("API-запрос на получение списка фильмов с неправильным методом post")
    def get_films_post(self, api_headers) -> Response:
        """Отправляет get-запрос.
        Возвращает сообщение об ошибке.
        :param my_headers: словарь со списком необходимых заголовков(токен, content-type)
        """
        resp = requests.post(self.url, headers = api_headers)
        return resp
    
    @allure.step("API-запрос на получение фильма по id")
    def get_film_id(self, film_id, api_headers) -> Response:
        """
        Отправляет get-запрос.
        Возвращает полный ответ с описанием фильма по заданному id.
        В случае неправильного или несуществующего id возвращает сообщение об ошибке.
        
        :param my_headers: словарь со списком необходимых заголовков(токен, content-type)
        :param film_id: id фильма
        """
        resp = requests.get(url = f"{self.url}/{film_id}", headers = api_headers)
        return resp
    
    @allure.step("Проверка статус-кода ответа")
    def assert_status_code(self, response, expected_code, message="") -> bool:
        """
        Проверяет статус-код и логирует в Allure.
        При несовпадении статус кода возвращает сообщение об ошибке
        """
        actual = response.status_code
        
        allure.attach(
            f"Ожидаемый статус: {expected_code}\nФактический статус: {actual}\n{message}",
            name="Результат проверки статуса",
            attachment_type=allure.attachment_type.TEXT
        )
        assert actual == expected_code, \
            f"❌ Статус {actual} != {expected_code}. {message}"
        
        return True
