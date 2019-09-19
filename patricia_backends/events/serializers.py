from datetime import datetime

from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Event, New


class PostEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'venue', 'start_date', 'start_time', 'end_date', 'end_time', 'organizer', 'description']

    def validate(self, attrs):
        data = self.context['request'].data
        event_start_date = datetime.strptime(data.get('start_date')+" "+data.get('start_time'), "%Y-%m-%d %H:%M")
        event_end_date = datetime.strptime(data.get('end_date')+" "+data.get('end_time'), "%Y-%m-%d %H:%M")
        if event_start_date < event_end_date:
            return super(PostEventSerializer, self).validate(attrs)
        else:
            raise ValidationError({'end_date': 'Event end date and time is before event start date and time.'})


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class PostNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        exclude = ['id']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class UpdateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['title', 'writer', 'updated_date', 'detail']
        read_only_fields = ['published_date']