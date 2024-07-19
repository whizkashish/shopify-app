import requests
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .forms import ZohoDetailsForm
from .models import ShopifyStore 
from django.views.decorators.csrf import csrf_exempt
from .zoho_utils import create_zoho_customer, create_zoho_order, create_zoho_inventory

SHOPIFY_API_KEY = '59f41b61ccf5dee1f6847f68fb69a739'
SHOPIFY_API_SECRET = '60074a1b5cd5eda34e43a92d52cf91ae'
SHOPIFY_REDIRECT_URI = 'https://shopify-app-sii3.onrender.com/shopify/callback'
SHOPIFY_SCOPE = 'read_orders,read_products,write_orders,write_products,read_customers, write_customers, read_inventory'

def install_app(request):
    shop = request.GET.get('shop')
    redirect_uri = SHOPIFY_REDIRECT_URI
    install_url = f"https://{shop}/admin/oauth/authorize?client_id={SHOPIFY_API_KEY}&scope={SHOPIFY_SCOPE}&redirect_uri={redirect_uri}"
    return HttpResponseRedirect(install_url)

def callback(request):
    shop = request.GET.get('shop')
    code = request.GET.get('code')

    access_token_url = f"https://{shop}/admin/oauth/access_token"
    payload = {
        'client_id': SHOPIFY_API_KEY,
        'client_secret': SHOPIFY_API_SECRET,
        'code': code
    }
    response = requests.post(access_token_url, data=payload)
    response_data = response.json()
    access_token = response_data['access_token']

    shopify_store, created = ShopifyStore.objects.get_or_create(shop_name=shop)
    shopify_store.access_token = access_token
    shopify_store.save()

    return HttpResponseRedirect(f'/shopify/enter-zoho-details/{shop}')

def enter_zoho_details(request, shop_name):
    store = ShopifyStore.objects.get(shop_name=shop_name)

    if request.method == 'POST':
        form = ZohoDetailsForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the dashboard or any other page
    else:
        form = ZohoDetailsForm(instance=store)

    return render(request, 'shopifyapp/zoho-details.html', {'form': form})

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        data = request.json()
        if 'customer' in data:
            create_zoho_customer(data['customer'])
        elif 'order' in data:
            create_zoho_order(data['order'])
        elif 'inventory_item' in data:
            create_zoho_inventory(data['inventory_item'])
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})