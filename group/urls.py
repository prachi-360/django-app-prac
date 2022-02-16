from django.urls import include, path
from group import views
urlpatterns = [
     path('add/',views.group),
     path('contactUs/',views.contactUs),
     path('aboutUs/',views.aboutUs),
     path('',views.index),
     
]