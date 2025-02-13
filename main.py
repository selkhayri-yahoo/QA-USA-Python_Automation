import data      # import the data.py file which contains the constant values
import helpers   # import the helpers.py file which contains networking functions

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
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
        cls.driver = webdriver.Chrome()

        # Check if the URL specified by constant URBAN_ROUTES_URL in the data.py file is reachable
        # and print a message accordingly
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            # Connection to Urban Routes web service failed
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Name: test_set_route
    # Parameters: None
    # Return: None
    #
    # This method tests the set_route method of the Urban Routes web service
    def test_set_route(self):
        # Add in S8
        print("function created for set_route")
        pass

    # Name: test_select_plan
    # Parameters: None
    # Return: None
    #
    # This method tests the select_plan method of the Urban Routes web service
    def test_select_plan(self):
        # Add in S8
        print("function created for select_plan")
        pass

    # Name: test_fill_phone_number
    # Parameters: None
    # Return: None
    #
    # This method tests the fill_phone_number method of the Urban Routes web service
    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill_phone_number")
        pass

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
test_urban_routes.teardown_class()
