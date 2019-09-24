import uuid

from datetime import datetime
from django.db import models


# Create your models here.


class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('Free Ticket', 'Free Ticket'),
        ('Ticket With Fee', 'Ticket With Fee'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(choices=EVENT_TYPE_CHOICES, default='Free Ticket', max_length=100)
    event_cost = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
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
    detail = models.CharField(blank=False, null=False, max_length=3000)


class Heritage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=10000, blank=False, null=False)