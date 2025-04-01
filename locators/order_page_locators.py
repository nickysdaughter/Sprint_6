from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма "Для кого самокат"
    TITLE_PERSONAL_INFO = (By.XPATH, "//div[text()='Для кого самокат' and contains(@class, 'Order_Header')]")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    SELECT_METRO_ITEM = (By.XPATH, ".//li[@class='select-search__row']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONTINUE_BTN = (By.XPATH, "//button[text()='Далее']")

    # Форма "Про аренду"
    TITLE_RENT_INFO = (By.XPATH, "//div[text()='Про аренду' and contains(@class, 'Order_Header')]")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR = (By.XPATH, "//div[@class='react-datepicker-popper']")
    CALENDAR_ITEM = (By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")
    RENTAL_PERIOD = (By.XPATH, ".//div[text()='* Срок аренды']")
    DROPDOWN_ITEM_RENT = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    CHECKBOX_COLOR_SCOOTER = (By.XPATH, "//input[@id='grey']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    MAKE_ORDER_BTN = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    # Подтверждение заказа
    CONFIRM_ORDER_BTN = (By.XPATH, "//button[text()='Да']")
    ORDER_STATUS_BTN = (By.XPATH, ".//*[text()='Посмотреть статус']")