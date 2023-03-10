from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model

# Create your models here.


class Item(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    item_desc = models.TextField(max_length=200)
    price = models.FloatField()
    safety_stock = models.IntegerField()
    note = models.TextField(max_length=200, null=True)
    in_use = models.BooleanField(default=True)

    def __str__(self):
        return self.item_desc


class ItemOnStock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    on_stock = models.FloatField()


class HardwareType(models.Model):
    hardware_id = models.BigAutoField(primary_key=True)
    type_desc = models.TextField(max_length=200)
    in_use = models.BooleanField(default=True)

    class Meta:
        ordering = ['-in_use']

    def __str__(self):
        return self.type_desc


class ItemForHardware(models.Model):
    # HardwareID = models.TextChoices('HardwareID', '1 2 3')
    # ItemID = models.TextChoices('ItemID', '1 2 3')
    # hardware_id = models.CharField(blank=False, choices=HardwareID.choices, max_length=20)
    # item_id = models.CharField(blank=False, choices=ItemID.choices, max_length=20)
    hardware_type = models.ForeignKey(HardwareType, on_delete=models.PROTECT, null=False)
    item = models.ForeignKey(Item, on_delete=models.PROTECT, null=False)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created']


class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    customer_name = models.TextField(max_length=200)
    in_use = models.BooleanField(default=True)

    def __str__(self):
        return self.customer_name


class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    order_num = models.IntegerField()
    order_desc = models.TextField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False)

    class Meta:
        ordering = ['-order_num']

    def __str__(self):
        return self.order_desc


class Hardware(models.Model):
    id = models.BigAutoField(primary_key=True)
    mac = models.TextField(max_length=200, null=True)
    type = models.ForeignKey(HardwareType, on_delete=models.PROTECT, null=False)
    location = models.TextField(max_length=200)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=False)
    in_use = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.mac


class ItemTran(models.Model):
    # TranType = models.TextChoices('TranID', 'in out')
    # tran_type = models.CharField(blank=False, choices=TranType.choices, max_length=20)
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True)
    tran_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-tran_created']