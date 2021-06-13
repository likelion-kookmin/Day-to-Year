from django.contrib import admin
from .views import *
from django.urls import path
urlpatterns = [
    path('rentallist/', rental , name="rentallist"),
    path('product/<str:rental_id>', product , name="product"),
    path('new/', new, name="new"),
    path('submit/',submit, name="submit")
] 
