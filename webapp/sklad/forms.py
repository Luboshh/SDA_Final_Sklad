from django import forms
from logging import getLogger

from django.core.exceptions import ValidationError
from django.forms import Form, Textarea, ModelForm
from sklad.models import Item, ItemTran, Order, Hardware, HardwareType

LOGGER = getLogger()


class AddItemForm(ModelForm):
    item_desc = forms.CharField(label='Item desc', max_length=50, widget=forms.TextInput)
    price = forms.FloatField()
    safety_stock = forms.IntegerField()
    note = forms.CharField(label='Item desc', max_length=50, widget=forms.TextInput, required=False)
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

    class Meta:
        model = Hardware
        fields = ['mac', 'type', 'location', 'order', 'in_use']