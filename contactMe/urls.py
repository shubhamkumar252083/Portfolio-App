from django.urls import path
from .views import *

urlpatterns = [
    path("", contactMe_index, name="contactMe_index"),
]
