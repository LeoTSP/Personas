from django.contrib import admin

# Register your models here.
from personas.models import Persona, Domicilio

#Registrar la clase de modelo
admin.site.register(Persona)

#Registrar la clase de modelo: Domicilio
admin.site.register(Domicilio)