# Generated by Django 5.0.7 on 2024-07-18 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopifyStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('access_token', models.CharField(max_length=255)),
                ('zoho_client_id', models.CharField(blank=True, max_length=255, null=True)),
                ('zoho_client_secret', models.CharField(blank=True, max_length=255, null=True)),
                ('zoho_refresh_token', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('store', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shopifyapp.shopifystore')),
            ],
        ),
    ]
