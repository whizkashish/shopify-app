from django.db import models

# Create your models here.

class Subscriber(models.Model):
    first_name = models.CharField(max_length=50,default=None)
    last_name = models.CharField(max_length=50,default=None)
    email = models.EmailField(blank=False,unique=True)

    def __str__(self):
        return self.first_name

        