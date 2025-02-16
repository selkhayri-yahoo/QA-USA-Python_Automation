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
    SMS_CODE_FIELD = (By.XPATH, '//input[@id="code"]')
    SMS_CONFIRM_BUTTON = (By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)')

    PAYMENT_METHOD = (By.XPATH, '//div[@class="pp-button filled"]')

    def __init__(self):
        self.driver = webdriver.Chrome()

    def driver_init(self):
        self.driver = webdriver.Chrome()
        self.driver.get(data.URBAN_ROUTES_URL)

    def driver_quit(self):
        self.driver.quit()

    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_custom_option(self):
        # Click Custom
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_optimal_option(self):
        self.driver.find_element(*self.OPTIMAL_OPTION_LOCATOR).click()

    def click_fastest_option(self):
        self.driver.find_element(*self.FASTEST_OPTION_LOCATOR).click()

    def click_scooter_icon(self):
        # Click Scooter Icon
        self.driver.find_element(*self.SCOOTER_ICON_LOCATOR).click()

    def get_results_text(self):
        # Return the results text
        return self.driver.find_element(*self.RESULTS_TEXT_LOCATOR).text

    def click_drive_icon(self):
        # Click Drive Icon
        self.driver.find_element(*self.DRIVE_ICON_LOCATOR).click()

    def click_book_button(self):
        # Click Book button
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()

    def click_camping_card(self):
        self.driver.find_element(*self.CAMPING_CARD_LOCATOR).click()

    def get_car_make(self):
        return self.driver.find_element(*self.CAR_MAKE_LOCATOR).text

    def click_licence_add_button(self):
        self.driver.find_element(*self.LICENCE_ADD_LOCATOR).click()

    def set_licence_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)

    def set_licence_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(last_name)

    def set_licence_birth_date(self, birth_date):
        self.driver.find_element(*self.BIRTH_DATE_LOCATOR).send_keys(birth_date)

    def set_licence_licence_number(self, licence_number):
        self.driver.find_element(*self.LICENCE_NUMBER_LOCATOR).send_keys(licence_number)

    def click_add_button(self):
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()

    def get_popup_window_text(self):
        return self.driver.find_element(*self.POPUP_WINDOW_LOCATOR).text

    def get_duration_text(self):
        return self.driver.find_element(*self.DURATION_TEXT_LOCATOR).text

    def click_car_icon(self):
        self.driver.find_element(*self.CAR_ICON_LOCATOR).click()

    def click_walk_icon(self):
        self.driver.find_element(*self.WALK_ICON_LOCATOR).click()

    def click_taxi_icon(self):
        try:
            self.driver.find_element(*self.TAXI_ICON_LOCATOR).click()
        except:
            self.driver.find_element(*self.TAXI_ICON_LOCATOR_ACTIVE).click()


    def click_bike_icon(self):
        # Click bike Icon
        self.driver.find_element(*self.BIKE_ICON_LOCATOR).click()

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()

    def click_business_tariff_card(self):
        self.driver.find_element(*self.BUSINESS_TARIFF_CARD).click()

    def click_sleepy_tariff_card(self):
        self.driver.find_element(*self.SLEEPY_TARIFF_CARD).click()

    def click_holiday_tariff_card(self):
        self.driver.find_element(*self.HOLIDAY_TARIFF_CARD).click()

    def click_talking_tariff_card(self):
        self.driver.find_element(*self.TALKING_TARIFF_CARD).click()

    def click_supportive_tariff_card(self):
        self.driver.find_element(*self.SUPPORTIVE_TARIFF_CARD).click()

    def click_glossy_tariff_card(self):
        self.driver.find_element(*self.GLOSSY_TARIFF_CARD).click()

    def click_phone_number_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()

    def set_phone_number_text(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(phone_number)

    def click_phone_number_next(self):
        #self.driver.find_elements(*self.PHONE_NUMBER_NEXT_BUTTON)[0].click()
        self.driver.find_element(*self.PHONE_NUMBER_NEXT_BUTTON).click()

    def set_sms_code(self, code):
        self.driver.find_element(*self.SMS_CODE_FIELD).send_keys(code)

    def click_sms_code_confirm(self):
        self.driver.find_element(*self.SMS_CONFIRM_BUTTON).click()

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD).click()

