from django.contrib import admin
from .models import (
    Loss,
    People,
    Family,
    Infrastructure,
    InfrastructureType,
    LivestockType,
)


class PeopleInline(admin.TabularInline):
    model = People
    extra = 1


class FamilyInline(admin.TabularInline):
    model = Family
    extra = 1


class InfrastructureInline(admin.TabularInline):
    model = Infrastructure
    extra = 1


@admin.register(Loss)
class LossAdmin(admin.ModelAdmin):
    inlines = (PeopleInline, FamilyInline, InfrastructureInline)


admin.site.register([InfrastructureType, LivestockType])
