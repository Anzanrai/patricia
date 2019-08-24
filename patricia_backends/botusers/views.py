from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView


class LoginView(TemplateView):
    template_name = 'user_login.html'


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginValidate(FormView):
    pass