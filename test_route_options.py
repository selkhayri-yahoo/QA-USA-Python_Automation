import time

from selenium import webdriver
from pages import UrbanRoutesPage
import data

driver = webdriver.Chrome()

driver.get(data.URBAN_ROUTES_URL)

urban_routes_page = UrbanRoutesPage(driver)

urban_routes_page.enter_from_location("East")
urban_routes_page.enter_to_location("1300")

time.sleep(2)

urban_routes_page.click_optimal_option()

time.sleep(2)

urban_routes_page.click_fastest_option()

time.sleep(2)

urban_routes_page.click_custom_option()

time.sleep(2)

driver.quit()

