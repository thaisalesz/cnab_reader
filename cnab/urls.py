from django.urls import path
from .views import home

urlpatterns = [
    path('cnab', home, name='home')
]

