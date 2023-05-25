from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = "beauty"


urlpatterns = [
    path('', views.view_index, name='start_page'),
    path('service/', views.view_service, name='service_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
