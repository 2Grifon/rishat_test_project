from django.contrib.admin import register, ModelAdmin

from apps.shop.models.item import Item


@register(Item)
class ItemAdmin(ModelAdmin):
    list_display = ["id", "name", "price", "currency"]
    search_fields = ["name"]
