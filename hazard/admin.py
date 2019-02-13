from django.contrib import admin
from .models import (
    Hazard,
    HazardResources,
)

admin.site.register([Hazard, HazardResources])
