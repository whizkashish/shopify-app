import requests

def get_zoho_access_token(store):
    # Refresh Zoho access token using the refresh token
    url = 'https://accounts.zoho.com/oauth/v2/token'
    payload = {
        'refresh_token': store.zoho_refresh_token,
        'client_id': store.zoho_client_id,
        'client_secret': store.zoho_client_secret,
        'grant_type': 'refresh_token'
    }
    response = requests.post(url, data=payload)
    response_data = response.json()
    return response_data['access_token']

def create_zoho_customer(store, customer_data):
    access_token = get_zoho_access_token(store)
    url = "https://www.zohoapis.com/crm/v2/Contacts"
    headers = {
        'Authorization': f'Zoho-oauthtoken {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=customer_data)
    return response.json()

def create_zoho_order(store, order_data):
    access_token = get_zoho_access_token(store)
    url = "https://www.zohoapis.com/crm/v2/SalesOrders"
    headers = {
        'Authorization': f'Zoho-oauthtoken {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=order_data)
    return response.json()

def create_zoho_inventory(store, inventory_data):
    access_token = get_zoho_access_token(store)
    url = "https://www.zohoapis.com/crm/v2/Products"
    headers = {
        'Authorization': f'Zoho-oauthtoken {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=inventory_data)
    return response.json()