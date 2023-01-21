from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, DeleteView

from webapp.sklad.models import Item

# Create your views here.
# Create your views here.
def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Ahoj {s}!!!')