
from django.contrib import admin
from django.urls import include, path
from .views import CreateTicket1

urlpatterns = [
    path('add/', CreateTicket1.as_view()),
    # path('view/',),

]
