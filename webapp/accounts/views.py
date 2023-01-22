
from logging import getLogger

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView

from sklad.views import home

LOGGER = getLogger()


class SignUpView(CreateView):
    template_name = 'accounts_back/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

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

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'sklad/signup.html', {'form': form})