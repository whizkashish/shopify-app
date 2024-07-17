# shopifyapp/views.py
import shopify
from django.shortcuts import redirect
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Subscriber

def add_contact_to_zoho(request):
    contact_data = {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john.doe@example.com',
             }
    subscriber = Subscriber(
        first_name = contact_data['first_name'],
        last_name = contact_data['last_name'],
        email = contact_data['email']
    )
    return JsonResponse({'status':'success'})

@csrf_exempt
def install(request):
    shop = request.GET.get('shop')
    shopify.Session.setup(api_key=settings.SHOPIFY_API_KEY, secret=settings.SHOPIFY_API_SECRET)
    session = shopify.Session(shop)
    permission_url = session.create_permission_url(['read_products', 'write_products'])
    return redirect(permission_url)

@csrf_exempt
def finalize(request):
    shopify.Session.setup(api_key=settings.SHOPIFY_API_KEY, secret=settings.SHOPIFY_API_SECRET)
    session = shopify.Session(request.GET['shop'])
    token = session.request_token(request.GET)
    request.session['shopify_token'] = token
    return JsonResponse({'status': 'success'})
