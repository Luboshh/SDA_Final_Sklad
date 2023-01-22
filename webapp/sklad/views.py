from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, DeleteView
from logging import getLogger

from sklad.forms import AddItemForm, ToStockForm, TranUpdateForm
from sklad.models import Item, Hardware, ItemTran

LOGGER = getLogger()


def home(request):
    template = "sklad/home.html"
    return render(request, template)


def add_item(request):
    if request.POST:
        form = AddItemForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    template = "sklad/additem.html"
    context = {'form': AddItemForm}
    return render(request, template, context)


def to_stock(request):
    title = 'list of transaction'
    queryset = ItemTran.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        'form': ToStockForm
    }

    if request.POST:
        form = ToStockForm(request.POST)
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.quantity *= 1
            instance.save()
            return redirect(to_stock)

    return render(request, "sklad/to_stock.html", context)


def update_tran(request, pk):
    item = ItemTran.objects.get(id=pk)
    form = TranUpdateForm(instance=item)
    if request.method == 'POST':
        form = TranUpdateForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(to_stock)

    context = {
        'form': form,
        'item': item,
    }
    return render(request, "sklad/update_tran.html", context)
