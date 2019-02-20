from django.contrib import admin
from .models import Earthquake


# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id", "event_on", "address", "magnitude", "description", "created_on"
                    , "modified_on"]

    class Meta:
        model = Earthquake


admin.site.register(Earthquake, PostModelAdmin)
