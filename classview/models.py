from django.db import models

class Hr(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField(max_length=100)
    contact = models.IntegerField()
    class Meta():
        db_table = 'hr'
