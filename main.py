import logging

import data      # import the data.py file which contains the constant values
import helpers   # import the helpers.py file which contains networking functions

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.chrome.options import Options

from pages import UrbanRoutesPage
import time

# from selection_helper_library import SelectionHelper
'''
Class TestUrbanRoutes

This class is used to test the functionality of the Urban Routes web app
'''
class TestUrbanRoutes:
    # Name: setup_class
    # Parameters: None
    # Return: None
    #
    # This is the class constructor. It establishes the connection with the Urban Routes web service
    @classmethod
    def setup_class(cls):
        # Add in S8
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        chrome_options = Options()
        #chrome_options.add_argument("--disable-extensions")
        #cls.driver = webdriver.Chrome(options=chrome_options)
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

        logging.basicConfig(filename="log.txt",
                            filemode='a',
                            format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            level=logging.INFO)

        # Check if the URL specified by constant URBAN_ROUTES_URL in the data.py file is reachable
        # and print a message accordingly
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            cls.driver.get(data.URBAN_ROUTES_URL)
            cls.urban_routes_page = UrbanRoutesPage(cls.driver)
            logging.log(logging.INFO, "Connected to the Urban Routes server")
        else:
            # Connection to Urban Routes web service failed
            logging.log(logging.ERROR, "Cannot connect to Urban Routes. Check the server is on and still running")

    def set_addresses(self):
        self.urban_routes_page.enter_from_location("East")
        self.urban_routes_page.enter_to_location("1300")

    def call_taxi(self, quit=False):
        self.set_addresses()
        time.sleep(2)
        self.urban_routes_page.click_custom_option()
        time.sleep(2)
        self.urban_routes_page.click_taxi_icon()
        time.sleep(5)
        self.urban_routes_page.click_call_taxi_button()

    def set_phone_number_code(self, phone_number, code):
        time.sleep(5)
        self.urban_routes_page.click_phone_number_button()
        time.sleep(3)
        self.urban_routes_page.set_phone_number_text(phone_number)
        time.sleep(3)
        self.urban_routes_page.click_phone_number_next()
        time.sleep(3)
        self.urban_routes_page.set_sms_code(code)
        time.sleep(3)
        self.urban_routes_page.click_sms_code_confirm()
        time.sleep(4)
        self.urban_routes_page.click_sms_code_close()

    def get_phone_number_code(self):
        self.urban_routes_page.click_phone_number_button()
        time.sleep(3)
        phone_number = self.urban_routes_page.get_phone_number_text()
        time.sleep(3)
        self.urban_routes_page.click_phone_number_next()
        time.sleep(3)
        code = self.urban_routes_page.get_sms_code_text()
        self.urban_routes_page.click_sms_code_close()
        
        return (phone_number, code)


    # Name: test_set_route
    # Parameters: None
    # Return: None
    #
    # This method tests the set_route method of the Urban Routes web service
    def test_set_route(self):
        # Add in S8
        logging.log(logging.INFO, "function created for set_route")
        address_from = "East"
        address_to = "1300"

        try:
            self.urban_routes_page.enter_from_location(address_from)
            self.urban_routes_page.enter_to_location(address_to)

            actual_from_location = self.urban_routes_page.get_from_location()
            actual_to_location = self.urban_routes_page.get_to_location()

            assert actual_from_location == address_from
            assert actual_to_location == address_to

            logging.log(logging.INFO, "Successfully set route")
        except:
            logging.log(logging.ERROR, "Failed to set route")




    # Name: test_select_plan
    # Parameters: None
    # Return: None
    #
    # This method tests the select_plan method of the Urban Routes web service
    def test_select_plan(self):
        # Add in S8
        print("function created for select_plan")
        self.set_addresses()
        time.sleep(5)
        self.urban_routes_page.click_optimal_option()

        try:
            assert "active" in self.urban_routes_page.get_optimal_option_status()
            logging.log(logging.INFO, "Successfully selected optimal plan")
        except:
            logging.log(logging.ERROR, "Failed to select optimal plan")

        time.sleep(5)

        self.urban_routes_page.click_fastest_option()

        try:
            assert "active" in self.urban_routes_page.get_fastest_option_status()
            logging.log(logging.INFO, "Successfully selected fastest plan")
        except:
            logging.log(logging.ERROR, "Failed to select fastest plan")

        self.urban_routes_page.click_custom_option()

        try:
            assert "active" in self.urban_routes_page.get_custom_option_status()
            logging.log(logging.INFO, "Successfully selected custom plan")
        except:
            logging.log(logging.ERROR, "Failed to select custom plan")



    # Name: test_fill_phone_number
    # Parameters: None
    # Return: None
    #
    # This method tests the fill_phone_number method of the Urban Routes web service
    def test_fill_phone_number(self):
        # Add in S8
        self.call_taxi()
        phone_number = "+1 519 555 1212"
        code = "4862"

        self.set_phone_number_code(phone_number, code)

        time.sleep(5)

        retrieved_phone_number, retrieved_code = self.get_phone_number_code()

        try:
            assert retrieved_phone_number == phone_number
            logging.log(logging.INFO, "Successfully set phone number")
        except:
            logging.log(logging.ERROR, "Failed to set phone number")

        try:
            assert retrieved_code == code
            logging.log(logging.INFO, "Successfully set code")
        except:
            logging.log(logging.ERROR, "Failed to set code")



    # Name: test_fill_card
    # Parameters: None
    # Return: None
    #
    # This method tests the fill_card method of the Urban Routes web service
    def test_fill_card(self):
        # Add in S8
        print("function created for fill_card")
        pass

    # Name: test_comment_for_driver
    # Parameters: None
    # Return: None
    #
    # This method tests the comment_for_driver method of the Urban Routes web service
    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment_for_driver")
        pass

    # Name: test_order_blanket_and_handkerchiefs
    # Parameters: None
    # Return: None
    #
    # This method tests the order_blanket_and_handkerchiefs method of the Urban Routes web service
    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for order_blanket_and_handkerchiefs")
        pass

    # Name: test_order_2_ice_creams
    # Parameters: None
    # Return: None
    #
    # This method tests the order_2_ice_creams method of the Urban Routes web service
    def test_order_2_ice_creams(self):
        # Add in S8
        print("function created for order_2_ice_creams")

        # A variable should be defined and then loop should iterate twice ...
        number_of_ice_creams = 2   # the number of ice creams to order
        for i in range(number_of_ice_creams):
            # Add in S8
            pass

        pass

    # Name: test_car_search_model_appears
    # Parameters: None
    # Return: None
    #
    # This method tests the car_search_model_appears method of the Urban Routes web service
    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car_search_model_appears")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



test_urban_routes = TestUrbanRoutes()
test_urban_routes.setup_class()
time.sleep(10)
# test_urban_routes.test_set_route()
# test_urban_routes.test_select_plan()
test_urban_routes.test_fill_phone_number()
time.sleep(10)
test_urban_routes.teardown_class()

