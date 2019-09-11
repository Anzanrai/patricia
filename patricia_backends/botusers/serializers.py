from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db import transaction
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
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        with transaction.atomic():
            user = BotUser(**validated_data)
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
            user.set_password(validated_data.get('password'))
            user.save()
            return HttpResponse('Please confirm your email address to complete the registration')


class BotUserSerializer(serializers.ModelSerializer):
    # queryset = BotUser.objects.filter(is_deleted= False)
    class Meta:
        model = BotUser
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'email', 'username', 'user_type']
