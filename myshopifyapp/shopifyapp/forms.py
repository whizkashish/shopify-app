from django import forms
from .models import ShopifyStore

class ZohoDetailsForm(forms.ModelForm):
    class Meta:
        model = ShopifyStore
        fields = ['zoho_client_id', 'zoho_client_secret', 'zoho_refresh_token']
