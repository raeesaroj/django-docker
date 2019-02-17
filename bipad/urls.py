"""
BIPAD URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import static
from django.urls import path

admin.site.site_header = 'BIPAD administration'

urlpatterns = [
    path('admin/', admin.site.urls),
] + static.static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
