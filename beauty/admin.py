from django.contrib import admin
from .models import Salon, Client, Master, Service, Order, Review, Category, DayOfWork


class WorkDayInline(admin.TabularInline):
    model = DayOfWork
    extra = 1


@admin.register(Category)
class SalonAdmin(admin.ModelAdmin):
    pass


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    inlines = [WorkDayInline]
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(DayOfWork)
class DayOfWorkAdmin(admin.ModelAdmin):
    pass