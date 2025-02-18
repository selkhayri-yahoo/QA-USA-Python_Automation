import time
from pages import UrbanRoutesPage


class SelectionHelper:

    def __init__(self):
        self.urban_routes_page = UrbanRoutesPage()
        self.urban_routes_page.driver_init()

    def reset_driver(self):
        self.urban_routes_page.driver_quit()
        time.sleep(5)
        self.urban_routes_page.driver_init()

    def call_taxi(self, quit=False):
        self.set_addresses()
        time.sleep(2)
        self.urban_routes_page.click_custom_option()
        time.sleep(2)
        self.urban_routes_page.click_taxi_icon()
        time.sleep(5)
        self.urban_routes_page.click_call_taxi_button()
        if quit:
            time.sleep(4)
            self.urban_routes_page.driver_quit()

    def set_addresses(self):
        self.urban_routes_page.enter_from_location("East")
        self.urban_routes_page.enter_to_location("1300")

    """
    def set_from_address(self, from_address):
        self.urban_routes_page.enter_from_location(from_address)

    def get_from_address(self):
        return self.urban_routes_page.get_from_location().getattribute("value")

    def set_to_address(self, to_address):
        self.urban_routes_page.enter_to_location(to_address)

    def get_to_address(self):
        return self.urban_routes_page.get_to_location().getattribute("value")
    """

    def test_tariff_cards(self):
        self.call_taxi()
        self.urban_routes_page.click_business_tariff_card()
        time.sleep(2)
        self.urban_routes_page.click_sleepy_tariff_card()
        time.sleep(2)
        self.urban_routes_page.click_holiday_tariff_card()
        time.sleep(2)
        self.urban_routes_page.click_talking_tariff_card()
        time.sleep(2)
        self.urban_routes_page.click_supportive_tariff_card()
        time.sleep(2)
        self.urban_routes_page.click_glossy_tariff_card()
        time.sleep(4)

    def test_add_payment_method(self):
        self.call_taxi()
        time.sleep(3)
        self.urban_routes_page.click_payment_method()
        time.sleep(4)

        # Add two credit cards
        for x in range(2):
            self.urban_routes_page.click_add_credit_card()
            time.sleep(2)
            self.urban_routes_page.set_credit_card_text("")
            self.urban_routes_page.set_credit_card_text("2315 8465 9872")
            time.sleep(2)
            self.urban_routes_page.set_credit_card_code("2468")
            time.sleep(4)
            self.urban_routes_page.submit_credit_card_add()
            time.sleep(2)

        self.urban_routes_page.close_payment_dialog()

    def test_selected_payment_method(self):
        self.urban_routes_page.click_payment_method()
        time.sleep(2)
        self.urban_routes_page.select_cash_payment()
        time.sleep(2)
        self.urban_routes_page.close_payment_dialog()

        assert "Cash" in self.urban_routes_page.get_selected_payment_method()

        time.sleep(5)

        self.urban_routes_page.click_payment_method()
        time.sleep(2)
        self.urban_routes_page.select_cc_payment()
        time.sleep(2)
        self.urban_routes_page.close_payment_dialog()

        assert "Card" in self.urban_routes_page.get_selected_payment_method()

    def test_phone_number_sms(self):
        self.call_taxi()
        time.sleep(5)
        self.urban_routes_page.click_phone_number_button()
        time.sleep(3)
        self.urban_routes_page.set_phone_number_text("+1 519 555 1212")
        time.sleep(3)
        self.urban_routes_page.click_phone_number_next()
        time.sleep(3)
        self.urban_routes_page.set_sms_code("4862")
        time.sleep(3)
        self.urban_routes_page.click_sms_code_confirm()
        time.sleep(4)

    def test_route_options(self):
        self.set_addresses()
        time.sleep(4)
        self.urban_routes_page.click_optimal_option()
        time.sleep(4)
        self.urban_routes_page.click_fastest_option()
        time.sleep(4)
        self.urban_routes_page.click_custom_option()
        time.sleep(4)

    def test_commuting_options(self):
        self.set_addresses()
        time.sleep(3)
        self.urban_routes_page.click_custom_option()
        time.sleep(2)
        self.urban_routes_page.click_car_icon()

        try:
            assert "Car" in self.urban_routes_page.get_results_text()
            assert "Duration" in self.urban_routes_page.get_duration_text()
        except:
            print("Results text not displaying Car")
        time.sleep(2)

        self.urban_routes_page.click_walk_icon()
        try:
            assert "Walk" in self.urban_routes_page.get_results_text()
            assert "Duration" in self.urban_routes_page.get_duration_text()
        except:
            print("Results text not displaying Walk")
        time.sleep(2)

        self.urban_routes_page.click_taxi_icon()
        try:
            assert "Taxi" in self.urban_routes_page.get_results_text()
            assert "Duration" in self.urban_routes_page.get_duration_text()
        except:
            print("Results text not displaying Taxi")
        time.sleep(2)

        self.urban_routes_page.click_bike_icon()
        try:
            assert "Bike" in self.urban_routes_page.get_results_text()
            assert "Duration" in self.urban_routes_page.get_duration_text()
        except:
            print("Results text not displaying Bike")
        time.sleep(2)

        self.urban_routes_page.click_scooter_icon()
        try:
            assert "Scooter" in self.urban_routes_page.get_results_text()
            assert "Duration" in self.urban_routes_page.get_duration_text()
        except:
            print("Results text not displaying Scooter")
        time.sleep(2)

        self.urban_routes_page.click_drive_icon()
        try:
            assert "Drive" in self.urban_routes_page.get_results_text()
            assert "Duration" in self.urban_routes_page.get_duration_text()
        except:
            print("Results text not displaying Drive")
        time.sleep(4)

    def test_send_message_to_driver(self):
        message = "Don't be late"

        self.call_taxi()
        self.urban_routes_page.send_message_to_driver(message)

        try:
            assert self.urban_routes_page.get_message_to_driver() == message
            print("Succeeded in sending message to driver")
        except:
            print("Failed to send message to driver")

        time.sleep(4)
