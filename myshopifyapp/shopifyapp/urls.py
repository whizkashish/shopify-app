# shopifyapp/urls.py
from django.urls import path
from .views import install, finalize, add_contact_to_zoho

urlpatterns = [
    path('install/', install, name='install'),
    path('finalize/', finalize, name='finalize'),
    path('add-contact/', add_contact_to_zoho, name='add_contact_to_zoho'),
]
