from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, DeleteView
from logging import getLogger

from sklad.forms import AddItemForm, ItemSearchForm
from sklad.models import Item, Hardware, ItemTran

from sklad.models import ItemTran

from sklad.models import ItemOnStock

LOGGER = getLogger()


def home(request):
    template = "sklad/home.html"
    return render(request, template)


def add_item(request):
    search = ItemSearchForm(request.POST or None)
    queryset = Item.objects.all()
    template = "sklad/add_item.html"
    quantity = ItemTran.quantity

    if request.POST:
        form = AddItemForm(request.POST)  # TODO proc se zobrazuje 2x Item_desc namísto note
        print(request.POST)
        if form.is_valid():
            form.save()
        # if Item.safety_stocks > ItemTran.quantity:  # TODO zatim nefukcni
        #     print("Nutno naskladnit")
        return redirect(add_item)

    if request.method == 'POST':
        queryset = Item.objects.filter(item_desc__icontains=search['item_desc'].value(),
                                       )
    context = {'form': AddItemForm,
               "queryset": queryset,
               "quantity": quantity,
               "search": search,
               }
    return render(request, template, context)

# def safety_stock(request):
#     queryset = Item.safety_stock
#     template = "sklad/add_item.html"
#     context = {"queryset": queryset}
#     if safety_stock()
#     return render(request, template, context=context)
