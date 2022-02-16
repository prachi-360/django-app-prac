from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def group(request):
    return HttpResponse("Group Called...")

def index(request):
    context = {
        'name':'FLIPCART',
    }
    return render(request,'group/index.html',context)

def contactUs(request):
    context = {
        'contact_name':['Ram','Bharat','Laxman','Shatrudhnya']
    }
    return render(request,'group/contactUs.html',context)

def aboutUs(request):
    context = {
        'isActive':True,
        'age':22 
    }
    return render(request,'group/aboutUs.html',context)