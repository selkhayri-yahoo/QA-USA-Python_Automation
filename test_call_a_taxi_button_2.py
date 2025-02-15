import time

from selenium import webdriver
from pages import UrbanRoutesPage
from selection_helper import SelectionHelper
import data

driver = webdriver.Chrome()
driver.get(data.URBAN_ROUTES_URL)
urban_routes_page = UrbanRoutesPage(driver)
select_helper = SelectionHelper(urban_routes_page)

try:
    select_helper.call_taxi()
    time.sleep(2)
    select_helper.test_tariff_cards()
    time.sleep(2)

finally:
    driver.quit()