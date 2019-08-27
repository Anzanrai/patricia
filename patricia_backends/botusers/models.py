import uuid
from random import randint

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.


class BotUserManager(BaseUserManager):
    def get_queryset(self):
        return super(BotUserManager, self).get_queryset().filter(is_deleted=False)

    def create_bot_user(self, username=None, password=None, **kwargs):
        bot_user = self.model(**kwargs)
        bot_user.username = username
        bot_user.set_password(password)
        bot_user.clean()
        return bot_user


class BotUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(blank=False, null=False, max_length=30)
    middle_name = models.CharField(blank=True, null=True, max_length=30)
    last_name = models.CharField(blank=False, null=False, max_length=30)
    email = models.EmailField(blank=False, null=False, max_length=30, unique=True)
    username = models.CharField('username', blank=False, null=False, max_length=100, unique=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = BotUserManager()
    USERNAME_FIELD = 'username'

    def clean(self):
        if not self.username:
            self.username = self.generate_username()

    def generate_username(self):
        username = (self.first_name[0:3]+self.last_name[0:3]).lower()
        suffix = ''
        while not suffix or BotUser.objects.filter(username=username).exists():
            suffix = ''.join(['%s' % randint(0, 4) for num in range(0, 4)])
            username = username + str(suffix)
        return username

