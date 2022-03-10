from django.db import models

class Ticket1(models.Model):
    ticket_title = models.CharField(max_length=100)
    ticket_description = models.TextField()

    class Meta():
        db_table = 'ticket1' 
