'''
File: data.py

This file contains the constants that are used in the API call to the Urban Routes web service.

ADDRESS_FROM: The source address from which route navigatioon is to start
ADDRESS_TO: The destination address at which route navigation is to end
PHONE_NUMBER: The phone number of the person making the navigation request
CARD_NUMNER: The number of the credit card of the person making the navigation request
CARD_CODE: The verification code of the credit card of the person making the navigation request
MESSAGE_FOR_DRIVER: Any special instructions to be relayed to the driver to be dispatched
URBAN_ROUTES_URL: The URL of the most recent instance of the Urban Routes web service
'''

ADDRESS_FROM	    = 'East 2nd Street, 601'
ADDRESS_TO	        = '1300 1st St'
PHONE_NUMBER	    = '+1 123 123 12 12'
CARD_NUMBER	        = '1234 5678 9100'
CARD_CODE	        = '1111'
MESSAGE_FOR_DRIVER  = 'Stop at the juice bar, please'
URBAN_ROUTES_URL    = 'https://cnt-bd505674-5f4a-4057-8d2f-ce291709998c.containerhub.tripleten-services.com'
