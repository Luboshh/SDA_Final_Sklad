from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, DeleteView
from logging import getLogger

from sklad.forms import UploadForm
from sklad.models import Item, Hardware

LOGGER = getLogger()


def home(request):
    template = "sklad/home.html"
    return render(request, template)


def upload(request):
    if request.POST:
        form = UploadForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    template = "sklad/upload.html"
    context = {'form': UploadForm}
    return render(request, template, context)


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
