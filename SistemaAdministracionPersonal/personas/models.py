from django.db import models

#Creamos la clase que hace referencia al domicilio
class Domicilio(models.Model):
    #Definir atributos y asignar campos
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    colonia = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)

    #Haremos uso del metodo de sobre escritura
    def __str__(self):
        return f'DOMICILIO: {self.id}: {self.calle}, {self.no_calle}, {self.colonia}, {self.ciudad}'


# Create your models here.
class Persona(models.Model):
    #Iniciamos con la definicion de los campos
    nombre = models.CharField(max_length=255)
    apellidoPaterno = models.CharField(max_length=255)
    apellidoMaterno = models.CharField(max_length=255)
    centroTrabajo = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    #Establecemos una llave foranea (ForeignKey)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    #Utilizaremos el método de sobre escritura
    def __str__(self):
        return f'PERSONA: {self.id}: ,{self.nombre}, {self.apellidoPaterno}, {self.apellidoMaterno}, {self.centroTrabajo}, {self.email}'
