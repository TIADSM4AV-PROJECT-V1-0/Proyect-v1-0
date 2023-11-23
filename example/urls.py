# example/urls.py
from django.urls import path

from example.views import index, dishes


urlpatterns = [
    path('', index),
    path('dishes', dishes),
]