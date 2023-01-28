from django.urls import path
from .views import ver_tela

urlpatterns = [
    path('cnab', ver_tela, name='home')
]

