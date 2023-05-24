from django.contrib import admin
from .models import Salon, Client, Master, Service, Order, Review


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'time_work')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone')


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone', 'speciality')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'salon', 'service', 'master', 'date', 'time')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'master', 'rate')
