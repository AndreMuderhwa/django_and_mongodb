from django.shortcuts import render
from .models import personne_Collection
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Bienvenue </h2>")


def addPerson(request):
    records={
        "nom":"Jennifer",
        "postnom":"Lopez",
        "adresse":["Himbi","Katoy","Majengo"]
    }
    personne_Collection.insert_one(records)
    return HttpResponse("New Personne added")


def get_all_person(request):
    persons=personne_Collection.find()
    return (persons)