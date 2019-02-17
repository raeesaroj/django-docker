from django.contrib import admin
from .models import (
    Province,
    District,
    Municipality,
    Ward,
)

admin.site.register([Province, District, Municipality, Ward])
