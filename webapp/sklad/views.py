from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.template.defaulttags import register
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, DeleteView
from logging import getLogger

from sklad.forms import AddItemForm, ToStockForm, TranUpdateForm
from sklad.forms import UnloadHardwareForm, HardwareUpdateForm, HardwareTypesForm, UpdateHardwareTypesForm
from sklad.forms import ItemForHardwareForm, OrdersForm, UpdateOrderForm, UpdateCustomerForm, CustomerForm, ItemUpdateForm
from sklad.models import Item, Hardware, ItemTran, ItemForHardware, ItemOnStock, HardwareType, Order, Customer


LOGGER = getLogger()


def home(request):
    template = "sklad/home.html"
    return render(request, template)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def add_item(request):
    queryset = Item.objects.all()
    template = "sklad/add_item.html"
    form = AddItemForm

    result = ItemTran.objects.values('item').annotate(sum=Sum('quantity'))
    print(result)
    quantity = dict()
    for r in result:
        quantity[r["item"]] = r["sum"]

    if request.POST:
        form = AddItemForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect(add_item)

    context = {'form': form,
               "queryset": queryset,
               "quantity": quantity,
               # "summary": summary
               }
    return render(request, template, context)


def update_item(request, pk):
    item = Item.objects.get(item_id=pk)
    form = ItemUpdateForm(instance=item)
    if request.method == 'POST':
        form = ItemUpdateForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(add_item)

    context = {
        'form': form,
        'item': item,
    }
    return render(request, "sklad/update_item.html", context)


class SignUpView(CreateView):
    template_name = 'sklad/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('signup')

def form_valid(self, form):
    result = super().form_valid(form)
    cleaned_data = form.cleaned_data
    username = cleaned_data['username']
    password = cleaned_data['password1']
    new_user = authenticate(username=username, password=password)
    if new_user is not None:
        login(self.request, new_user)
        # LOGGER.warning(new_user)
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
        form = HardwareUpdateForm(request.POST, instance=hardware)
        if form.is_valid():
            print(request.POST)
            form.save()
        return redirect(unload_hardware)

    context = {
        'form': form,
        'hardware': hardware,
    }
    return render(request, "sklad/update_hardware.html", context)


def hardware_types(request):
    queryset = HardwareType.objects.all()
    context = {
        "queryset": queryset,
        'form': HardwareTypesForm
    }

    if request.POST:
        form = HardwareTypesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(hardware_types)

    return render(request, "sklad/hardware_types.html", context)


def update_hardware_type(request, pk):
    hardware = HardwareType.objects.get(hardware_id=pk)
    form = UpdateHardwareTypesForm(instance=hardware)
    if request.method == 'POST':
        form = UpdateHardwareTypesForm(request.POST, instance=hardware)
        if form.is_valid():
            form.save()
        return redirect(hardware_types)

    context = {
        'form': form,
        'hardware': hardware,
    }
    return render(request, "sklad/update_hardwaretype.html", context)


def item_for_hardware(request, pk):
    hardware = HardwareType.objects.get(hardware_id=pk)
    queryset = ItemForHardware.objects.filter(hardware_type=hardware.hardware_id)
    if request.POST:
        form = ItemForHardwareForm(request.POST)
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            item = instance.item
            quantity = instance.quantity
            tran = ItemForHardware(hardware_type=hardware, item=item, quantity=quantity)
            tran.save()

    context = {
        "queryset": queryset,
        'form': ItemForHardwareForm,
        'hardware': hardware,
    }

    return render(request, "sklad/items_for_hardware.html", context)


def orders(request):
    queryset = Order.objects.all()
    context = {
        "queryset": queryset,
        'form': OrdersForm
    }

    if request.POST:
        form = OrdersForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect(orders)

    return render(request, "sklad/orders.html", context)


def update_order(request, pk):
    order = Order.objects.get(order_id=pk)
    form = UpdateOrderForm(instance=order)
    if request.method == 'POST':
        form = UpdateOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect(orders)

    context = {
        'form': form,
        'order': order,
    }
    return render(request, "sklad/update_order.html", context)


def customers(request):
    queryset = Customer.objects.all()
    context = {
        "queryset": queryset,
        'form': CustomerForm
    }

    if request.POST:
        form = CustomerForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect(customers)

    return render(request, "sklad/customers.html", context)


def update_customer(request, pk):
    customer = Customer.objects.get(customer_id=pk)
    form = UpdateCustomerForm(instance=customer)
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect(customers)

    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, "sklad/update_customer.html", context)