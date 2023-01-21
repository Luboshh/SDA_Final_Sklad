"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import path

from accounts import views as accounts_views

from sklad import views as sklad_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', sklad_views.home, name='home'),
    path('upload/', sklad_views.upload, name='upload'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password_change/',
         PasswordChangeView.as_view(template_name="registration/password_change.html"),
         name='password_change'),
    path('accounts/password_change/done/',
         PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),
         name='password_change_done'),
    path('accounts/signup/', accounts_views.SignUpView.as_view(), name='signup'),

]

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='Participants'))
