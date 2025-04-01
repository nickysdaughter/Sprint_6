import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Дождаться отображения кнопки "Заказать" в верхней части страницы')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.ORDER_BTN_IN_HEADER)

    @allure.step('Нажать на кнопку "Заказать" в верхней части страницы')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.ORDER_BTN_IN_HEADER)

    @allure.step('Дождаться загрузки элемента логотипа "Самокат" в шапке сайта')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Дождаться загрузки элемента логотипа "Яндекс" в шапке сайта')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Выполнить клик по логотипу "Самокат" в шапке сайта')
    def click_on_header_logo_scooter(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Выполнить клик по логотипу "Яндекс" в шапке сайта')
    def click_on_header_logo_yandex(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Дождаться появления основного заголовка на главной странице')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.HOME_HEADER)

    @allure.step('Проверить наличие основного заголовка на странице')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.HOME_HEADER)

    @allure.step('Прокрутить страницу до раздела часто задаваемых вопросов')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.FAQ)

    @allure.step('Дождаться отображения вопроса в секции FAQ')
    def wait_visibility_of_faq_items(self, data):
        self.wait_visibility_of_element(MainPageLocators.QUESTIONS[data])

    @allure.step('Нажать на вопрос в секции FAQ')
    def click_on_faq_items(self, data):
        self.click_on_element(MainPageLocators.QUESTIONS[data])

    @allure.step('Дождаться появления ответа на вопрос в секции FAQ')
    def wait_visibility_of_faq_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.ANSWERS[data])

    @allure.step('Получить текст ответа на вопрос из секции FAQ')
    def get_displayed_text_from_faq_answer(self, data):
        return self.get_element_text(MainPageLocators.ANSWERS[data])

    @allure.step('Ожидание загрузки заголовка страницы Дзен')
    def wait_for_title(self):
        self.wait_for_title_is('Дзен')