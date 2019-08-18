from django.contrib import admin

# Register your models here.
from .models import Event

admin.site.register(Event)
# class EventAdmin(admin.AdminSite):
