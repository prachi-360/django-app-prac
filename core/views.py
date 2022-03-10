from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView

class UserLogin(LoginView):
    template_name = 'core/login.html'

class UserLogout(LogoutView):
    pass
