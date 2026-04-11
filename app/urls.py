from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('sobre/', about, name='about'),
    path('reservas/', reservations, name='reservations'),
]