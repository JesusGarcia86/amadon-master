from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_reroute),
    path('amadon', views.amadon),
]