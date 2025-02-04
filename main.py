import helpers

'''
Class TestUrnanRoutes

This class is used to test the functionality of the Urban Routes web app

Class variables
urban_routes_server (str): the url of the Urban Routes server web service under test
'''
class TestUrbanRoutes:
    # Name: setup_class
    # Parameters: None
    # Return: None
    #
    # This is the class constructor. It establishes the connection with the Urban Routes web service
    @classmethod
    def setup_class(cls, urban_routes_server):
        # Check if the URL specified by constant URBAN_ROUTES_URL in the data.py file is reachable
        # and print a message accordingly
        if helpers.is_url_reachable(urban_routes_server):
            print("Connected to the Urban Routes server")
        else:
            # Connection to Urban Routes web service failed
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Name: test_set_route
    # Parameters: None
    # Return: None
    #
    # THis method tests the set_route method of the Urban Routes web service
    def test_set_route(self):
        # Add in S8
        print("function created for set route")
        pass

    # Name: test_select_plan
    # Parameters: None
    # Return: None
    #
    # THis method tests the select_plan method of the Urban Routes web service
    def test_select_plan(self):
        # Add in S8
        print("function created for set route")
        pass

    # Name: test_fill_phone_number
    # Parameters: None
    # Return: None
    #
    # THis method tests the fill_phone_number method of the Urban Routes web service
    def test_fill_phone_number(self):
        # Add in S8
        print("function created for set route")
        pass

    # Name: test_fill_card
    # Parameters: None
    # Return: None
    #
    # THis method tests the fill_card method of the Urban Routes web service
    def test_fill_card(self):
        # Add in S8
        print("function created for set route")
        pass

    # Name: test_comment_for_driver
    # Parameters: None
    # Return: None
    #
    # THis method tests the comment_for_driver method of the Urban Routes web service
    def test_comment_for_driver(self):
        # Add in S8
        print("function created for set route")
        pass

    # Name: test_order_blanket_and_handkerchiefs
    # Parameters: None
    # Return: None
    #
    # THis method tests the order_blanket_and_handkerchiefs method of the Urban Routes web service
    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for set route")
        pass

    # Name: test_order_2_ice_creams
    # Parameters: None
    # Return: None
    #
    # THis method tests the order_2_ice_creams method of the Urban Routes web service
    def test_order_2_ice_creams(self):
        # Add in S8
        print("function created for set route")

        # Iterate through the two icecream orders and do something ...
        for i in range(2):
            # Add in S8
            pass

        pass

    # Name: test_car_search_model_appears
    # Parameters: None
    # Return: None
    #
    # THis method tests the car_search_model_appears method of the Urban Routes web service
    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for set route")
        pass
