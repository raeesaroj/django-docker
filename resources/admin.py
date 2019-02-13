from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import (
    Resource,
    Education,
    Health,
)


@admin.register(Resource)
class ResourceAdmin(PolymorphicParentModelAdmin):
    base_model = Resource
    child_models = (Education, Health)


@admin.register(Education)
class EducationAdmin(ResourceAdmin):
    base_model = Education  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site


@admin.register(Health)
class HealthAdmin(ResourceAdmin):
    base_model = Health
    show_in_index = True

# admin.site.register(Education, ResourceAdmin)
