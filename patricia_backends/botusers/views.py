from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, FormView

# from botusers.forms import RegisterForm
from .forms import RegisterForm


class LoginView(TemplateView):
    template_name = 'user_login.html'


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginValidate(FormView):
    pass


class RegisterView(View):
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponse({'text': 'Registration Successful'})
        return HttpResponse({'error': 'Registration Failure'})

