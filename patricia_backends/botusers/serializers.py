from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import request, HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers

from .tokens import account_activation_token
from .models import BotUser


class RegisterSerializer(serializers.ModelSerializer):
    # queryset = BotUser.objects.filter(is_deleted=False)

    class Meta:
        model = BotUser
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email']

    # def send_registration_email(self):

    def create(self, validated_data):
        user = BotUser(**validated_data)
        # user.is_active = False
        # user.save()
        # current_site = get_current_site(request)
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': 'localhost:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        mail_subject = 'Patricia Account Activation.'
        to_email = validated_data.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        user.save()
        return HttpResponse('Please confirm your email address to complete the registration')


class BotUserSerializer(serializers.ModelSerializer):
    # queryset = BotUser.objects.filter(is_deleted= False)
    class Meta:
        model = BotUser
        fields = ['__all__']