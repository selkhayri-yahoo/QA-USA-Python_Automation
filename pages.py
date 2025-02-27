from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import data
import time

class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    FROM_LOCATOR_PARENT = (By.CSS_SELECTOR, '#root > div > div.workflow > div.dst-picker > div:nth-child(1) > div:nth-child(2) > div.input-container')

    TO_LOCATOR = (By.ID, 'to')
    TO_LOCATOR_PARENT = (By.CSS_SELECTOR, '#root > div > div.workflow > div.dst-picker > div:nth-child(2) > div:nth-child(2) > div.input-container')

    CALL_TAXI_LOCATOR = (By.CSS_SELECTOR, "div.results-text>button.button")

    BUSINESS_TARIFF_CARD = (By.XPATH, '//img[@alt="Business"]')
    BUSINESS_TARIFF_IND = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(1)')
    SLEEPY_TARIFF_CARD = (By.XPATH, '//img[@alt="Sleepy"]')
    SLEEPY_TARIFF_IND = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(2)')
    HOLIDAY_TARIFF_CARD = (By.XPATH, '//img[@alt="Holiday"]')
    HOLIDAY_TARIFF_IND = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(3)')
    TALKING_TARIFF_CARD = (By.XPATH, '//img[@alt="Talking"]')
    TALKING_TARIFF_IND = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(4)')
    SUPPORTIVE_TARIFF_CARD = (By.XPATH, '//img[@alt="Supportive"]')
    SUPPORTIVE_TARIFF_IND = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(5)')
    GLOSSY_TARIFF_CARD = (By.XPATH, '//img[@alt="Glossy"]')
    GLOSSY_TARIFF_IND = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(6)')

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

    ICE_CREAM_ADD = (By.CLASS_NAME, "counter-plus")
    ITEM_COUNTS = (By.CLASS_NAME, 'counter-value')

    TARIFF_PICKER = (By.XPATH, "//div[contains(@class, 'tariff-picker') and contains(@class, 'shown')]")
    
    SMART_BUTTON = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button')
    ORDER_BODY = (By.CSS_SELECTOR, '#root > div > div.order.shown > div.order-body')

    """
    Name: __init__
    Parameters: driver
    Return: None

    This is the class constructor.
    """
    def __init__(self,driver):
        self.driver = driver


    """
    Name: enter_from_location
    Parameters: from_text
    Return: None

    This method sets the "From" address in the Urban Routes web interface
    """
    def enter_from_location(self, from_text):
        # Enter From address
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    
    """
    Name: get_from_location
    Parameters: None
    Return: The value in the "From" address field

    This method retrieves the value that is stored in the "From" address field
    """
    def get_from_location(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

    
    """
    Name: enter_to_location
    Parameters: to_text
    Return: None

    This method sets the "To" address field with the passed-in parameter
    """
    def enter_to_location(self, to_text):
        # Enter To address
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    
    """
    Name: get_to_location
    Parameters: None
    Return: The value in the "To" address field

    This method retrieves the value that is stored in the "To" address field
    """
    def get_to_location(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")


    """
    Name: click_call_taxi_button
    Parameters: None
    Return: None

    This method clicks the "Call a taxi" button on the Urban Routes page
    """
    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()


    """
    Name: click_business_tariff_card
    Parameters: None
    Return: None

    This method clicks the "Business" tariff card on the Urban Routes page
    """
    def click_business_tariff_card(self):
        self.driver.find_element(*self.BUSINESS_TARIFF_CARD).click()

    
    """
    Name: click_sleepy_tariff_card
    Parameters: None
    Return: None

    This method clicks the "Sleepy" tariff card on the Urban Routes page
    """
    def click_sleepy_tariff_card(self):
        self.driver.find_element(*self.SLEEPY_TARIFF_CARD).click()

    
    """
    Name: click_holiday_tariff_card
    Parameters: None
    Return: None

    This method clicks the "Holiday" tariff card of the Urban Routes page
    """
    def click_holiday_tariff_card(self):
        self.driver.find_element(*self.HOLIDAY_TARIFF_CARD).click()

    """
    Name: click_talking_tariff_card
    Parameters: None
    Return: None

    This method clicks the "Talking" tariff card of the Urban Routes page
    """
    def click_talking_tariff_card(self):
        self.driver.find_element(*self.TALKING_TARIFF_CARD).click()


    """
    Name: click_supportive_tariff_card
    Parameters: None
    Return: None

    This method clicks the "Supportive" tariff card of the Urban Routes page
    """
    def click_supportive_tariff_card(self):
        self.driver.find_element(*self.SUPPORTIVE_TARIFF_CARD).click()

    """
    Name: click_glossy_tariff_card
    Parameters: None
    Return: None

    This method clicks the "Glossy" tariff card of the Urban Routes page
    """
    def click_glossy_tariff_card(self):
        self.driver.find_element(*self.GLOSSY_TARIFF_CARD).click()

    """
    Name: click_phone_number_button
    Parameters: None
    Return: None

    This method clicks the "Phone Number" button of the Urban Routes page
    """
    def click_phone_number_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()


    """
    Name: click_phone_number_close
    Parameters: None
    Return: None

    This method clicks the "Close" button of the "Phone number" dialog
    """
    def click_phone_number_close(self):
        self.driver.find_element(*self.PHONE_CLOSE_BUTTON).click()

    """
    Name: click_payment_method
    Parameters: None
    Return: None

    This method clicks the "Payment Method" button on the Urban Routes page
    """
    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD).click()

    """
    Name: click_add_credit_card
    Parameters: None
    Return: None

    This method clicks on the "Add" credit card button of the payment methods
    dialog
    """
    def click_add_credit_card(self):
        self.driver.find_elements(*self.PAYMENT_METHOD_CC_LOCATOR)[-1].click()

    """
    Name: set_credit_card_text
    Parameters: credit_card_text
    Return: None

    This method sets the credit card number field of the "Add Credit Card" 
    dialog
    """
    def set_credit_card_text(self, credit_card_text):
        self.driver.find_element(*self.ADD_CARD_CC_NUM).send_keys(credit_card_text)

    """
    Name: set_credit_card_code
    Parameters: code
    Return: None

    This method sets the credit card code field of the "Add Credit Card" dialog
    """
    def set_credit_card_code(self, code):
        self.driver.find_elements(*self.ADD_CARD_CC_CODE)[1].send_keys(code)


    """
    Name: submit_credit_card_add
    Parameters: None
    Return: None

    This method clicks the "submit" button of the "Add Credit Card" dialog
    """
    def submit_credit_card_add(self):
        self.driver.find_element(*self.ADD_CARD_SUBMIT_FORM).submit()


    """
    Name: select_cash_payment
    Parameters: None
    Return: None

    This method selects the Cash Payment method
    """
    def select_cash_payment(self):
        self.driver.find_element(*self.SELECT_CASH).click()


    """
    Name: select_cc_payment
    Parameters: None
    Return: None

    This method selects one of the available Credit Card payment methods
    """
    def select_cc_payment(self):
        self.driver.find_element(*self.SELECT_CC).click()


    """
    Name: get_selected_payment_method
    Parameters: None
    Return:

    This method retrieves and returns the selected payment method
    """
    def get_selected_payment_method(self):
        return self.driver.find_element(*self.SELECTED_PAYMENT_METHOD).text


    """
    Name: close_payment_dialog
    Parameters: None
    Return: None

    This method closes the "Payment Method" dialog
    """
    def close_payment_dialog(self):
        self.driver.find_element(*self.PAYMENT_DIALOG_CLOSE).click()


    """
    Name: send_message_to_driver
    Parameters: message
    Return: None

    This method populates the "Message to the driver..." text field
    """
    def send_message_to_driver(self, message):
        self.driver.find_element(*self.MESSAGE_TO_DRIVER).send_keys(message)


    """
    Name: get_message_to_driver
    Parameters: None
    Return:

    This message gets the contents of the "Message to the driver..." text field
    """
    def get_message_to_driver(self):
        return self.driver.find_element(*self.MESSAGE_TO_DRIVER).get_attribute('value')

    
    """
    Name: click_blanket_and_handkerchiefs
    Parameters: None
    Return: None

    This method clicks the toggle switch for "Blanket and handkerchiefs"
    """
    def click_blanket_and_handkerchiefs(self):
        self.driver.find_elements(*self.BLANKET_AND_HANDKERCHIEFS_click)[0].click()


    """
    Name: get_blanket_and_handkerchiefs_checkbox_value
    Parameters: None
    Return:

    This method returns the state of the toggle switch for "Blanket and 
    handkerchiefs"
    """
    def get_blanket_and_handkerchiefs_checkbox_value(self):
        switches = self.driver.find_elements(*self.BLANKET_AND_HANDKERCHIEFS_read)

        return switches[0].is_selected()


    """
    Name: click_add_icecream
    Parameters: None
    Return: None

    This method increments the counter for "Ice cream" by clicking the adjacent
    "+" button
    """
    def click_add_icecream(self):
        self.driver.find_element(*self.ICE_CREAM_ADD).click()

    """
    Name: get_icecream_count
    Parameters: None
    Return:

    This method returns the value of the counter for "Ice cream"    
    """
    def get_icecream_count(self):
        return self.driver.find_elements(*self.ITEM_COUNTS)[0].text


    """
    Name: close_payment_method_dialog
    Parameters: None
    Return: None

    This method closes the "Payment method" dialog
    """
    def close_payment_method_dialog(self):
        self.driver.find_element(*self.PAYMENT_METHOD_CLOSE).click()


    """
    Name: reload_page    
    Paramaters: None
    Returns: None

    This method reloads the urban routes page.
    """
    def reload_page(self):
        # Check if the URL specified by constant URBAN_ROUTES_URL in the data.py file is reachable
        # and print a message accordingly
        self.driver.get(data.URBAN_ROUTES_URL)  # Retrieve the urban routes page


    """
    Name: click_smart_button    
    Paramaters: None
    Returns: None

    This method clicks the "Enter the number and order" button.
    """
    def click_smart_button(self):
        self.driver.find_element(*self.SMART_BUTTON).click()


    """
    Name: is_order_visible    
    Paramaters: None
    Returns: None

    This method return true if the "Car search" dialog is visible
    """        
    def is_order_visible(self):
        return self.driver.find_element(*self.ORDER_BODY) != None


    """
    Name: set_addresses    
    Parameters: None
    Returns: None

    This method sets the source and destination addresses.
    """
    def set_addresses(self):
        self.enter_from_location("East")  # Set the "From" address to "East"
        self.enter_to_location("1300")  # Set the "To" address to "1300"

    """
    Name: call_taxi    
    Parameters: None
    Returns: None

    This method implements all the operations from setting the source and destination addresses to calling a taxi
    """


    def call_taxi(self):
        self.set_addresses()  # Set the "From" and "To" addresses
        time.sleep(2)
        self.click_call_taxi_button()  # Click the "Call a taxi" button


    """
    Name: set_phone_number    
    Parameters: phone_number (string of numbers: +1 XXX XXX XXXX)
    Returns: None

    This method sets the phone number field in the Phone number dialog box.
    """
    def set_phone_number(self, phone_number):
        time.sleep(5)
        self.click_phone_number_button()  # Open the "Phone number" dialog
        time.sleep(3)
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(phone_number)  # Set the "Phone number"


    """
    Name: get_phone_number    
    Parameters: None
    Returns: The phone number the was entered into the Phone number dialog.

    This method gets the phone number the was entered into the Phone number dialog
    """
    def get_phone_number(self):
        self.click_phone_number_button()  # Open the "Phone number" dialog
        time.sleep(3)
        return self.driver.find_element(*self.PHONE_NUMBER_FIELD).get_attribute("value")  # Retrieve and return the "Phone number" field


    """
    Name: add_credit_card_payment    
    Parameters: None
    Returns: None

    This method adds a credit card option in the Payment Methods dialog.
    """
    def add_credit_card_payment(self):
        # Open the "Payment Method" dialog
        self.click_payment_method()  # Open the "Payment Method" dialog

        # Add a credit card number and code
        try:
            time.sleep(4)
            self.click_add_credit_card()  # Open the "Add a card" dialog box
            time.sleep(4)
            self.set_credit_card_text("1234 5678 9012")  # Enter credit card number
            time.sleep(4)
            self.set_credit_card_code("4970")  # Enter credit card code
            time.sleep(4)
            self.submit_credit_card_add()  # Click link to add credit card and close the "Add a card" dialog
            time.sleep(4)
            self.close_payment_method_dialog()  # Close the "Payment Method" dialog
            time.sleep(4)
            print("Successfully filled card: add credit card")  # Log success
        except:
            print("Failed to fill card: add credit card")  # log failure


    """
    Name: toggle_payment_method_selection
    Parameters: None
    Returns: None

    This method tests the ability to toggle between cash payment and credit card payment.
    """
    def toggle_payment_method_selection(self):
        # Select cash payment method
        self.click_payment_method()  # Open the "Payment method" dialog
        time.sleep(2)
        self.select_cash_payment()  # Select "Cash"
        time.sleep(2)
        self.close_payment_dialog()  # Close the "Payment method" dialog

        # Verify that the cash payment method has been successfully selected
        try:
            assert "Cash" in self.get_selected_payment_method()
            print("Successfully selected cash payment method")
        except:
            print("Failed to select cash payment method")

        time.sleep(2)

        # Select credit card payment method
        self.click_payment_method()
        time.sleep(2)
        self.select_cc_payment()
        time.sleep(2)
        self.close_payment_dialog()

        # Verify that the credit card payment method has been selected
        try:
            assert "Card" in self.get_selected_payment_method()
            print("Successfully selected card payment method")
        except:
            print("Failed to select card payment method")


    """
    Name: is_business_tariff_card_selected   
    Parameters: None
    Returns: None
    
    This method returns True if the "Business" tariff card is selected and False 
    if not
    """            
    def is_business_tariff_card_selected(self):
        return "active" in self.driver.find_element(*self.BUSINESS_TARIFF_IND).get_attribute("class")


    """
    Name: is_sleepy_tariff_card_selected    
    Parameters: None
    Returns: None
    
    This method returns True if the "Sleepy" tariff card is selected and False 
    if not
    """
    def is_sleepy_tariff_card_selected(self):
        return "active" in self.driver.find_element(*self.SLEEPY_TARIFF_IND).get_attribute("class")


    """
    Name: is_holiday_tariff_card_selected    
    Parameters: None
    Returns: None
    
    This method returns True if the "Holiday" tariff card is selected and False 
    if not
    """
    def is_holiday_tariff_card_selected(self):
        return "active" in self.driver.find_element(*self.HOLIDAY_TARIFF_IND).get_attribute("class")


    """
    Name: is_talking_tariff_card_selected    
    Parameters: None
    Returns: None
    
    This method returns True if the "Talking" tariff card is selected and False 
    if not
    """
    def is_talking_tariff_card_selected(self):
        return "active" in self.driver.find_element(*self.TALKING_TARIFF_IND).get_attribute("class")


    """
    Name: is_supportive_tariff_card_selected    
    Parameters: None
    Returns: None
    
    This method returns True if the "Supportive" tariff card is selected 
    and False if not
    """
    def is_supportive_tariff_card_selected(self):
        return "active" in self.driver.find_element(*self.SUPPORTIVE_TARIFF_IND).get_attribute("class")


    """
    Name: is_glossy_tariff_card_selected    
    Parameters: None
    Returns: None
    
    This method returns True if the "Glossy" tariff card is selected and False 
    if not
    """
    def is_glossy_tariff_card_selected(self):
        return "active" in self.driver.find_element(*self.GLOSSY_TARIFF_IND).get_attribute("class")
    
    
    """
    Name: order_ice_cream    
    Parameters: number_of_ice_creams (integer)
    Returns: None
    
    This method orders as many icecreams as specified by the number_of_ice_creams
    parameter.
    """
    def order_ice_cream(self, number_of_ice_creams: int):
        for i in range(number_of_ice_creams):   # For number_of_ice_creams times, run the following loop
            self.click_add_icecream()
            time.sleep(2)
