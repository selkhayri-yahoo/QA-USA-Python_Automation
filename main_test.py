from selection_helper import SelectionHelper
import time

# initialize SelectionHelper class
select_helper = SelectionHelper()

# test route options
time.sleep(3)
select_helper.test_route_options()

# test call taxi
select_helper.reset_driver()
select_helper.call_taxi()
time.sleep(2)

# test tariff cards
select_helper.reset_driver()
select_helper.test_tariff_cards()

time.sleep(2)

# test payment method
select_helper.reset_driver()
select_helper.test_payment_method()

time.sleep(2)

# test phone number / sms
select_helper.reset_driver()
select_helper.test_phone_number_sms()

time.sleep(2)

# test commuting options
select_helper.reset_driver()
select_helper.test_commuting_options()

time.sleep(2)





