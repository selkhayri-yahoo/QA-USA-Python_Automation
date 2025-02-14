import time

from selenium import webdriver
from pages import UrbanRoutesPage
import data

driver = webdriver.Chrome()

try:
    driver.get(data.URBAN_ROUTES_URL)

    urban_routes_page = UrbanRoutesPage(driver)

    urban_routes_page.enter_from_location("East")
    urban_routes_page.enter_to_location("1300")

    time.sleep(2)

    urban_routes_page.click_custom_option()

    time.sleep(2)

    urban_routes_page.click_taxi_icon()

    time.sleep(5)

    urban_routes_page.click_call_taxi_button()

    time.sleep(3)

    urban_routes_page.click_business_tariff_card()

    time.sleep(3)

    urban_routes_page.click_sleepy_tariff_card()

    time.sleep(3)

    urban_routes_page.click_holiday_tariff_card()

    time.sleep(3)

    urban_routes_page.click_talking_tariff_card()

    time.sleep(3)

    urban_routes_page.click_supportive_tariff_card()

    time.sleep(3)

    urban_routes_page.click_glossy_tariff_card()

    time.sleep(3)


finally:
    driver.quit()