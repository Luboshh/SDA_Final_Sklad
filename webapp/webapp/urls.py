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
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password_change/',
         PasswordChangeView.as_view(template_name="registration/password_change.html"),
         name='password_change'),
    path('accounts/password_change/done/',
         PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),
         name='password_change_done'),
    #path('accounts_back/signup/', accounts_views.SignUpView.as_view(template_name="sklad/signup.html"), name='signup'),
    path('accounts/signup/', accounts_views.signup_view, name='signup'),
    path('', sklad_views.home, name='home'),
    path('add_item/', sklad_views.add_item, name='add_item'),
    path('add_item/<str:pk>/', sklad_views.update_item, name='update_item'),
    path('tostock/', sklad_views.to_stock, name='to_stock'),
    path('tostock/<str:pk>/', sklad_views.update_tran, name='update_tran'),
    path('unload/', sklad_views.unload_hardware, name='unload'),
    path('unload/<str:pk>/', sklad_views.update_hardware, name='update_hardware'),
    path('add_item/', sklad_views.add_item, name='add_item'),
    path('home/', sklad_views.home, name='home'),
    path('hardwaretypes/', sklad_views.hardware_types, name='hardware_types'),
    path('hardwaretypes/<str:pk>/', sklad_views.update_hardware_type, name='update_hardwaretype'),
    path('itemsforhardware/<str:pk>/', sklad_views.item_for_hardware, name='items_for_hardwware'),
    path('orders/', sklad_views.orders, name='orders'),
    path('orders/<str:pk>/', sklad_views.update_order, name='update_order'),
    path('customers/', sklad_views.customers, name='customers'),
    path('customers/<str:pk>/', sklad_views.update_customer, name='update_customer'),
    ]



