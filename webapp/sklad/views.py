from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, DeleteView
from logging import getLogger

from sklad.forms import AddItemForm, ToStockForm, TranUpdateForm, UnloadHardwareForm, HardwareUpdateForm
from sklad.models import Item, Hardware, ItemTran, ItemForHardware

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


def unload_hardware(request):
    queryset = Hardware.objects.all()
    if request.POST:
        form = UnloadHardwareForm(request.POST)
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            hardware_type = instance.type
            hardware_order = instance.order
            for item_hw in hardware_type.itemforhardware_set.all():
                print(item_hw.item.item_desc)
                item = item_hw.item
                quantity = item_hw.quantity * -1
                tran = ItemTran(item=item_hw.item, quantity=quantity, order=hardware_order)
                tran.save()
                form.save()
            return redirect(unload_hardware)

    context = {
        'form': UnloadHardwareForm,
        'queryset': queryset,
    }

    return render(request, "sklad/unload.html", context)


def update_hardware(request, pk):
    hardware = Hardware.objects.get(id=pk)
    form = HardwareUpdateForm(instance=hardware)
    if request.method == 'POST':
        form = TranUpdateForm(request.POST, instance=hardware)
        if form.is_valid():
            form.save()
        return redirect(unload_hardware)

    context = {
        'form': form,
        'hardware': hardware,
    }
    return render(request, "sklad/update_hardware.html", context)