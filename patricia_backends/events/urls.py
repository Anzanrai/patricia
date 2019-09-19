from django.urls import path, include
from rest_framework import routers

from .views import EventViewSet, NewsViewSet

router = routers.DefaultRouter()
router.register(r'event', EventViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
