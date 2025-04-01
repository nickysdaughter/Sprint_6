import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import TestData


class OrderPage(BasePage):

    @allure.step('Выбрать станцию метро из выпадающего списка')
    def select_station(self):
        self.click_on_element(OrderPageLocators.SELECT_METRO_ITEM)

    @allure.step('Ввести дату доставки самоката в поле ввода')
    def send_keys_date_by_keyboard_input(self):
        self.send_keys_to_input(OrderPageLocators.DATE_INPUT).send_keys(TestData.FIRST_USER_DATA[5])

    @allure.step('Подтвердить выбор даты в календаре')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.CALENDAR_ITEM)

    @allure.step('Проверить видимость кнопки "Посмотреть статус" после оформления заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_of_element(OrderPageLocators.ORDER_STATUS_BTN)

    @allure.step('Заполнить первую часть формы и перейти к следующему шагу')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.NAME_INPUT)
        self.click_on_element(OrderPageLocators.NAME_INPUT)
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, test_data[0])
        self.click_on_element(OrderPageLocators.LASTNAME_INPUT)
        self.send_keys_to_input(OrderPageLocators.LASTNAME_INPUT, test_data[1])
        self.click_on_element(OrderPageLocators.ADDRESS_INPUT)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_INPUT, test_data[2])
        self.click_on_element(OrderPageLocators.METRO_INPUT)
        self.send_keys_to_input(OrderPageLocators.METRO_INPUT, test_data[3])
        self.click_on_element(OrderPageLocators.SELECT_METRO_ITEM)
        self.click_on_element(OrderPageLocators.PHONE_INPUT)
        self.send_keys_to_input(OrderPageLocators.PHONE_INPUT, test_data[4])
        self.click_on_element(OrderPageLocators.CONTINUE_BTN)

    @allure.step('Заполнить вторую часть формы и подтвердить заказ')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.DATE_INPUT)
        self.click_on_element(OrderPageLocators.DATE_INPUT)
        self.send_keys_to_input(OrderPageLocators.DATE_INPUT, test_data[5])
        self.click_on_element(OrderPageLocators.CHECKBOX_COLOR_SCOOTER)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.DROPDOWN_ITEM_RENT)
        self.click_on_element(OrderPageLocators.COMMENT_INPUT)
        self.send_keys_to_input(OrderPageLocators.COMMENT_INPUT, test_data[6])
        self.click_on_element(OrderPageLocators.MAKE_ORDER_BTN)
        self.wait_visibility_of_element(OrderPageLocators.CONFIRM_ORDER_BTN)
        self.click_on_element(OrderPageLocators.CONFIRM_ORDER_BTN)