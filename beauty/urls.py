from django.urls import path
from . import views


app_name = "beauty"


urlpatterns = [
    path('', views.view_index, name='start_page'),
]
