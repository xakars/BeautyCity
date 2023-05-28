from django.shortcuts import render
from beauty.models import Service, Master, Salon, Review


def view_index(request):
    services = Service.objects.all()
    salons = Salon.objects.all()
    masters = Master.objects.all()
    reviews = Review.objects.all()
    return render(
        request,
        template_name="index.html",
        context={
            'salons': salons,
            'services': services,
            'masters': masters,
            'reviews': reviews
        }
    )


def view_service(request):
    services = Service.objects.all()
    salons = Salon.objects.all()
    masters = Master.objects.all()
    return render(
        request,
        template_name="service.html",
        context={
            'salons': salons,
            'services': services,
            'masters': masters,
        }
    )


def service_finally(request):
    # Логика для отображения страницы serviceFinally.html
    return render(
        request,
        'serviceFinally.html',
    )
