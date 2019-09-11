import uuid
from random import randint

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db import models

# Create your models here.
from django.db.models import Q


class BotUserManager(UserManager):
    def get_queryset(self):
        return super(BotUserManager, self).get_queryset().filter(is_deleted=False)

    def create_bot_user(self, username=None, password=None, **kwargs):
        bot_user = self.model(**kwargs)
        bot_user.username = username
        bot_user.set_password(password)
        bot_user.clean()
        return bot_user


class BotUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=100, default='User')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(blank=False, null=False, max_length=30)
    middle_name = models.CharField(blank=True, null=True, max_length=30)
    last_name = models.CharField(blank=False, null=False, max_length=30)
    email = models.EmailField(blank=False, null=False, max_length=30, unique=True)
    username = models.CharField('username', blank=False, null=False, max_length=100, unique=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = BotUserManager()
    USERNAME_FIELD = 'username' or 'email'

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


MyUser = get_user_model()


class UsernameOrEmailBackend(object):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
           # Try to fetch the user by searching the username or email field
            user = MyUser.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            MyUser().set_password(password)