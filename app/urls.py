from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("add/",views.addPerson),
    path("list/",views.get_all_person)
]
