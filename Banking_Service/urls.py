from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('customers',views.customers,name='Customers'),
    path('transactions',views.trans,name='Transactions')
]