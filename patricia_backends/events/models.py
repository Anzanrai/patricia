import uuid

from datetime import datetime
from django.db import models


# Create your models here.


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=False, null=False, max_length=500)
    venue = models.CharField(blank=False, null=False, max_length=300)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.CharField(max_length=800)
    organizer = models.CharField(max_length=300, blank=False, null=False)


class New(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=False, null=False, max_length=500)
    writer = models.CharField(blank=False, null=False, max_length=300)
    published_date = models.DateField(blank=False, null=False, default=datetime.today().date())
    updated_date = models.DateField(blank=True, null=True)
    detail = models.CharField(blank=False, null=False, max_length=1000)