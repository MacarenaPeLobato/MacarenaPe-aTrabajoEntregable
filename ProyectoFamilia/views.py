from django.http import HttpResponse
from django.template import Template, Context

def apellido (request):
    return HttpResponse ("El apellido de esta familia es Peña")

def integrantes (request):
    return HttpResponse ("Los integrantes de esta familia son los siguientes: Macarena, Emanuel, Maria y Ruben")

def probando (request):
    diccionario= {"integrante1": "Macarena", "integrante2": "Maria", "integrante3": "Ruben", "integrante4": "Emanuel", "edad": [26, 64, 64, 29]}
    archivo=open("C:/Users/fedef/Desktop/MACA PYTHON/TrabajoEntregable/ProyectoFamilia/Plantillas/template.html")
    template= Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario)
    documento=template.render(contexto)
    return HttpResponse(documento)


