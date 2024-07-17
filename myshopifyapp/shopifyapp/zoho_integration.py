# shopifyapp/zoho_integration.py
import requests
from django.conf import settings

ZOHO_CLIENT_ID = 'your_zoho_client_id'
ZOHO_CLIENT_SECRET = 'your_zoho_client_secret'
ZOHO_REFRESH_TOKEN = 'your_zoho_refresh_token'

# def get_zoho_access_token():
#     url = 'https://accounts.zoho.com/oauth/v2/token'
#     params = {
#         'refresh_token': ZOHO_REFRESH_TOKEN,
#         'client_id': ZOHO_CLIENT_ID,
#         'client_secret': ZOHO_CLIENT_SECRET,
#         'grant_type': 'refresh_token'
#     }
#     response = requests.post(url, params=params)
#     response_data = response.json()
#     return response_data['access_token']

def create_contact_in_zoho(contact_data):
    # access_token = get_zoho_access_token()
    # url = 'https://www.zohoapis.com/crm/v2/Contacts'
    # headers = {
    #     'Authorization': f'Zoho-oauthtoken {access_token}'
    # }
    # response = requests.post(url, json=contact_data, headers=headers)
    # return response.json()

    Subscriber.objects.create(contact_data)
    return True
