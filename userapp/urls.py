from os import name
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserLoginView
from . import views

app_name = 'product_urls'

urlpatterns = [
    
    path("user-registration/",BaseRegisterView.as_view(),name="user-registration"),
    path('user-login/',UserLoginView.as_view(),name='user-login'),
    path("index/",views.index),
]