from selenium import webdriver
from UI_tests.Login.Login import Login
from UI_tests.Search.Search import Search
import pytest
from time import sleep
import allure
@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тестирование Онлайн-кинотеатра Кинопоик")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках формы авторизации и поиска на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Онлайн-кинотеатр Кинопоиск")

def test_login_positive(driver):
    """
    Тест проверяет авторизацию по существующему номеру телефона.
    :param driver: WebDriver — объект драйвера Selenium.
    :param number: номер телефона пользователя.
    :param seconds: время ожидания в секундах.
    """
    with allure.step("Авторизация на сайте онлайн-кинотеатра Кинопоиск"):
        number = "9102470863"
        seconds = "20"
        log = Login(driver)
        log.open_page()
        sleep(40)
        """
        Параметр sleep для обхода вручную капчи на сайте.
        """
        log.waits(seconds)
        log.login(number)
        log.waits(seconds)
        sleep(15)
        """
        Параметр sleep для ожидания загрузки формы ввода кода и сообщения об успешной автоизации на сайте.
        """
        success_text = log.success()
    
        expected_part = "Введите код из пуш-уведомления"
        assert expected_part in success_text, f"Ожидалось '{expected_part}', получено '{success_text}'"
    

def test_login_negative_zero(driver):
    """
    Тест проверяет авторизацию по несуществующему номеру телефона.
    :param driver: WebDriver — объект драйвера Selenium.
    :param number: номер телефона пользователя.
    :param seconds: время ожидания в секундах.
    """
    with allure.step("Авторизация на сайте онлайн-кинотеатра Кинопоиск"):
        number = "0000000000"
        seconds = "10"
        log = Login(driver)
        log.open_page()
        sleep(40)
        """
        Параметр sleep для обхода вручную капчи на сайте.
        """
        log.waits(seconds)
        log.login(number)
        log.waits(seconds)

        mis = log.mistake()
        assert mis == 'Что-то пошло не так'
        allure.attach(driver.get_screenshot_as_png(), name="Скриншот", attachment_type=allure.attachment_type.PNG)

def test_login_negative_empty_number(driver):
    """
    Тест проверяет авторизацию по номеру телефона с пустым полем ввода.
    :param driver: WebDriver — объект драйвера Selenium.
    :param number: номер телефона пользователя.
    :param seconds: время ожидания в секундах.
    """
    with allure.step("Авторизация на сайте онлайн-кинотеатра Кинопоиск"):
        number = ""
        seconds = "10"
        log = Login(driver)
        log.open_page()
        sleep(40)
        """
        Параметр sleep для обхода вручную капчи на сайте.
        """
        log.waits(seconds)
        log.login(number)
        log.waits(seconds)

        mis1 = log.mistake_empty()
        assert mis1 == 'Пожалуйста, укажите номер телефона'

def test_search_positive_latin(driver):
    """
    Тест проверяет поиск фильма на сайте онлайн-кинотеатра Кинопоиск неавторизованным пользователем с позитивным значением на латиннице.
    :param driver: WebDriver — объект драйвера Selenium.
    """
    with allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск"):
        sch = Search(driver)
        sch.open_page()
        sleep(40)
        """
        Параметр sleep для обхода вручную капчи на сайте.
        """
    with allure.step("Поиск фильма неавторизованным пользователем"):
        sch.search("Game of Thrones")
    sleep(3)
    """
    Параметр sleep для прогрузки элемента и стабильной работы теста.
    """
    with allure.step("Проверка результата поиска на латиннице"):
        result = sch.check_l("Игра престолов")
        
        assert result is not None, "Фильм не найден в результатах поиска"
        print(f"Найден фильм: {result}")

def test_search_positive_kiril(driver):
    """
    Тест проверяет поиск фильма на сайте онлайн-кинотеатра Кинопоиск неавторизованным пользователем с позитивным значением на кириллице.
    :param driver: WebDriver — объект драйвера Selenium.
    """
    with allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск"):
        sch = Search(driver)
        sch.open_page()
        sleep(40)
        """
        Параметр sleep для обхода вручную капчи на сайте.
        """
    with allure.step("Поиск фильма неавторизованным пользователем"):   
        sch.search("Игра престолов")

    with allure.step("Проверка результата поиска на кириллице"):
        result1 = sch.check_k("Игра престолов")
        
        assert result1 is not None, "Фильм не найден в результатах поиска"
        print(f"Найден фильм: {result1}")

    