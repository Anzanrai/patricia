from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView

from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from .forms import LoginForm
from .tokens import account_activation_token
from .models import BotUser
from .serializers import RegisterSerializer, BotUserSerializer


@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    return Response("Email account is activated")


class LoginView(APIView):
    # template_name = 'user_login.html'
    form_class = LoginForm

    def form_valid(self, form):
        pass


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if not(username or email) or not password:
        return Response({'error': 'Please provide credentials to login'}, status=HTTP_400_BAD_REQUEST)
    else:
        try:
            user = BotUser.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user': BotUserSerializer(user).data}, status=HTTP_200_OK)
            else:
                return Response({'error': 'Incorrect login credentials provided.'}, status=HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({'error': 'User does not exist with provided credentials.'}, status=HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def logout(request):
    return Response({'token': '', 'user': {}}, status=HTTP_200_OK)


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginValidate(FormView):
    pass


class RegisterViewSet(viewsets.ModelViewSet):
    # form_class = RegisterForm
    queryset = BotUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(data={'body': ['You have successfully register']}, status=status.HTTP_201_CREATED,
                            headers=headers)
        else:
            errors = serializer.errors
            if 'username' in errors:
                if request.data.get('username'):
                    errors.update({'username': ['Username already taken.']})
                else:
                    errors.update({'username': ['Username not provided.']})
            if 'email' in errors:
                if request.data.get('email'):
                    errors.update({'email': ['This email is already registered.']})
                else:
                    errors.update({'email': ['Email not provided.']})
            if 'password' in errors and not request.data.get('password'):
                errors.update({'password': ['Password not provided.']})
            return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)


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