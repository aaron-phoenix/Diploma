import pytest
import allure
from selenium import webdriver
from UI_tests.Login.Login import Login
from UI_tests.Search.Search import Search


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.epic("Тестирование Онлайн-кинотеатра Кинопоиск")
@allure.title("Авторизация с валидным номером телефона")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках формы авторизации на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("UI-тестирование")
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
        log.waits(seconds)
        log.login(number)
        success_text = log.success()
    
        expected_part = "Введите код из пуш-уведомления"
        assert expected_part in success_text, f"Ожидалось '{expected_part}', получено '{success_text}'"
    
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоиск")
@allure.title("Авторизация с номером телефона из нулей")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках формы авторизации на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("UI-тестирование")
def test_login_negative_zero(driver):
    """
    Тест проверяет авторизацию по несуществующему номеру телефона.
    :param driver: WebDriver — объект драйвера Selenium.
    :param number: номер телефона пользователя.
    :param seconds: время ожидания в секундах.
    """
    with allure.step("Авторизация на сайте онлайн-кинотеатра Кинопоиск"):
        number = "0000000000"
        seconds = "40"
        log = Login(driver)
        log.open_page()
        log.waits(seconds)
        log.login(number)
        mis = log.mistake(seconds)
    
        assert mis == 'Что-то пошло не так'
        allure.attach(driver.get_screenshot_as_png(), name="Скриншот", attachment_type=allure.attachment_type.PNG)

@allure.epic("Тестирование Онлайн-кинотеатра Кинопоиск")
@allure.title("Авторизация с пустым полем ввода номера телефона")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках формы авторизации на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("UI-тестирование")
def test_login_negative_empty_number(driver):
    """
    Тест проверяет авторизацию по номеру телефона с пустым полем ввода.
    :param driver: WebDriver — объект драйвера Selenium.
    :param number: номер телефона пользователя.
    :param seconds: время ожидания в секундах.
    """
    with allure.step("Авторизация на сайте онлайн-кинотеатра Кинопоиск"):
        number = ""
        seconds = "40"
        log = Login(driver)
        log.open_page()
        log.waits(seconds)
        log.login(number)
        mis1 = log.mistake_empty()
        assert mis1 == 'Пожалуйста, укажите номер телефона'

@allure.epic("Тестирование Онлайн-кинотеатра Кинопоиск")
@allure.title("Поиск фильма на латиннице")
@allure.description("Тестирование проверяет работоспособность поиска онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("UI-тестирование")
def test_search_positive_latin(driver):
    """
    Тест проверяет поиск фильма на сайте онлайн-кинотеатра Кинопоиск неавторизованным пользователем с позитивным значением на латиннице.
    :param driver: WebDriver — объект драйвера Selenium.
    """
    with allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск"):
        sch = Search(driver)
        sch.open_page()
        sch.waits(40)
       
    with allure.step("Поиск фильма неавторизованным пользователем"):
        sch.search("Game of Thrones")
    
    with allure.step("Проверка результата поиска на латиннице"):
        result = sch.check_l("Игра престолов")
        
        assert result is not None, "Фильм не найден в результатах поиска"
        print(f"Найден фильм: {result}")

@allure.epic("Тестирование Онлайн-кинотеатра Кинопоиск")
@allure.title("Поиск фильма на кириллице")
@allure.description("Тестирование проверяет работоспособность поиска онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("UI-тестирование")
def test_search_positive_kiril(driver):
    """
    Тест проверяет поиск фильма на сайте онлайн-кинотеатра Кинопоиск неавторизованным пользователем с позитивным значением на кириллице.
    :param driver: WebDriver — объект драйвера Selenium.
    """
    with allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск"):
        sch = Search(driver)
        sch.open_page()
        sch.waits(40)
        
    with allure.step("Поиск фильма неавторизованным пользователем"):   
        sch.search("Игра престолов")

    with allure.step("Проверка результата поиска на кириллице"):
        result1 = sch.check_k("Игра престолов")
        
        assert result1 is not None, "Фильм не найден в результатах поиска"
        print(f"Найден фильм: {result1}")
   