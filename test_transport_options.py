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

    urban_routes_page.click_car_icon()

    time.sleep(2)

    urban_routes_page.click_walk_icon()

    time.sleep(2)

    urban_routes_page.click_taxi_icon()

    time.sleep(2)

    urban_routes_page.click_bike_icon()

    time.sleep(2)

    urban_routes_page.click_scooter_icon()

    time.sleep(2)

    urban_routes_page.click_drive_icon()

    time.sleep(4)

finally:

    driver.quit()

