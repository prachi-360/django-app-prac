from dataclasses import fields
from django.shortcuts import render
from .models import Cart,Payment,Season
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


class CreatePayment(CreateView):
    model = Payment
    fields = ['amount','payment_status']
    template_name = 'cart/create_payment.html'
    success_url = '/cart/create_cart'


class CreateCart(CreateView):
    model = Cart
    fields = '__all__'
    template_name = 'cart/create_cart.html'
    success_url = '/cart/create_cart'

class CreateSeason(CreateView):
    model = Season
    fields = '__all__'
    template_name = 'cart/create_season.html'
    success_url = '/cart/create_season'


