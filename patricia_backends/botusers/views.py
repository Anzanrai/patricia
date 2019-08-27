from django.http import HttpResponse

# Create your views here.
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import TemplateView, FormView

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tokens import account_activation_token
from .models import BotUser
from .serializers import RegisterSerializer, BotUserSerializer


@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    return Response("Email account is activated")


class LoginView(TemplateView):
    template_name = 'user_login.html'


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginValidate(FormView):
    pass


class RegisterViewSet(viewsets.ModelViewSet):
    # form_class = RegisterForm
    queryset = BotUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponse({'text': 'Registration Successful'})
        return HttpResponse({'error': 'Registration Failure'})


class UserViewSet(viewsets.ViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = BotUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, BotUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')