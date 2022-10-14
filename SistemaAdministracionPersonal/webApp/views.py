#Realizaremos la importación
from django.http import HttpResponse
from django.shortcuts import render

#Importaremos la clase
from personas.models import Persona

# Create your views here.
def bienvenido(request):
    #Realizaremos un retorno
    # return HttpResponse('SEMINARIO DE PROGRAMACIÓN')

    #Manejo de funciones
    noPeronasBd = Persona.objects.count()

    #Declarar una variable, a la cual le asignamos el contenido de la tabla
    personas = Persona.objects.all()

    #Haremos uso de Templates
    #Diccionario: Key-Value
    return render(request, 'bienvenido.html', {'no_PersonasBd': noPeronasBd,'personas':personas})



#Creamos la función que permita retornar un mensaje de despedida
def despedir(request):
    #Realizaremos el retorno del mensaje
    return HttpResponse('Muchas gracias por utilizar los serivios de nuestra página')