from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.epic("Авторизация")
class Login:
    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.url = url
        """
        Конструктор класса Login.
        :param driver: WebDriver — объект драйвера Selenium.
        :param url: сайт онлайн кинотеатра Кинопоиск.
        """

    @allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск")
    def open_page(self) -> None:
        """
        Открывает страницу онлайн-кинотеатра Кинопоиск.
        Разворачивает окно браузера на максимум.
        """
        self.driver.get(self.url)
        self.driver.maximize_window()

    @allure.step("Авторизация на сайте онлайн-кинотеатра Кинопоиск")
    def login(self, number) -> None:
        """
        Открывает страницу с формой авторизации онлайн-кинотеатра Кинопоиск.
        Находит поле ввода номера телефона.
        Вводит значение - номер телефона.
        нажимает кнопку Войти.
        
        :param number: номер телефона пользователя
        """
        self.driver.find_element(By.CSS_SELECTOR,"a[href*='passport.yandex']").click()
        input = self.driver.find_element(By.CSS_SELECTOR,".ya_899deef4")
        input.send_keys(number)
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="split-add-user-next-phone"]').click()

    @allure.step("Ожидание результата")
    def waits(self, seconds) -> None:
        """
        Ожидает загрузки страницы после авторизации.
        Ожидаемый результат - появление кнопки Войти.
        :param seconds: время ожидания в секундах
        
        """
        waiter = WebDriverWait(self.driver, seconds)

        waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='passport.yandex']"))
    )
    
    @allure.step("Сообщение об ошибке при введении неправильного номера")
    def mistake(self, seconds) -> str:
        """
        Возвращает сообщение об ошибке при введении неправильного номера телефона.
        Ожидаемый результат - появление кнопки Войти.
        :params seconds: ожидание появления сообщения об ошибке.
        """
        waiter = WebDriverWait(self.driver, seconds)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.centered.page-header-text [data-color="primary"]'), "Что-то пошло не так"))
        return self.driver.find_element(By.CSS_SELECTOR, '.centered.page-header-text [data-color="primary"]').text
    
    @allure.step("Сообщение об ошибке при оставлении поле ввода пустым")
    def mistake_empty(self) -> str:
        """
        Возвращает сообщение об ошибке при оставлении поле ввода номера телефона пустым.
        """
        
        return self.driver.find_element(By.XPATH, "//span[text()='Пожалуйста, укажите номер телефона']").text


    @allure.step("Сообщение при успешной авторизации")
    def success(self) -> str:
        """
        Возвращает текст сообщения при успешной авторизации.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".TitleWithAppList"))
        )
        return element.text