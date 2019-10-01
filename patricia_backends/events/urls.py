from django.urls import path, include
from rest_framework import routers

from .views import EventViewSet, NewsViewSet, HeritageViewSet, HeritageSuggestionViewSet

router = routers.DefaultRouter()
router.register(r'event', EventViewSet)
router.register(r'news', NewsViewSet)
router.register(r'heritage', HeritageViewSet, basename='heritage')
router.register(r'suggestive_heritage', HeritageSuggestionViewSet, basename='suggestive_heritage')

urlpatterns = [
    path('', include(router.urls)),
]
