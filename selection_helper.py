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

    def test_payment_method(self):
        self.call_taxi()
        time.sleep(3)
        self.urban_routes_page.click_payment_method()
        time.sleep(4)
        #################
        # NOT COMPLETE
        #################

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
        time.sleep(2)
        self.urban_routes_page.click_walk_icon()
        time.sleep(2)
        self.urban_routes_page.click_taxi_icon()
        time.sleep(2)
        self.urban_routes_page.click_bike_icon()
        time.sleep(2)
        self.urban_routes_page.click_scooter_icon()
        time.sleep(2)
        self.urban_routes_page.click_drive_icon()

        time.sleep(4)