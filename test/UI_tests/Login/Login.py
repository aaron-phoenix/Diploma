from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.epic("Авторизация")
class Login:
    def __init__(self, driver):
        self.driver = driver
        """
        Конструктор класса Login.
        :param driver: WebDriver — объект драйвера Selenium.
        """

    @allure.step("Открытие страницы онлайн-кинотеатра Кинопоиск")
    def open_page(self):
        """
        Открывает страницу онлайн-кинотеатра Кинопоиск.
        Разворачивает окно браузера на максимум.
        """
        self.driver.get("https://hd.kinopoisk.ru")
        self.driver.maximize_window()

    @allure.step("Авторизация на сайте онлайн-кинотеатра Кинопоиск")
    def login(self, number):
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
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[2]/form/div[2]/div[2]/button/span").click()

    @allure.step("Ожидание результата")
    def waits(self, seconds):
        """
        Ожидает загрузки страницы после авторизации.
        Ожидаемый результат - загрузка html-тега body.
        :param seconds: время ожидания в секундах
        
        """
        waiter = WebDriverWait(self.driver, seconds)

        waiter.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "body"))
    )
    
    @allure.step("Сообщение об ошибке при введении неправильного номера")
    def mistake(self):
        """
        Возвращает сообщение об ошибке при введении неправильного номера телефона.
        """
        return self.driver.find_element(By.CSS_SELECTOR, '.centered.page-header-text [data-color="primary"]').text
    
    @allure.step("Сообщение об ошибке при оставлении поле ввода пустым")
    def mistake_empty(self):
        """
        Возвращает сообщение об ошибке при оставлении поле ввода номера телефона пустым.
        """
        
        return self.driver.find_element(By.XPATH, "//span[text()='Пожалуйста, укажите номер телефона']").text


    @allure.step("Сообщение при успешной авторизации")
    def success(self):
        """
        Возвращает текст сообщения при успешной авторизации.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".TitleWithAppList"))
        )
        return element.text