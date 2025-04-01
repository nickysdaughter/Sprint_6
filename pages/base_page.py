from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Выполнить клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Извлечь текст из элемента')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Прокрутить страницу до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Дождаться видимости элемента на странице')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Проверить, что элемент отображается на экране')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Переключиться на другую вкладку браузера')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить текущий URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться загрузки заголовка страницы')
    def wait_for_title_is(self, title):
        WebDriverWait(self.driver, 10).until(expected_conditions.title_contains(title))