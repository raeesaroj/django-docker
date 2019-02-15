from django.contrib import admin
from .models import (
    Inventory,
    Item,
    Category,
)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['item', 'resource', 'quantity']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["unit"]
        else:
            return []


admin.site.register(Category)
