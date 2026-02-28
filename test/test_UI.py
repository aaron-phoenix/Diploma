import pytest
import allure
from selenium import webdriver
from UI_tests.Login.Login import Login
from UI_tests.Search.Search import Search
from API_tests.conftest import base_url1


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.ui
@pytest.mark.positive
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоиск")
@allure.title("Авторизация с валидным номером телефона")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках формы авторизации на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("UI-тестирование")
def test_login_positive(driver, base_url1):
    """
    Тест проверяет авторизацию по существующему номеру телефона.
    :param driver: WebDriver — объект драйвера Selenium.
    :param base_url: сайт онлайн кинотеатра Кинопоиск.
    :param number: номер телефона пользователя.
    :param seconds: время ожидания в секундах.
    """
    number = "9102470863"
    seconds = "20"
    log = Login(driver, base_url1)

    with allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск"):
        log.open_page()

    with allure.step("Ожидание результата"):
        log.waits(seconds)

    with allure.step("Авторизация на сайте онлайн-кинотеатра Кинопоиск"):
        log.login(number)

    with allure.step("Сообщение при успешной авторизации"):
        success_text = log.success()

        expected_part = "Введите код из пуш-уведомления"

        assert expected_part in success_text, f"Ожидалось '{expected_part}', получено '{success_text}'"
        allure.attach(driver.get_screenshot_as_png(), name="Скриншот", attachment_type=allure.attachment_type.PNG)

@pytest.mark.ui
@pytest.mark.negative
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоиск")
@allure.title("Авторизация с номером телефона из нулей")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках формы авторизации на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("UI-тестирование")
def test_login_negative_zero(driver, base_url1):
    """
    Тест проверяет авторизацию по несуществующему номеру телефона.
    :param driver: WebDriver — объект драйвера Selenium.
    :param base_url: сайт онлайн кинотеатра Кинопоиск.
    :param number: номер телефона пользователя.
    :param seconds: время ожидания в секундах.
    """
    
    number = "0000000000"
    seconds = "40"
    log = Login(driver,base_url1)

    with allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск"):
        log.open_page()
    
    with allure.step("Ожидание результата"):
        log.waits(seconds)

    with allure.step("Авторизация на сайте онлайн-кинотеатра Кинопоиск"):
        log.login(number)
    
    with allure.step("Сообщение об ошибке при введении неправильного номера"):
        mis = log.mistake(seconds)
    
        assert mis == 'Что-то пошло не так'
        allure.attach(driver.get_screenshot_as_png(), name="Скриншот", attachment_type=allure.attachment_type.PNG)

@pytest.mark.ui
@pytest.mark.negative
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоиск")
@allure.title("Авторизация с пустым полем ввода номера телефона")
@allure.description("Тестирование проверяет работоспособность и адекватное поведение при ошибках формы авторизации на сайте онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("UI-тестирование")
def test_login_negative_empty_number(driver, base_url1):
    """
    Тест проверяет авторизацию по номеру телефона с пустым полем ввода.
    :param driver: WebDriver — объект драйвера Selenium.
    :param base_url: сайт онлайн кинотеатра Кинопоиск.
    :param number: номер телефона пользователя.
    :param seconds: время ожидания в секундах.
    """
    
    number = ""
    seconds = "40"
    log = Login(driver, base_url1)
    with allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск"):
        log.open_page()

    with allure.step("Ожидание результата"):  
        log.waits(seconds)

    with allure.step("Авторизация на сайте онлайн-кинотеатра Кинопоиск"):
        log.login(number)

    with allure.step("Сообщение об ошибке при оставлении поле ввода пустым"):
        mis1 = log.mistake_empty()

        assert mis1 == 'Пожалуйста, укажите номер телефона'
        allure.attach(driver.get_screenshot_as_png(), name="Скриншот", attachment_type=allure.attachment_type.PNG)


@pytest.mark.ui
@pytest.mark.positive
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоиск")
@allure.title("Поиск фильма на латиннице")
@allure.description("Тестирование проверяет работоспособность поиска онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("UI-тестирование")
def test_search_positive_latin(driver, base_url1):
    """
    Тест проверяет поиск фильма на сайте онлайн-кинотеатра Кинопоиск неавторизованным пользователем с позитивным значением на латиннице.
    :param driver: WebDriver — объект драйвера Selenium.
    :param base_url: сайт онлайн кинотеатра Кинопоиск.
    """
    sch = Search(driver, base_url1)

    with allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск"):
        sch.open_page()

    with allure.step("Ожидание результата"):
        sch.waits(40)
       
    with allure.step("Поиск фильма неавторизованным пользователем"):
        sch.search("Game of Thrones")
    
    with allure.step("Проверка результата поиска на латиннице"):
        result = sch.check_l("Игра престолов")
        
        assert result is not None, "Фильм не найден в результатах поиска"
        print(f"Найден фильм: {result}")
        allure.attach(driver.get_screenshot_as_png(), name="Скриншот", attachment_type=allure.attachment_type.PNG)


@pytest.mark.ui
@pytest.mark.positive
@allure.epic("Тестирование Онлайн-кинотеатра Кинопоиск")
@allure.title("Поиск фильма на кириллице")
@allure.description("Тестирование проверяет работоспособность поиска онлайн-кинотеатра Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("UI-тестирование")
def test_search_positive_kiril(driver, base_url1):
    """
    Тест проверяет поиск фильма на сайте онлайн-кинотеатра Кинопоиск неавторизованным пользователем с позитивным значением на кириллице.
    :param driver: WebDriver — объект драйвера Selenium.
    :param base_url: сайт онлайн кинотеатра Кинопоиск.
    """
    sch = Search(driver, base_url1)

    with allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск"):
        sch.open_page()

    with allure.step("Ожидание результата"):
        sch.waits(40)
        
    with allure.step("Поиск фильма неавторизованным пользователем"):   
        sch.search("Игра престолов")

    with allure.step("Проверка результата поиска на кириллице"):
        result1 = sch.check_k("Игра престолов")
        
        assert result1 is not None, "Фильм не найден в результатах поиска"
        print(f"Найден фильм: {result1}")
        allure.attach(driver.get_screenshot_as_png(), name="Скриншот", attachment_type=allure.attachment_type.PNG)

   