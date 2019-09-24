from django.urls import path, include
from rest_framework import routers

from .views import EventViewSet, NewsViewSet, HeritageViewSet

router = routers.DefaultRouter()
router.register(r'event', EventViewSet)
router.register(r'news', NewsViewSet)
router.register(r'heritage', HeritageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
