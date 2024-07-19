# myshopifyapp/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shopify/', include('shopifyapp.urls')),
    path('', include('pages.urls')),
]