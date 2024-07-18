from django.urls import path
from . import views

urlpatterns = [
    path('install/', views.install_app, name='install_app'),
    path('callback/', views.callback, name='callback'),
    path('enter-zoho-details/<str:shop_name>/', views.enter_zoho_details, name='enter_zoho_details'),
    path('webhook/', views.webhook, name='webhook'),
]