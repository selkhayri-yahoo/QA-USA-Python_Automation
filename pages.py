from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    OPTIMAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Optimal"]')
    FASTEST_OPTION_LOCATOR = (By.XPATH, '//div[text()="Fastest"]')
    SCOOTER_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]')
    SCOOTER_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/bike.fb41c762.svg"]')
    BIKE_TEXT_LOCATOR = SCOOTER_TEXT_LOCATOR
    DRIVE_ICON_LOCATOR = (By.XPATH, '//div[@class="type drive"]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//div[@class="results-text"]/button[@class="button round"]')
    CAMPING_CARD_LOCATOR = (By.XPATH, '//div[text()="Camping"]/..')     #'//div[@class="tariff-cards"]/div[@class="tcard"]'
    CAR_MAKE_LOCATOR = (By.XPATH, '//div[@class="drive-preview-title"]')
    LICENCE_ADD_LOCATOR = (By.XPATH, '//div[@class="workflow"]//div[@class="np-button"]')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    BIRTH_DATE_LOCATOR = (By.ID, 'birthDate')
    LICENCE_NUMBER_LOCATOR = (By.ID, 'number')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//div[@class="rights-buttons"]/button[text()="Add"]')
    POPUP_WINDOW_LOCATOR = (By.XPATH, '//div[@class="section active"]//div[@class="head"]')
    DURATION_TEXT_LOCATOR = (By.CSS_SELECTOR, "div.results-text>div.duration")

    def __init__(self, driver):
        self.driver = driver

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

    def get_scooter_text(self):
        # Return the "Scooter" text
        return self.driver.find_element(*self.SCOOTER_TEXT_LOCATOR).text

    def click_bike_icon(self):
        # Click bike Icon
        self.driver.find_element(*self.BIKE_ICON_LOCATOR).click()

    def get_bike_icon(self):
        # Click Bike Icon
        self.driver.find_element(*self.BIKE_ICON_LOCATOR).click()

    def get_bike_text(self):
        # Return the "Bike" text
        return self.driver.find_element(*self.BIKE_TEXT_LOCATOR).text

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
