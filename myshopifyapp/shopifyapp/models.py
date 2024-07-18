from django.db import models

# Create your models here.

# shopify_sync/models.py

from django.db import models

class ShopifyStore(models.Model):
    shop_name = models.CharField(max_length=255,unique=True)
    active = models.BooleanField(default=True)
    access_token = models.CharField(max_length=255)
    zoho_client_id = models.CharField(max_length=255, blank=True, null=True)
    zoho_client_secret = models.CharField(max_length=255, blank=True, null=True)
    zoho_refresh_token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shop_name



class Subscriber(models.Model):
    first_name = models.CharField(max_length=50,default=None)
    last_name = models.CharField(max_length=50,default=None)
    email = models.EmailField(blank=False)
    store = models.ForeignKey(ShopifyStore,blank=False, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.first_name
