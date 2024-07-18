from django.core.management.base import BaseCommand
from shopifyapp.models import ShopifyStore
from shopifyapp.utils import get_shopify_customers, get_shopify_orders, get_shopify_inventory
from shopifyapp.zoho_utils import create_zoho_customer, create_zoho_order, create_zoho_inventory

class Command(BaseCommand):
    help = 'Sync data between Shopify and Zoho'

    def handle(self, *args, **kwargs):
        stores = ShopifyStore.objects.all()
        for store in stores:
            shop = store.shop_name
            access_token = store.access_token

            customers = get_shopify_customers(shop, access_token)
            for customer in customers['customers']:
                create_zoho_customer(store, customer)

            orders = get_shopify_orders(shop, access_token)
            for order in orders['orders']:
                create_zoho_order(store, order)

            inventory = get_shopify_inventory(shop, access_token)
            for item in inventory['inventory_levels']:
                create_zoho_inventory(store, item)
