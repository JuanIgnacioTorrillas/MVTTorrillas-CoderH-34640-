from django.shortcuts import render
from django.http import HttpResponse
from AppFamilia.models import *
from django.template import loader

#VISTAS

def madre(request):

    madre=familiar(nombre="Laura",fecha_de_nacimiento="1964-7-5",dni=27095841)
    madre.save()
    
    nom="Laura"
    fecha="1964-7-5"
    dni=27095841
    
    dicc={"Nombre":nom,"Fecha_de_Nacimiento":fecha,"DNI":dni}
    
    plantilla=loader.get_template("template.html")
    docu=plantilla.render(dicc)
    
    return HttpResponse (docu)
    
def padre(request):

    padre=familiar(nombre="Mario",fecha_de_nacimiento="1964-10-14",dni=27087842)
    padre.save()
    
    nom="Mario"
    fecha="1964-10-14"
    dni=27087842
    
    dicc={"Nombre":nom,"Fecha_de_Nacimiento":fecha,"DNI":dni}
    
    plantilla=loader.get_template("template.html")
    docu=plantilla.render(dicc)
    
    return HttpResponse (docu)

def hermana(request):

    hermana=familiar(nombre="Dolores",fecha_de_nacimiento="2000-2-23",dni=45095472)
    hermana.save()
    
    nom="Dolores"
    fecha="2000-2-23"
    dni=45095472
    
    dicc={"Nombre":nom,"Fecha_de_Nacimiento":fecha,"DNI":dni}
    
    plantilla=loader.get_template("template.html")
    docu=plantilla.render(dicc)
    
    return HttpResponse (docu)