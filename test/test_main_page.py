import allure
from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from conftest import driver
from data import TestData
import pytest


class TestMainPageFaq:
    @allure.title('Тестирование раздела "Вопросы о важном"')
    @allure.description('Проверка корректности отображения текста после раскрытия каждого вопроса в разделе FAQ')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.FAQ)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_items(question_number)
        main_page.click_on_faq_items(question_number)
        main_page.wait_visibility_of_faq_answer(question_number)
        assert main_page.get_displayed_text_from_faq_answer(question_number) == expected_answer

    @allure.title('Проверка редиректа на главную страницу при клике на логотип "Самокат"')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу Дзена при клике на логотип "Яндекс"')
    def test_logo_redirect_to_dzen_success(self, driver):

        main_page = MainPage(driver)
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        main_page.wait_for_title()
        assert main_page.get_current_url() == 'https://dzen.ru/?yredirect=true'


