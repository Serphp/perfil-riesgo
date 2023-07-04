from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import forms

class DatosPersonaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    segundo_nombre = forms.CharField(max_length=50, required=False)
    primer_apellido = forms.CharField(max_length=50)
    segundo_apellido = forms.CharField(max_length=50, required=False)
    genero = forms.ChoiceField(choices=[('Hombre', 'Hombre'), ('Femenino', 'Femenino')])
    pais_nacimiento = forms.ChoiceField(choices=[('Panamá', 'Panamá'), ('Otros países', 'Otros países')])
    pais_residencia = forms.ChoiceField(choices=[('Panamá', 'Panamá'), ('Otros países', 'Otros países')])
    profesion = forms.ChoiceField(choices=[('Abogado', 'Abogado'),
                                           ('Ingeniería', 'Ingeniería'), 
                                           ('Médico', 'Médico'), 
                                           ('Contador', 'Contador'),
                                           ('Otras profesiones', 'Otras profesiones')])
    edad = forms.ChoiceField(choices=[('Menos 25', 'Menos 25'),
                                      'Entre 25 y 55',
                                      'Mayor de 55'])
    Nivel_de_ingresos = forms.ChoiceField(choices=[('Menos de 20K anual',
                                                    'Entre 20k y 75k',
                                                    'Mayor de 75k')])
    PEP = forms.ChoiceField(choices=[('Sí', 'Sí'), ('No', 'No')])

def index(request):
    if request.method == 'POST':
        form = DatosPersonaForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            puntaje_riesgo = calcular_puntaje_riesgo(datos)
            return redirect('mostrar_resultado', puntaje_riesgo=puntaje_riesgo)
    else:
        form = DatosPersonaForm()
    
    return render(request, 'index.html', {'form': form})

   # return render(request, 'index.html')

#def calcular_puntaje(request):

def calcular_puntaje_riesgo(datos):
    puntaje = 0

    # Calcular puntaje en base al país de nacimiento
    if datos['pais_nacimiento'] == 'Panamá':
        puntaje += 100
    else:
        puntaje += 200

    # Agregar aquí la lógica para calcular el puntaje en base a los valores y pesos ingresados

    return puntaje

def mostrar_resultado(request, puntaje_riesgo):
    return render(request, 'mostrar_resultado.html', {'puntaje_riesgo': puntaje_riesgo})