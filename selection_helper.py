import time

from pages import UrbanRoutesPage
import data

class SelectionHelper:

    def __init__(self,urbanroutespage):
        self.urban_routes_page = urbanroutespage

    def call_taxi(self):

        self.set_addresses()
        time.sleep(2)
        self.urban_routes_page.click_custom_option()
        time.sleep(2)
        self.urban_routes_page.click_taxi_icon()
        time.sleep(5)
        self.urban_routes_page.click_call_taxi_button()


    def set_addresses(self):
        self.urban_routes_page.enter_from_location("East")
        self.urban_routes_page.enter_to_location("1300")

    def test_tariff_cards(self):
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
