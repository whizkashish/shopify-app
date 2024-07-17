from django.contrib import admin
from .models import Subscriber
# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']


admin.site.register(Subscriber,SubscriberAdmin)