"""
BIPAD URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import static
from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

admin.site.site_header = 'BIPAD administration'

router = routers.DefaultRouter()

API_VERSION = 'v1'


def get_api_path(path):
    return r'^api/(?P<version>({}))/{}'.format(API_VERSION, path)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(get_api_path(r'token/$'), TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(get_api_path(r'token/refresh/$'), TokenRefreshView.as_view(), name='token_refresh'),
    re_path(get_api_path(r'token/verify/$'), TokenVerifyView.as_view(), name='token_verify'),
    re_path(get_api_path(''), include(router.urls)),
] + static.static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
