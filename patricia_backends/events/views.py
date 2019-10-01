from datetime import datetime

from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializers import PostEventSerializer, EventSerializer, PostNewsSerializer, UpdateNewsSerializer, NewsSerializer, \
    PostHeritageSerializer, UpdateHeritageSerializer, HeritageSerializer
from .models import Event, New, Heritage


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

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostNewsSerializer
        if self.request.method == 'PUT':
            return UpdateNewsSerializer
        return NewsSerializer

    def create(self, request, *args, **kwargs):
        data = {}
        for key, value in request.data.items():
            data[key] = value
        data['writer'] = request.user.username
        data['published_date'] = datetime.today().date()
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(data={'body': ['News has been successfully added.']}, status=status.HTTP_201_CREATED,
                            headers=headers)
        else:
            errors = serializer.errors
            if 'title' in errors:
                errors.update({'title': ['Please provide news title.']})
            if 'detail' in errors:
                if not request.data['detail']:
                    errors.update({'detail': ['News detail is not provided.']})
            return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)


class HeritageViewSet(viewsets.ModelViewSet):
    # queryset = Heritage.objects.all()
    permission_classes = (AllowAny, )

    def get_queryset(self):
        heritage_name = self.request.query_params.get('name', '')
        if heritage_name:
            return Heritage.objects.filter(name__icontains=heritage_name)
        else:
            return Heritage.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostHeritageSerializer
        if self.request.method == 'PUT':
            return UpdateHeritageSerializer
        return HeritageSerializer


class HeritageSuggestionViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )

    def get_queryset(self):
        heritage_name = self.request.query_params.get('heritage_name', '')
        if heritage_name:
            return Heritage.objects.annotate(similarity=TrigramSimilarity('name', heritage_name), )\
                .order_by('-similarity')
        else:
            return Heritage.objects.all()

    def get_serializer_class(self):
        return HeritageSerializer