from django.contrib import admin
from .models import (
    Organization,
    Project,
)

admin.site.register([Organization, Project])
