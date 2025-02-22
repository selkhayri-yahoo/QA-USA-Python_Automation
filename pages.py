from selenium import webdriver
from selenium.webdriver.common.by import By
import data

class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    OPTIMAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Optimal"]')
    FASTEST_OPTION_LOCATOR = (By.XPATH, '//div[text()="Fastest"]')

    CAR_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/car.8a2b1ff5.svg"]')
    WALK_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/walk.d33bf83c.svg"]')
    TAXI_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/taxi.9a02abc6.svg"]')
    TAXI_ICON_LOCATOR_ACTIVE = (By.XPATH, '//img[@src="/static/media/taxi-active.b0be3054.svg"]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/bike.fb41c762.svg"]')
    SCOOTER_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]')
    DRIVE_ICON_LOCATOR = (By.XPATH, '//div[@class="type drive"]')

    RESULTS_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')
    DURATION_TEXT_LOCATOR = (By.CSS_SELECTOR, "div.results-text>div.duration")
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//div[@class="results-text"]/button[@class="button round"]')
    CAMPING_CARD_LOCATOR = (By.XPATH, '//div[text()="Camping"]/..')

    CAR_MAKE_LOCATOR = (By.XPATH, '//div[@class="drive-preview-title"]')

    LICENCE_ADD_LOCATOR = (By.XPATH, '//div[@class="workflow"]//div[@class="np-button"]')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    BIRTH_DATE_LOCATOR = (By.ID, 'birthDate')
    LICENCE_NUMBER_LOCATOR = (By.ID, 'number')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//div[@class="rights-buttons"]/button[text()="Add"]')
    POPUP_WINDOW_LOCATOR = (By.XPATH, '//div[@class="section active"]//div[@class="head"]')

    CALL_TAXI_LOCATOR = (By.CSS_SELECTOR, "div.results-text>button.button")

    BUSINESS_TARIFF_CARD = (By.XPATH, '//img[@alt="Business"]')
    SLEEPY_TARIFF_CARD = (By.XPATH, '//img[@alt="Sleepy"]')
    HOLIDAY_TARIFF_CARD = (By.XPATH, '//img[@alt="Holiday"]')
    TALKING_TARIFF_CARD = (By.XPATH, '//img[@alt="Talking"]')
    SUPPORTIVE_TARIFF_CARD = (By.XPATH, '//img[@alt="Supportive"]')
    GLOSSY_TARIFF_CARD = (By.XPATH, '//img[@alt="Glossy"]')

    PHONE_NUMBER_BUTTON = (By.XPATH, '//div[@class="workflow"]/div[@class="workflow-subcontainer"]/div[@class="tariff-picker shown"]/div[@class="form"]/div[@class="np-button"]')
    PHONE_NUMBER_FIELD = (By.XPATH, '//input[@name="phone"]')
    PHONE_NUMBER_NEXT_BUTTON = (By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section > form > div.buttons > button.button.full') #
    PHONE_CLOSE_BUTTON = (By.XPATH, "//div[@class='number-picker open']//button[@class='close-button section-close']")

    PAYMENT_METHOD = (By.CSS_SELECTOR, "#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled")
    PAYMENT_METHOD_CC_LOCATOR = (By.XPATH, '//div[@id="root"]/div[@class="app"]/div[@class="payment-picker open"]/div[@class="modal"]/div[@class="section active"]\
/div[@class="pp-selector"]/div[@class="pp-row disabled"]')
    PAYMENT_METHOD_CLOSE = (By.CSS_SELECTOR, "#root > div > div.payment-picker.open > div.modal > div.section.active > button")

    ADD_CARD_CC_NUM = (By.ID, 'number')
    ADD_CARD_CC_CODE = (By.CLASS_NAME, "card-input")  # [1]

    ADD_CARD_SUBMIT_FORM = (By.CSS_SELECTOR, "#root > div > div.payment-picker.open > div.modal.unusual > div.section.active.unusual > form")

    SELECTED_PAYMENT_METHOD = (By.CSS_SELECTOR, "#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled > div.pp-value > div.pp-value-text")
    SELECT_CASH = (By.CSS_SELECTOR, "#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div:nth-child(1) > div.pp-title")
    SELECT_CC = (By.CSS_SELECTOR, "#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div:nth-child(3) > div.pp-checkbox")

    PAYMENT_DIALOG_CLOSE = (By.CSS_SELECTOR, "#root > div > div.payment-picker.open > div.modal > div.section.active > button")

    BLANKET_AND_HANDKERCHIEFS_click = (By.CLASS_NAME, 'switch') # [0]
    BLANKET_AND_HANDKERCHIEFS_read = (By.CLASS_NAME, 'switch-input')

    MESSAGE_TO_DRIVER = (By.ID, "comment")

    ORDER_REQUIREMENTS = (By.CLASS_NAME, "reqs")

    ICE_CREAM_ADD = (By.CLASS_NAME, "counter-plus")
    ITEM_COUNTS = (By.CLASS_NAME, 'counter-value')

    TARIFF_PICKER = (By.XPATH, "//div[contains(@class, 'tariff-picker') and contains(@class, 'shown')]")

    """
    Name: __init__
    Parameters: driver
    Return: None


    """
    def __init__(self, driver):
        self.driver = driver

    #def driver_init(self):
    #    self.driver = webdriver.Chrome()
    #    self.driver.get(data.URBAN_ROUTES_URL)

    #def driver_quit(self):
    #    self.driver.quit()

    """
    Name: enter_from_location
    Parameters: from_text
    Return: None


    """
    def enter_from_location(self, from_text):
        # Enter From address
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    """
    Name: get_from_location
    Parameters: None
    Return:


    """
    def get_from_location(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

    """
    Name: enter_to_location
    Parameters: to_text
    Return: None


    """
    def enter_to_location(self, to_text):
        # Enter To address
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    """
    Name: get_to_location
    Parameters: None
    Return:


    """
    def get_to_location(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")

    """
    Name: click_custom_option
    Parameters: None
    Return: None


    """
    def click_custom_option(self):
        # Click Custom
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    """
    Name: get_custom_option_status
    Parameters: None
    Return:


    """
    def get_custom_option_status(self):
        return self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).get_attribute("class")

    """
    Name: click_optimal_option
    Parameters: None
    Return: None


    """
    def click_optimal_option(self):
        self.driver.find_element(*self.OPTIMAL_OPTION_LOCATOR).click()

    """
    Name: get_optimal_option_status
    Parameters: None
    Return:


    """
    def get_optimal_option_status(self):
        return self.driver.find_element(*self.OPTIMAL_OPTION_LOCATOR).get_attribute("class")

    """
    Name: click_fastest_option
    Parameters: None
    Return: None


    """
    def click_fastest_option(self):
        self.driver.find_element(*self.FASTEST_OPTION_LOCATOR).click()

    """
    Name: get_fastest_option_status
    Parameters: None
    Return:


    """
    def get_fastest_option_status(self):
        return self.driver.find_element(*self.FASTEST_OPTION_LOCATOR).get_attribute("class")

    """
    Name: click_scooter_icon
    Parameters: None
    Return: None


    """
    def click_scooter_icon(self):
        # Click Scooter Icon
        self.driver.find_element(*self.SCOOTER_ICON_LOCATOR).click()

    """
    Name: get_results_text
    Parameters: None
    Return:


    """
    def get_results_text(self):
        # Return the results text
        return self.driver.find_element(*self.RESULTS_TEXT_LOCATOR).text

    """
    Name: click_drive_icon
    Parameters: None
    Return: None


    """
    def click_drive_icon(self):
        # Click Drive Icon
        self.driver.find_element(*self.DRIVE_ICON_LOCATOR).click()

    """
    Name: click_book_button
    Parameters: None
    Return: None


    """
    def click_book_button(self):
        # Click Book button
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()

    """
    Name: click_camping_card
    Parameters: None
    Return:


    """
    def click_camping_card(self):
        self.driver.find_element(*self.CAMPING_CARD_LOCATOR).click()

    """
    Name: get_car_make
    Parameters: None
    Return:


    """
    def get_car_make(self):
        return self.driver.find_element(*self.CAR_MAKE_LOCATOR).text

    """
    Name: click_licence_add_button
    Parameters: None
    Return: None


    """
    def click_licence_add_button(self):
        self.driver.find_element(*self.LICENCE_ADD_LOCATOR).click()

    """
    Name: set_licence_first_name
    Parameters: first_name
    Return: None


    """
    def set_licence_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)

    """
    Name: set_licence_last_name
    Parameters: last_name
    Return: None


    """
    def set_licence_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(last_name)

    """
    Name: set_licence_birth_date
    Parameters: birth_date
    Return: None


    """
    def set_licence_birth_date(self, birth_date):
        self.driver.find_element(*self.BIRTH_DATE_LOCATOR).send_keys(birth_date)

    """
    Name: set_licence_licence_number
    Parameters: licence_number
    Return: None


    """
    def set_licence_licence_number(self, licence_number):
        self.driver.find_element(*self.LICENCE_NUMBER_LOCATOR).send_keys(licence_number)

    """
    Name: click_add_button
    Parameters: None
    Return: None


    """
    def click_add_button(self):
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()

    """
    Name: get_popup_window_text
    Parameters: None
    Return:


    """
    def get_popup_window_text(self):
        return self.driver.find_element(*self.POPUP_WINDOW_LOCATOR).text

    """
    Name: get_duration_text
    Parameters: None
    Return:


    """
    def get_duration_text(self):
        return self.driver.find_element(*self.DURATION_TEXT_LOCATOR).text

    """
    Name: click_car_icon
    Parameters: None
    Return:


    """
    def click_car_icon(self):
        self.driver.find_element(*self.CAR_ICON_LOCATOR).click()

    """
    Name: click_walk_icon
    Parameters: None
    Return:


    """
    def click_walk_icon(self):
        self.driver.find_element(*self.WALK_ICON_LOCATOR).click()

    """
    Name: click_taxi_icon
    Parameters: None
    Return: None


    """
    def click_taxi_icon(self):
        try:
            self.driver.find_element(*self.TAXI_ICON_LOCATOR).click()
        except:
            self.driver.find_element(*self.TAXI_ICON_LOCATOR_ACTIVE).click()

    """
    Name: click_bike_icon
    Parameters: None
    Return:


    """
    def click_bike_icon(self):
        # Click bike Icon
        self.driver.find_element(*self.BIKE_ICON_LOCATOR).click()

    """
    Name: click_call_taxi_button
    Parameters: None
    Return: None


    """
    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()

    """
    Name: click_business_tariff_card
    Parameters: None
    Return: None


    """
    def click_business_tariff_card(self):
        self.driver.find_element(*self.BUSINESS_TARIFF_CARD).click()

    """
    Name: click_sleepy_tariff_card
    Parameters: None
    Return: None


    """
    def click_sleepy_tariff_card(self):
        self.driver.find_element(*self.SLEEPY_TARIFF_CARD).click()

    """
    Name: click_holiday_tariff_card
    Parameters: None
    Return: None


    """
    def click_holiday_tariff_card(self):
        self.driver.find_element(*self.HOLIDAY_TARIFF_CARD).click()

    """
    Name: click_talking_tariff_card
    Parameters: None
    Return: None


    """
    def click_talking_tariff_card(self):
        self.driver.find_element(*self.TALKING_TARIFF_CARD).click()

    """
    Name: click_supportive_tariff_card
    Parameters: None
    Return: None


    """
    def click_supportive_tariff_card(self):
        self.driver.find_element(*self.SUPPORTIVE_TARIFF_CARD).click()

    """
    Name: click_glossy_tariff_card
    Parameters: None
    Return: None


    """
    def click_glossy_tariff_card(self):
        self.driver.find_element(*self.GLOSSY_TARIFF_CARD).click()

    """
    Name: click_phone_number_button
    Parameters: None
    Return: None


    """
    def click_phone_number_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()

    """
    Name: set_phone_number_text
    Parameters: phone_number
    Return: None


    """
    def set_phone_number_text(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(phone_number)

    """
    Name: get_phone_number_text
    Parameters: None
    Return:


    """
    def get_phone_number_text(self):
        return self.driver.find_element(*self.PHONE_NUMBER_FIELD).get_attribute("value")

    """
    Name: click_phone_number_next
    Parameters: None
    Return: None


    """
    def click_phone_number_next(self):
        self.driver.find_element(*self.PHONE_NUMBER_NEXT_BUTTON).click()

    """
    Name: click_phone_number_close
    Parameters: None
    Return: None


    """
    def click_phone_number_close(self):
        self.driver.find_element(*self.PHONE_CLOSE_BUTTON).click()

    """
    Name: click_payment_method
    Parameters: None
    Return: None


    """
    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD).click()

    """
    Name: click_add_credit_card
    Parameters: None
    Return: None


    """
    def click_add_credit_card(self):
        self.driver.find_elements(*self.PAYMENT_METHOD_CC_LOCATOR)[-1].click()

    """
    Name: set_credit_card_text
    Parameters: credit_card_text
    Return: None


    """
    def set_credit_card_text(self, credit_card_text):
        self.driver.find_element(*self.ADD_CARD_CC_NUM).send_keys(credit_card_text)

    """
    Name: set_credit_card_code
    Parameters: code
    Return: None


    """
    def set_credit_card_code(self, code):
        self.driver.find_elements(*self.ADD_CARD_CC_CODE)[1].send_keys(code)

    """
    Name: submit_credit_card_add
    Parameters: None
    Return: None


    """
    def submit_credit_card_add(self):
        self.driver.find_element(*self.ADD_CARD_SUBMIT_FORM).submit()

    """
    Name: select_cash_payment
    Parameters: None
    Return: None


    """
    def select_cash_payment(self):
        self.driver.find_element(*self.SELECT_CASH).click()

    """
    Name: select_cc_payment
    Parameters: None
    Return: None


    """
    def select_cc_payment(self):
        self.driver.find_element(*self.SELECT_CC).click()

    """
    Name: get_selected_payment_method
    Parameters: None
    Return:


    """
    def get_selected_payment_method(self):
        return self.driver.find_element(*self.SELECTED_PAYMENT_METHOD).text

    """
    Name: close_payment_dialog
    Parameters: None
    Return: None


    """
    def close_payment_dialog(self):
        self.driver.find_element(*self.PAYMENT_DIALOG_CLOSE).click()

    """
    Name: send_message_to_driver
    Parameters: message
    Return: None


    """
    def send_message_to_driver(self, message):
        self.driver.find_element(*self.MESSAGE_TO_DRIVER).send_keys(message)

    """
    Name: get_message_to_driver
    Parameters: None
    Return:


    """
    def get_message_to_driver(self):
        return self.driver.find_element(*self.MESSAGE_TO_DRIVER).get_attribute('value')

    """
    Name: click_order_requirements
    Parameters: None
    Return: None


    """
    def click_order_requirements(self):
        self.driver.find_elements(*self.ORDER_REQUIREMENTS)[0].click()

    """
    Name: click_blanket_and_handkerchiefs
    Parameters: None
    Return: None


    """
    def click_blanket_and_handkerchiefs(self):
        self.driver.find_elements(*self.BLANKET_AND_HANDKERCHIEFS_click)[0].click()

    """
    Name: get_blanket_and_handkerchiefs_checkbox_value
    Parameters: None
    Return:


    """
    def get_blanket_and_handkerchiefs_checkbox_value(self):
        switches = self.driver.find_elements(*self.BLANKET_AND_HANDKERCHIEFS_read)

        return switches[0].is_selected()

    """
    Name: click_add_icecream
    Parameters: None
    Return: None


    """
    def click_add_icecream(self):
        self.driver.find_element(*self.ICE_CREAM_ADD).click()

    """
    Name: get_icecream_count
    Parameters: None
    Return:


    """
    def get_icecream_count(self):
        return self.driver.find_elements(*self.ITEM_COUNTS)[0].text

    """
    Name: is_tariff_picker_shown
    Parameters: None
    Return:


    """
    def is_tariff_picker_shown(self):
        tp = self.driver.find_element(*self.TARIFF_PICKER)

        return tp != None

    """
    Name: click_add_cc_payment
    Parameters: None
    Return: None


    """
    def click_add_cc_payment(self):
        self.driver.find_element(*self.PAYMENT_METHOD_CC_LOCATOR).click()

    """
    Name: close_payment_method_dialog
    Parameters: None
    Return: None


    """
    def close_payment_method_dialog(self):
        self.driver.find_element(*self.PAYMENT_METHOD_CLOSE).click()
