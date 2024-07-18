import requests

def get_shopify_customers(shop, access_token):
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }
    url = f"https://{shop}/admin/api/2021-04/customers.json"
    response = requests.get(url, headers=headers)
    return response.json()

def get_shopify_orders(shop, access_token):
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }
    url = f"https://{shop}/admin/api/2021-04/orders.json"
    response = requests.get(url, headers=headers)
    return response.json()

def get_shopify_inventory(shop, access_token):
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }
    url = f"https://{shop}/admin/api/2021-04/inventory_levels.json"
    response = requests.get(url, headers=headers)
    return response.json()
