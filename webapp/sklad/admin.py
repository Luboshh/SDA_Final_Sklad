from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sklad.models import Item, ItemOnStock, ItemTran, ItemForHardware, HardwareType, Hardware, Customer, Order


class ItemAdmin(admin.ModelAdmin):
    # ListView
    ordering = ['item_id']
    list_display = ['item_desc', 'price', 'safety_stock', 'note', 'in_use']
    list_per_page = 20
    search_fields = ['item_desc']


class ItemOnStockAdmin(admin.ModelAdmin):
    # ListView
    ordering = ['item']
    list_display = ['item', 'on_stock']
    list_per_page = 20
    search_fields = ['item']


class ItemTranAdmin(admin.ModelAdmin):
    # ListView
    ordering = ['tran_created']
    list_display = ['id', 'item', 'quantity', 'tran_created']
    list_per_page = 50
    search_fields = ['item']


class ItemForHardwareAdmin(admin.ModelAdmin):
    # ListView
    ordering = ['hardware_type']
    list_display = ['hardware_type', 'item', 'quantity']
    list_per_page = 20


class HardwareTypeAdmin(admin.ModelAdmin):
    # ListView
    ordering = ['hardware_id']
    list_display = ['hardware_id', 'type_desc', 'in_use']
    list_per_page = 20


class CustomerAdmin(admin.ModelAdmin):
    # ListView
    ordering = ['customer_id']
    list_display = ['customer_name', 'in_use']
    list_per_page = 20


class OrderAdmin(admin.ModelAdmin):
    # ListView
    ordering = ['order_id']
    list_display = ['order_num', 'order_desc', 'customer']
    list_per_page = 20


class HardwareAdmin(admin.ModelAdmin):
    # ListView
    ordering = ['id']
    list_display = ['id', 'mac', 'type', 'customer', 'location', 'order', 'in_use']
    list_per_page = 20

    class Meta:
        model = Order

    def customer(self, obj):
        return obj.order.customer


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemOnStock, ItemOnStockAdmin)
admin.site.register(ItemTran, ItemTranAdmin)
admin.site.register(ItemForHardware, ItemForHardwareAdmin)
admin.site.register(HardwareType, HardwareTypeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Hardware, HardwareAdmin)
