from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import RegisterViewSet, UserViewSet, activate, login

router = routers.DefaultRouter()
router.register(r'registers', RegisterViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    path(r'login/', login),
]
