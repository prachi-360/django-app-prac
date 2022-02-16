
from django.contrib import admin
from django.urls import include, path
from product import views

urlpatterns = [
    path('addProduct/', views.addProduct),
    
]