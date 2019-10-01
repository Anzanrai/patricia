from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError
# from ../../models import BotUser
from events.models import Event, Heritage, New

from botusers.models import BotUser

from .data import HERITAGE_DATA, EVENT_DATA, USER_DATA, NEWS_DATA


class Command(BaseCommand):
    help = 'Sets up database with initial data.'

    def handle(self, *args, **options):
        for user in USER_DATA:
            new_user = BotUser(**user)
            new_user.save()

        for event in EVENT_DATA:
            new_event = Event(**event)
            new_event.save()

        for heritage in HERITAGE_DATA:
            new_heritage = Heritage(**heritage)
            new_heritage.save()

        for news in NEWS_DATA:
            new_news = New(**news)
            new_news.save()