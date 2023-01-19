from django import forms
from logging import getLogger

from django.core.exceptions import ValidationError
from django.forms import Form, Textarea, ModelForm
from sklad.models import Item

LOGGER = getLogger()


class UploadForm(ModelForm):
    item_desc = forms.TextInput()
    price = forms.FloatField()
    safety_stock = forms.IntegerField()
    note = forms.TextInput()
    in_use = forms.BooleanField()
    class Meta:
        model = Item
        fields = ['item_desc', 'price', 'safety_stock', 'note', 'in_use']