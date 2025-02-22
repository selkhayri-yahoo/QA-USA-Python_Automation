import time
import traceback

import logging

import data      # import the data.py file which contains the constant values
import helpers   # import the helpers.py file which contains networking functions

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

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

        chrome_options = Options()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

        logging.basicConfig(filename="logs/log.txt",
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
            raise Exception("Cannot connect to Urban Routes. Check the server is on and still running")

    """
    Name: reload_page    
    Paramaters: None
    Returns: None
    
    This method reloads the urban routes page.
    """
    def reload_page(self):
        # Check if the URL specified by constant URBAN_ROUTES_URL in the data.py file is reachable
        # and print a message accordingly
        self.driver.get(data.URBAN_ROUTES_URL)          # Retrieve the urban routes page
        self.urban_routes_page = UrbanRoutesPage(self.driver)  # Instantiote the Urban

        time.sleep(5)

    """
    Name: set_addresses    
    Parameters: None
    Returns: None
    
    This method sets the source and destination addresses.
    """
    def set_addresses(self):
        self.urban_routes_page.enter_from_location("East")  # Set the "From" address to "East"
        self.urban_routes_page.enter_to_location("1300")   # Set the "To" address to "1300"

    """
    Name: call_taxi    
    Parameters: None
    Returns: None
    
    This method implements all the operations from setting the source and destination addresses to calling a taxi
    """
    def call_taxi(self):
        self.set_addresses()                # Set the "From" and "To" addresses
        time.sleep(2)
        self.urban_routes_page.click_custom_option()  # Select the "Custom" option
        time.sleep(2)
        self.urban_routes_page.click_taxi_icon()   # Click the "taxi" icon
        time.sleep(5)
        self.urban_routes_page.click_call_taxi_button()  # Click the "Call a taxi" button

    """
    Name: set_phone_number    
    Parameters: phone_numbner (string of numbers: +1 XXX XXX XXXX)
    Returns: None
    
    This method sets the phone number field in the Phone number dialog box.
    """
    def set_phone_number(self, phone_number):
        time.sleep(5)
        self.urban_routes_page.click_phone_number_button()    # Open the "Phone number" dialog
        time.sleep(3)
        self.urban_routes_page.set_phone_number_text(phone_number)   # Set the "Phone number"

    """
    Name: get_phone_number    
    Parameters: None
    Returns: The phone number the was entered into the Phone number dialog.
    
    This method gets the phone number the was entered into the Phone number dialog
    """
    def get_phone_number(self):
        self.urban_routes_page.click_phone_number_button()     # Open the "Phone number" dialog
        time.sleep(3)
        return self.urban_routes_page.get_phone_number_text()   # Retrieve and return the "Phone number" field

    """
    Name: add_credit_card_payment    
    Parameters: None
    Returns: None
    
    This method adds a credit card option in the Payment Methods dialog.
    """
    def add_credit_card_payment(self):
        # Open the "Payment Method" dialog
        self.urban_routes_page.click_payment_method()   # Open the "Payment Method" dialog

        # Add a credit card number and code
        try:
            time.sleep(4)
            self.urban_routes_page.click_add_credit_card()  # Open the "Add a card" dialog box
            time.sleep(4)
            self.urban_routes_page.set_credit_card_text("1234 5678 9012")   # Enter credit card number
            time.sleep(4)
            self.urban_routes_page.set_credit_card_code("4970")  # Enter credit card code
            time.sleep(4)
            self.urban_routes_page.submit_credit_card_add()     # Click link to add credit card and close the "Add a card" dialog
            time.sleep(4)
            self.urban_routes_page.close_payment_method_dialog()   # Close the "Payment Method" dialog
            time.sleep(4)
            logging.log(logging.INFO, "Successfully filled card: add credit card")  # Log success
        except:
            logging.log(logging.ERROR, "Failed to fill card: add credit card")  # log failure

    """
    Name: toggle_payment_method_selection
    Parameters: None
    Returns: None
    
    This method tests the ability to toggle between cash payment and credit card payment.
    """
    def toggle_payment_method_selection(self):
        # Select cash payment method
        self.urban_routes_page.click_payment_method()   # Open the "Payment method" dialog
        time.sleep(2)
        self.urban_routes_page.select_cash_payment()    # Select "Cash"
        time.sleep(2)
        self.urban_routes_page.close_payment_dialog()   # Close the "Payment method" dialog

        # Verify that the cash payment method has been successfully selected
        try:
            assert "Cash" in self.urban_routes_page.get_selected_payment_method()
            logging.log(logging.INFO, "Successfully selected cash payment method")
        except:
            logging.log(logging.ERROR, "Failed to select cash payment method")

        time.sleep(2)

        # Select credit card payment method
        self.urban_routes_page.click_payment_method()
        time.sleep(2)
        self.urban_routes_page.select_cc_payment()
        time.sleep(2)
        self.urban_routes_page.close_payment_dialog()

        # Verify that the credit card payment method has been selected
        try:
            assert "Card" in self.urban_routes_page.get_selected_payment_method()
            logging.log(logging.INFO, "Successfully selected card payment method")
        except:
            logging.log(logging.ERROR, "Failed to select card payment method")

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

            logging.log(logging.INFO, "Successfully set route")  #   "Log success"

        except Exception as e:
            logging.log(logging.ERROR,
                        f"Failed to set route. Exception: {traceback.format_exception(e)}.")  # Log failure


        self.reload_page()    # Reload the Urban Routes page in preparation for the next test


    """
    Name: test_select_plan
    Parameters: None
    Return: None

    This method tests the ability of the users to select their travel plan mode
    """
    def test_select_plan(self):
        self.set_addresses()        # Set the "From" and "To" addresses
        time.sleep(5)
        self.urban_routes_page.click_optimal_option()   # Select the "Optimal" plan

        try:
            assert "active" in self.urban_routes_page.get_optimal_option_status()  # Check that the "Optimal" plan is now active
            logging.log(logging.INFO, "Successfully selected optimal plan")  # Log success
        except:
            logging.log(logging.ERROR, "Failed to select optimal plan")   # Log failure

        time.sleep(5)

        self.urban_routes_page.click_fastest_option()  # Select the "Fastest" plan

        try:
            assert "active" in self.urban_routes_page.get_fastest_option_status()  # Check that the "Fastest" plan is now active
            logging.log(logging.INFO, "Successfully selected fastest plan")  # Log success
        except:
            logging.log(logging.ERROR, "Failed to select fastest plan")     # Log failure

        self.urban_routes_page.click_custom_option()   # Select the "Custom" plan

        try:
            assert "active" in self.urban_routes_page.get_custom_option_status()  # Check that the "Custom" plan is now active
            logging.log(logging.INFO, "Successfully selected custom plan")   # Log success
        except:
            logging.log(logging.ERROR, "Failed to select custom plan")       # Log failure

        self.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_fill_phone_number
    Parameters: None
    Return: None

    This method tests the ability of the user to enter their phone number into the Urban Routes web service
    """
    def test_fill_phone_number(self):
        self.call_taxi()         # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"
        phone_number = "+1 519 555 1212"       # The test phone number
        self.set_phone_number(phone_number)     # Call the set_phone_number method with the phone_number as an argument
        self.urban_routes_page.click_phone_number_close()   # Close the Phone number dialog
        retrieved_phone_number = self.get_phone_number()    # Retrieve the saved phone number from the app

        try:
            assert retrieved_phone_number == phone_number  # Verify that the retrieved phone number matches the original
            logging.log(logging.INFO, "Successfully set phone number")  # Log success
        except:
            logging.log(logging.ERROR, "Failed to set phone number. Expecting "
                        + str(phone_number) + ", Retrieved: " + str(retrieved_phone_number))  # Log failure

        self.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_fill_card
    Parameters: None
    Return: None

    This method tests the ability of the user to add a credit card to the Urban Routes web service
    """
    def test_fill_card(self):
        self.call_taxi()   # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"
        time.sleep(4)
        self.add_credit_card_payment()  # Add a credit card payment method
        time.sleep(4)
        self.toggle_payment_method_selection()  # Test toggling between cash and credit card payment methods

        self.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_comment_for_driver
    Parameters: None
    Return: None

    This method tests the comment_for_driver method of the Urban Routes web service
    """
    def test_comment_for_driver(self):
        self.call_taxi()  # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"

        comment_for_driver = "Do not be late!"  # The test comment for driver
        self.urban_routes_page.send_message_to_driver(comment_for_driver)  # Call send_message_to_driver method of UrbanRoutesPage
                                                                           # with test address
        retrieved_comment_for_driver = self.urban_routes_page.get_message_to_driver() # Retrieve the address
                                                                                      # that is stored in the app
        try:
            assert comment_for_driver == retrieved_comment_for_driver   # Verify that stored address matches test address
            logging.log(logging.INFO, "Successfully commented for driver")  # Log success
        except:
            logging.log(logging.ERROR, "Failed to commented for driver")  # Log failure

        self.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_order_blanket_and_handkerchiefs
    Parameters: None
    Return: None

    This method tests the ability of users to order a blanket and handkerchiefs from the Urban Routes web service
    """
    def test_order_blanket_and_handkerchiefs(self):
        self.call_taxi()     # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"
        self.urban_routes_page.click_supportive_tariff_card()  # Click the "Supportive" option
        time.sleep(2)

        self.urban_routes_page.click_order_requirements()   # Click on the "Order requirements" button
        time.sleep(2)
        first_value = self.urban_routes_page.get_blanket_and_handkerchiefs_checkbox_value()  # Get the state of the "Blanket and Handkerchiefs" toggle switch

        self.urban_routes_page.click_blanket_and_handkerchiefs()    # Click the "Blanket and Handkerchiefs" toggle switch
        second_value = self.urban_routes_page.get_blanket_and_handkerchiefs_checkbox_value()  # Get the new state of the "Blanket and Handkerchiefs" toggle switch
        time.sleep(2)

        self.urban_routes_page.click_blanket_and_handkerchiefs()    # Click the "Blanket and Handkerchiefs" toggle switch
        third_value = self.urban_routes_page.get_blanket_and_handkerchiefs_checkbox_value() # Get the new state of the "Blanket and Handkerchiefs" toggle switch

        try:   # Verify that the toggle switch state changed and then changed back
            assert first_value != second_value and second_value != third_value and first_value == third_value
            logging.log(logging.INFO, "Successfully set blanket and handkerchiefs")  # Log success
        except:
            logging.log(logging.ERROR, "Failed to set blanket and handkerchiefs")   # Log failure

        self.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_order_2_ice_creams
    Parameters: None
    Return: None

    This method tests the ability of users to order two icecream from the Urban Routes web service
    """
    def test_order_2_ice_creams(self):
        self.call_taxi()   # Enter "From" and "To" addresses, "Custom" option, "Taxi", then click "Call a taxi"
        self.urban_routes_page.click_supportive_tariff_card()  # Click the "Supportive" option
        time.sleep(2)
        self.urban_routes_page.click_order_requirements()   # Click on the "Order requirements" button
        time.sleep(2)

        # A variable should be defined and then loop should iterate twice ...
        number_of_ice_creams = 2   # the number of ice creams to order
        for i in range(number_of_ice_creams):   # For number_of_ice_creams times, run the following loop
            self.urban_routes_page.click_add_icecream()     # Click "+" on the left of "Ice cream" in "Ice cream bucket"
            time.sleep(1)


        try:    # Verify that the number of ice creams displayed in the app is number_of_ice_creams
            assert str(number_of_ice_creams) == self.urban_routes_page.get_icecream_count()
            logging.log(logging.INFO, "Successfully set icecream count")  # Log success
        except:
            msg = (f"Failed to set icecream count; Number of ice creams needed: {number_of_ice_creams}, "
                   f"Number of ice creams set: {self.urban_routes_page.get_icecream_count()}.")
            logging.log(logging.ERROR, msg)   # Log failure

        self.reload_page()    # Reload the Urban Routes page in preparation for the next test

    """
    Name: test_car_search_model_appears
    Parameters: None
    Return: None

    This method tests the users' ability to select which car to book in the Urban Routes web service
    """
    def test_car_search_model_appears(self):
        self.set_addresses()    # Set the "From" and "To" addresses
        time.sleep(2)
        self.urban_routes_page.click_custom_option()   # Select the "Custom" option
        time.sleep(2)
        self.urban_routes_page.click_drive_icon()   # Select the "Drive" icon
        time.sleep(4)
        self.urban_routes_page.click_book_button()  # Click the "Book" button
        time.sleep(2)
        try:
            assert self.urban_routes_page.is_tariff_picker_shown() == True      # Verify that the car selection dialog is displayed
            logging.log(logging.INFO, "Successfully shown car search model")  # Log success
        except Exception as e:
            logging.log(logging.ERROR, f"Failed to show car search model. Error: {str(e)}")  # Log failure

        self.reload_page()    # Reload the Urban Routes page in preparation for the next test

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



test_urban_routes = TestUrbanRoutes()
test_urban_routes.setup_class()
test_urban_routes.test_set_route()
test_urban_routes.test_select_plan()
test_urban_routes.test_fill_phone_number()
test_urban_routes.test_comment_for_driver()
test_urban_routes.test_order_blanket_and_handkerchiefs()
test_urban_routes.test_order_2_ice_creams()
test_urban_routes.test_car_search_model_appears()
test_urban_routes.test_fill_card()

time.sleep(10)
test_urban_routes.teardown_class()

