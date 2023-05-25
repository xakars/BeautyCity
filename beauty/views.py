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
    return render(request, template_name="service.html", context={})
