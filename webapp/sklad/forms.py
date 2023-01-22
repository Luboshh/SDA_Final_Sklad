from django import forms
from logging import getLogger

from django.core.exceptions import ValidationError
from django.forms import Form, Textarea, ModelForm
from sklad.models import Item, ItemTran

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

    def clean_item_desc(self):
        item_desc = self.cleaned_data.get('item_desc')
        if not item_desc:
            raise forms.ValidationError('This field is required')
        return item_desc


class QuantityForm(ModelForm):
    quantity = forms.FloatField()

    class Meta:
        model = ItemTran
        fields = ['quantity']


class ItemSearchForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_desc']
