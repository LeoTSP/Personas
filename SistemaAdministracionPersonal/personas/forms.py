#Realizamos la importación
from django.forms import ModelForm, EmailInput
from personas.models import Persona

#Creamos la clase
class PersonaForm(ModelForm):
    class Meta:
        #declaramos la variable y asignamos la clase
        model = Persona
        fields = '__all__'
        widgets = {
            'email':EmailInput(attrs={'type':'email'})
        }