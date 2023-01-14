from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model

# Create your models here.

class Item(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    item_desc = models.TextField(max_length=200)
    price = models.IntegerField()
    safety_stock = models.IntegerField()
    note = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.item_desc


class Item_on_stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    on_stock = models.IntegerField()

    def __str__(self):
        return self.item


class Hardware_type(models.Model):
    hardware_id = models.BigAutoField(primary_key=True)
    type_desc = models.TextField(max_length=200)

    def __str__(self):
        return self.type_desc

class Item_for_hardware(models.Model):
    # HardwareID = models.TextChoices('HardwareID', '1 2 3')
    # ItemID = models.TextChoices('ItemID', '1 2 3')
    # hardware_id = models.CharField(blank=False, choices=HardwareID.choices, max_length=20)
    # item_id = models.CharField(blank=False, choices=ItemID.choices, max_length=20)
    hardware_id = models.ForeignKey(Hardware_type, on_delete=models.PROTECT, null=False)
    item_id = models.ForeignKey(Item, on_delete=models.PROTECT, null=False)
    quantity = models.IntegerField()


# class Hardware(models.Model):
#     mac = models.TextField(primary_key=True)
#     type_id = models.TextField(max_length=200)
#     price = models.IntegerField()
#     safety_stock = models.IntegerField()
#     note = models.TextField(max_length=200)
#
#     def __str__(self):
#         return self.