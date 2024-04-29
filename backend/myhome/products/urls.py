
from django.urls import path
from .views import *

urlpatterns = [
    path('populate_products/', populate_products),
]
