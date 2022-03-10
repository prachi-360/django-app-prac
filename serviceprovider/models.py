from platform import python_branch
from django.db import models

class ServiceProvider(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    phone = models.IntegerField()
    website = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta():
        db_table = 'service_provider'