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

    urban_routes_page.click_phone_number_button()

    time.sleep(3)

    urban_routes_page.set_phone_number_text("+1 519 555 1212")

    time.sleep(3)

finally:

    driver.quit()