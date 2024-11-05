from django.urls import path

from . import views

urlpatterns = [
    path("", views.getAllItems, name="index"),
    path("item/", views.findOneItem, name="findOne"),
]