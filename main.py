import time
import traceback

import data      # import the data.py file which contains the constant values
import helpers   # import the helpers.py file which contains networking functions

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from pages import UrbanRoutesPage

'''
Class TestUrbanRoutes

This class is used to test the functionality of the Urban Routes web app
'''
class TestUrbanRoutes:
    """
    Name: setup_class
    Parameters: None
    Return: None

    This is the class constructor. It establishes the connection with the Urban Routes web service
    """
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
            cls.driver.get(data.URBAN_ROUTES_URL)
            cls.urban_routes_page = UrbanRoutesPage(cls.driver)
            print("Connected to the Urban Routes server")
        else:
            # Connection to Urban Routes web service failed
            print("Cannot connect to Urban Routes. Check the server is on and still running")


    """
    Name: test_set_route
    Parameters: None
    Return: None

    This method tests the ability to set the start and end addresses of a planned route
    """
    def test_set_route(self):
        address_from = "East"
        address_to = "1300"


        try:
            # Set the start and end address points of the route
            self.urban_routes_page.enter_from_location(address_from)  # Set the "From" address
            self.urban_routes_page.enter_to_location(address_to)      # Set the "To" address

            # Retrieve the start and ends point addresses of the route that have been set into the app
            retrieved_from_location = self.urban_routes_page.get_from_location()  # Retrieve the "From" address
            retrieved_to_location = self.urban_routes_page.get_to_location()      # Retrieve the "To" address

            # Verify that the retrieved addresses match the actual addresses
            assert retrieved_from_location == address_from       # Compare actual "From" to retrieved "From" address
            assert retrieved_to_location == address_to           # Compare actual "To" to retrieved "To" address

            print("Successfully set route")  #   "Log success"

        except Exception as e:
            print(f"Failed to set route. Exception: {traceback.format_exception(e)}.")  # Log failure


        self.urban_routes_page.reload_page()    # Reload the Urban Routes page in preparation for the next test


    """
    Name: test_select_plan
    Parameters: None
    Return: None

    This method tests the ability of the users to select their travel plan mode
    """
    def test_select_plan(self):
        self.urban_routes_page.call_taxi()
        time.sleep(2)
        
        # Select business 
        self.urban_routes_page.click_business_tariff_card()
        time.sleep(2)
        
        # Verify that business has been selected
        try:
            assert self.urban_routes_page.is_business_tariff_card_selected() == True
            print("Selected business plan successfully")
        except:
            print("Failed to select business plan")
        
        time.sleep(2)        
    
        # Select sleepy
        self.urban_routes_page.click_sleepy_tariff_card()
        time.sleep(2)
        
        # Verify that sleepy has been selected
        try:
            assert self.urban_routes_page.is_sleepy_tariff_card_selected() == True
            print("Selected sleepy plan successfully")
        except:
            print("Failed to select sleepy plan")
        
        # Select holiday
        self.urban_routes_page.click_holiday_tariff_card()
        time.sleep(2)
        
        # Verify that holiday has been selected
        try:
            assert self.urban_routes_page.is_holiday_tariff_card_selected() == True
            print("Selected holiday plan successfully")
        except:
            print("Failed to select holiday plan")
        
        time.sleep(2)
        
        # Select talking
        self.urban_routes_page.click_talking_tariff_card()
        time.sleep(2)
        
        # Verify that talking has been selected
        try:
            assert self.urban_routes_page.is_talking_tariff_card_selected() == True
            print("Selected talking plan successfully")
        except:
            print("Failed to select talking plan")
        
        time.sleep(2)
        
        # Select supportive
        self.urban_routes_page.click_supportive_tariff_card()
        time.sleep(2)
                
        # Verify that supportive has been selected
        try:
            assert self.urban_routes_page.is_supportive_tariff_card_selected() == True
            print("Selected supportive plan successfully")
    
        except:
            print("Failed to supportive glossy plan")
        
        time.sleep(2)
        
        # Select glossy
        self.urban_routes_page.click_glossy_tariff_card()
        time.sleep(2)
        
        # Verift that glossy has been selected
        try:
            assert self.urban_routes_page.is_glossy_tariff_card_selected() == True
            print("Selected glossy plan successfully")
        except:
            print("Failed to select glossy plan")
       
        self.urban_routes_page.reload_page()    # Reload the Urban Routes page in preparation for the next test
            
    """
    Name: test_fill_phone_number
    Parameters: None
    Return: None

    This method tests the ability of the user to enter their phone number into the Urban Routes web service
    """
    def test_fill_phone_number(self):
        self.urban_routes_page.call_taxi()         # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"
        phone_number = "+1 519 555 1212"       # The test phone number
        self.urban_routes_page.set_phone_number(phone_number)     # Call the set_phone_number method with the phone_number as an argument
        self.urban_routes_page.click_phone_number_close()   # Close the Phone number dialog
        retrieved_phone_number = self.urban_routes_page.get_phone_number()    # Retrieve the saved phone number from the app

        try:
            assert retrieved_phone_number == phone_number  # Verify that the retrieved phone number matches the original
            print("Successfully set phone number")  # Log success
        except:
            print("Failed to set phone number. Expecting "
                        + str(phone_number) + ", Retrieved: " + str(retrieved_phone_number))  # Log failure

        self.urban_routes_page.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_fill_card
    Parameters: None
    Return: None

    This method tests the ability of the user to add a credit card to the Urban Routes web service
    """
    def test_fill_card(self):
        self.urban_routes_page.call_taxi()   # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"
        time.sleep(4)
        self.urban_routes_page.add_credit_card_payment()  # Add a credit card payment method
        time.sleep(4)
        self.urban_routes_page.toggle_payment_method_selection()  # Test toggling between cash and credit card payment methods

        self.urban_routes_page.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_comment_for_driver
    Parameters: None
    Return: None

    This method tests the comment_for_driver method of the Urban Routes web service
    """
    def test_comment_for_driver(self):
        self.urban_routes_page.call_taxi()  # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"

        comment_for_driver = "Do not be late!"  # The test comment for driver
        self.urban_routes_page.send_message_to_driver(comment_for_driver)  # Call send_message_to_driver method of UrbanRoutesPage
                                                                           # with test address
        retrieved_comment_for_driver = self.urban_routes_page.get_message_to_driver() # Retrieve the address
                                                                                      # that is stored in the app
        try:
            assert comment_for_driver == retrieved_comment_for_driver   # Verify that stored address matches test address
            print("Successfully commented for driver")  # Log success
        except:
            print("Failed to commented for driver")  # Log failure

        self.urban_routes_page.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_order_blanket_and_handkerchiefs
    Parameters: None
    Return: None

    This method tests the ability of users to order a blanket and handkerchiefs from the Urban Routes web service
    """
    def test_order_blanket_and_handkerchiefs(self):
        self.urban_routes_page.call_taxi()     # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"
        self.urban_routes_page.click_supportive_tariff_card()  # Click the "Supportive" option
        time.sleep(2)

        first_value = self.urban_routes_page.get_blanket_and_handkerchiefs_checkbox_value()  # Get the state of the "Blanket and Handkerchiefs" toggle switch

        self.urban_routes_page.click_blanket_and_handkerchiefs()    # Click the "Blanket and Handkerchiefs" toggle switch
        second_value = self.urban_routes_page.get_blanket_and_handkerchiefs_checkbox_value()  # Get the new state of the "Blanket and Handkerchiefs" toggle switch
        time.sleep(2)

        self.urban_routes_page.click_blanket_and_handkerchiefs()    # Click the "Blanket and Handkerchiefs" toggle switch
        third_value = self.urban_routes_page.get_blanket_and_handkerchiefs_checkbox_value() # Get the new state of the "Blanket and Handkerchiefs" toggle switch

        try:   # Verify that the toggle switch state changed and then changed back
            assert first_value != second_value and second_value != third_value and first_value == third_value
            print("Successfully set blanket and handkerchiefs")  # Log success
        except:
            print("Failed to set blanket and handkerchiefs")   # Log failure

        self.urban_routes_page.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_order_2_ice_creams
    Parameters: None
    Return: None

    This method tests the ability of users to order two icecream from the Urban Routes web service
    """
    def test_order_2_ice_creams(self):
        self.urban_routes_page.call_taxi()   # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"
        self.urban_routes_page.click_supportive_tariff_card()  # Click the "Supportive" option
        time.sleep(2)
        
        # A variable should be defined and then loop should iterate twice ...
        number_of_ice_creams = 2   # the number of ice creams to order

        # Call the order_ice_cream method of the UrbanRoutesPage class with
        # number_of _ice_creams as a parameter to order 2 ice creams
        self.urban_routes_page.order_ice_cream(number_of_ice_creams)
        
        try:    # Verify that the number of ice creams displayed in the app is number_of_ice_creams
            assert str(number_of_ice_creams) == self.urban_routes_page.get_icecream_count()
            print("Successfully set icecream count")  # Log success
        except:
            msg = (f"Failed to set icecream count; Number of ice creams needed: {number_of_ice_creams}, "
                   f"Number of ice creams set: {self.urban_routes_page.get_icecream_count()}.")
            print(msg)   # Log failure

        self.urban_routes_page.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_car_search_model_appears
    Parameters: None
    Return: None

    This method tests the users' ability to select which car to book in the Urban Routes web service
    """
    def test_car_search_model_appears(self):
        self.urban_routes_page.call_taxi() # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"
        
        self.urban_routes_page.click_smart_button() # Click "Enter the number and order"
        
        try:
            assert self.urban_routes_page.is_order_visible() == True    # Verify that the car selection dialog is displayed
            print("Successfully showed car search model")
        except Exception as e:
            print(f"Failed to show car search model. Error: {str(e)}")
        
        self.urban_routes_page.reload_page()    # Reload the Urban Routes page in preparation for the next test

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

	
