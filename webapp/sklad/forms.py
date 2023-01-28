from django import forms
from logging import getLogger

from django.core.exceptions import ValidationError
from django.forms import Form, Textarea, ModelForm
from sklad.models import Item, ItemTran, Order, Hardware, HardwareType, ItemForHardware, Customer

LOGGER = getLogger()


class AddItemForm(ModelForm):
    item_desc = forms.CharField(label='Item desc', max_length=50, widget=forms.TextInput)
    price = forms.FloatField()
    safety_stock = forms.IntegerField()
    note = forms.CharField(label='Note', max_length=50, widget=forms.TextInput, required=False)
    in_use = forms.BooleanField(widget=forms.CheckboxInput, initial=True)

    class Meta:
        model = Item
        fields = ['item_desc', 'price', 'safety_stock', 'note', 'in_use']

        def clean_item_desc(self):
            item_desc = self.cleaned_data.get('item_desc')
            if not item_desc:
                raise forms.ValidationError('This field is required')
            return item_desc


class ItemUpdateForm(ModelForm):
    item_desc = forms.CharField(label='Item desc', max_length=50, widget=forms.TextInput)
    price = forms.FloatField()
    safety_stock = forms.IntegerField()
    note = forms.CharField(label='Note', max_length=50, widget=forms.TextInput, required=False)
    in_use = forms.BooleanField(widget=forms.CheckboxInput, initial=True)

    class Meta:
        model = Item
        fields = ['item_desc', 'price', 'safety_stock', 'note', 'in_use']


class ToStockForm(ModelForm):
    item = forms.ModelChoiceField(Item.objects.all())
    quantity = forms.IntegerField()
    order = forms.ModelChoiceField(Order.objects.all(), required=False)

    class Meta:
        model = ItemTran
        fields = ['item', 'quantity', 'order']


class TranUpdateForm(ModelForm):

    class Meta:
        model = ItemTran
        fields = ['item', 'quantity', 'order']


class UnloadHardwareForm(ModelForm):
    type = forms.ModelChoiceField(HardwareType.objects.all(), label='Box type')
    mac = forms.CharField(label='Box mac', max_length=50, widget=forms.TextInput)
    order = forms.ModelChoiceField(Order.objects.all(), label='Custommer order')
    location = forms.CharField(label='Location', max_length=50, widget=forms.TextInput, required=False)

    class Meta:
        model = Hardware
        fields = ['mac', 'type', 'order', 'location']


class HardwareUpdateForm(ModelForm):
    mac = forms.CharField(label='Location', max_length=50, widget=forms.TextInput, required=False)
    in_use = forms.BooleanField(label='in_use', required=False)
    location = forms.CharField(label='Location', max_length=50, widget=forms.TextInput, required=False)
    in_use = forms.BooleanField(required=False, widget=forms.CheckboxInput)

    class Meta:
        model = Hardware
        fields = ['mac', 'type', 'location', 'order', 'in_use']


class HardwareTypesForm(ModelForm):
    type_desc = forms.CharField(label='Type description', max_length=50, widget=forms.TextInput, required=False)

    class Meta:
        model = HardwareType
        fields = ['type_desc']


class UpdateHardwareTypesForm(ModelForm):
    type_desc = forms.CharField(label='Type description', max_length=50, widget=forms.TextInput, required=False)
    in_use = forms.BooleanField(required=False, widget=forms.CheckboxInput)

    class Meta:
        model = HardwareType
        fields = ['type_desc', 'in_use']


class ItemForHardwareForm(ModelForm):
    item = forms.ModelChoiceField(Item.objects.all())
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = ItemForHardware
        fields = ['item', 'quantity']


class OrdersForm(ModelForm):
    order_num = forms.IntegerField(label='Number', required=True)
    order_desc = forms.CharField(label='Description', required=True)
    customer = forms.ModelChoiceField(Customer.objects.all(), label='Custommer')

    class Meta:
        model = Order
        fields = ['order_num', 'order_desc', 'customer']


class UpdateOrderForm(ModelForm):
    order_desc = forms.CharField(label='Description', required=True)
    customer = forms.ModelChoiceField(Customer.objects.all(), label='Custommer')

    class Meta:
        model = Order
        fields = ['order_desc', 'customer']


class CustomerForm(ModelForm):
    customer_name = forms.CharField(label='Customer', required=True)
    in_use = forms.BooleanField(required=False, widget=forms.CheckboxInput)

    class Meta:
        model = Customer
        fields = ['customer_name', 'in_use']


class UpdateCustomerForm(ModelForm):
    customer_name = forms.CharField(label='Customer', required=True)
    in_use = forms.BooleanField(required=False, widget=forms.CheckboxInput)

    class Meta:
        model = Customer
        fields = ['customer_name', 'in_use']