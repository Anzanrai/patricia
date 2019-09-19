from datetime import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import PostEventSerializer, EventSerializer, PostNewsSerializer, UpdateNewsSerializer, NewsSerializer
from .models import Event, New


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = PostEventSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsSetPagination

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostEventSerializer
        return EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(data={'body': ['New event has been successfully added.']}, status=status.HTTP_201_CREATED,
                            headers=headers)
        else:
            errors = serializer.errors
            if 'title' in errors:
                errors.update({'title': ['Please provide event title.']})
            if 'venue' in errors:
                errors.update({'venue': ['Location of the event is not provided.']})
            if 'organizer' in errors:
                errors.update({'organizer': ['Organizer of the event not provided.']})
            if 'description' in errors:
                errors.update({'description': ['Please provide short description of the event.']})
            return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = New.objects.filter(published_date__gte=datetime.today().date())
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsSetPagination
