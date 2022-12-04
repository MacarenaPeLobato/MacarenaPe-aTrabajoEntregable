from django.shortcuts import render
from .models import Padre, Madre, Hijo, Hija
from django.http import HttpResponse #LO IMPORTO 

# Create your views here.
def padre (request):
    pa= Padre(nombre="Ruben", apellido="pena", celular="2955208457", profesion="herrero")
    pa.save()
    info_padre=f"El nombre del padre de familia es {pa.nombre} {pa.apellido}, su telefono es {pa.celular} y su profesion es {pa.profesion}"
    return HttpResponse (info_padre)

def madre (request):
    ma= Madre (nombre="Maria", apellidocasada="Pena", apellidosoltera="Martinez", profesion= "ser la mejor en todo" )
    ma.save()
    info_ma=f"La madre de la familia es {ma.nombre}, y su apellido heredado es {ma.apellidosoltera} y su profesion es {ma.profesion}"
    return HttpResponse (info_ma)

def hija (request):
    hijita= Hija (nombre="Macarena", dni="12343567", estudiando= "en el mejor curso de Python" )
    hijita.save()
    info_hija=f"La mas pequena de la familia es {hijita.nombre}, su numero de documento es: {hijita.dni}. Actualmente esta estudiando en {hijita.estudiando}"
    return HttpResponse (info_hija)

def hijo (request):
    hijazo= Hijo (nombre="Emanuel", dni="98765432")
    hijazo.save()
    info_hijo=f"El primer hijo de la familia se llama {hijazo.nombre}, su numero de documento es: {hijazo.dni}."
    return HttpResponse (info_hijo)