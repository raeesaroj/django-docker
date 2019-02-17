from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin
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
    base_model = Education
    show_in_index = True


@admin.register(Health)
class HealthAdmin(ResourceAdmin):
    base_model = Health
    show_in_index = True
