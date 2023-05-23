from django.shortcuts import render


def view_index(request):
    return render(request, template_name="index.html", context={})


def view_service(request):
    return render(request, template_name="service.html", context={})
