from dataclasses import field
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Ticket1

class CreateTicket1(CreateView):
    model = Ticket1
    fields = ['ticket_title','ticket_description']
    template_name = 'ticket1/create_ticket.html'
    success_url = '/ticket1/view/'
