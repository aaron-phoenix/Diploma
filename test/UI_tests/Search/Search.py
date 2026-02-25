from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.epic("Поиск")
class Search:
    def __init__(self, driver) -> None:
        self.driver = driver
        """
        Конструктор класса Search.
        :param driver: WebDriver — объект драйвера Selenium.
        """
    @allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск")
    def open_page(self) -> None:
        """
        Открывает страницу онлайн-кинотеатра Кинопоиск.
        Разворачивает окно браузера на максимум.
        """
        self.driver.get("https://hd.kinopoisk.ru")
        self.driver.maximize_window()

    @allure.step("Поиск фильма неавторизованным пользователем")
    def search(self, data, time:int = 10) -> None:
        """
        Находит иконку поиска и кликает на нее.
        Ожидает загрузку поля ввода значений для поиска.
        Вводит значение для поиска в поле ввода.
        :param time: int - значение по умолчанию - 10
        :param data: данные для ввода в поле поиска
        """
        search_button = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-tid='SearchButton']"))
        )
        search_button.click()

        input_field = WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )
        input_field.send_keys(data)

    @allure.step("Проверка результата поиска на латиннице")
    def check_l(self, expected_text, time:int = 15) -> str:
        """
        Проверяет результат поиска на латиннице.
        :param expected_text: ожидаемый результат поиска.
        :param time: int - значение по умолчанию - 10
        """
        waiter = WebDriverWait(self.driver, time)

        waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-tid="SuggestDropdownFooter"]'))
     )
        results = waiter.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.styles_title__BpljK"))
        )
        for result in results:
            if expected_text.lower() in result.text.lower():
                return result.text
        return None
    
    @allure.step("Проверка результата поиска на кириллице")
    def check_k(self, expected_text, time:int = 15) -> str:
        """
        Проверяет результат поиска на кириллице.
        :param expected_text: ожидаемый результат поиска.
        :param time: int - значение по умолчанию - 10
        """
        waiter = WebDriverWait(self.driver, time)

        waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-tid="SuggestDropdownFooter"]'))
     )
        results = waiter.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#suggest-item-0"))
        )
        for result in results:
            if expected_text.lower() in result.text.lower():
                return result.text
        return None
    
    @allure.step("Ожидание результата")
    def waits(self, seconds) -> None:
        """
        Ожидает загрузки страницы после авторизации.
        Ожидаемый результат - загрузка html-тега body.
        :param seconds: время ожидания в секундах
        
        """
        waiter = WebDriverWait(self.driver, seconds)

        waiter.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "body"))
    )
   