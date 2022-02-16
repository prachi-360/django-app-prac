from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addProduct(request):
    print("Add Product Called...")
    return HttpResponse("Add Product Called...")