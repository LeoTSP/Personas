from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
# Crearemos el método
from personas.forms import PersonaForm
from personas.models import Persona

#Método
def detallePersona(request,id):
    #Declarar la variable la cual recibe la clase
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)

    #Creamos la plantilla
    return render(request,'personas/detalle.html',{'persona':persona})


#Creamos una variable,
# PersonaForm = modelform_factory(Persona, exclude=[])


#Segundo Método
def personaNueva(request):

    #Validaremos el uso del método POST
    if request.method == 'POST':
        #Declaramos la variable que recibe la clas
        formaPersona = PersonaForm(request.POST)

        #Realizamos la validación
        if formaPersona.is_valid():
            formaPersona.save()

            #Realizaremos el redireccionamiento
            return redirect('index')

        else:
            # Haremos uso de la plantilla
            return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

    else:
        # Instanciar
        formaPersona = PersonaForm()

        # Haremos uso de la plantilla
        return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})
