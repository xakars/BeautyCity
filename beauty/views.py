from django.shortcuts import render
from beauty.models import Service, Master, Salon, Review, Schedule


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
    schedules = Schedule.objects.all()
    return render(
        request,
        template_name="service.html",
        context={
            'salons': salons,
            'services': services,
            'masters': masters,
            'schedules': schedules
        }
    )
