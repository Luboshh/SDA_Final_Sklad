from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sklad.models import Item, Item_on_stock, Item_for_hardware, Hardware_type

class ItemAdmin(admin.ModelAdmin):
    # ListView
    ordering = ['item_id']
    list_display = ['item_id', 'item_desc', 'price', 'safety_stock']
    list_display_links = ['item_id', 'item_desc']
    list_per_page = 20
    search_fields = ['item_desc']

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Item_on_stock)
admin.site.register(Item_for_hardware)
admin.site.register(Hardware_type)
