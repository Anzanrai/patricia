from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    path("login/form/", views.LoginView.as_view(), name='login_form')
]