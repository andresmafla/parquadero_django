from datetime import timezone
from math import ceil
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from parqueadero.models import carro
from .forms import CarroForm

# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def carros(request):
    carros = carro.objects.all()
    return render(request, 'carros/index.html', {'Carros': carros})


def crear(request):
    formulario = CarroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('carros')
    return render(request, 'carros/crear.html', {'formulario': formulario})


def borrar(request, id):
    carro1 = carro.objects.get(id=id)
    carro1.delete()
    return redirect('carros')


def cobro(request, id):
    carro1 = carro.objects.get(id=id)
    carro1.tiempo = ceil(
        ((timezone.now() - carro1.entrada).total_seconds() / 3600))
    carro1.salida = timezone.now()
    print(carro1.tipo)
    if str(carro1.tipo) == 'carro':
        carro1.total = 3000+(500*(carro1.tiempo-1))
    elif str(carro1.tipo) == 'moto':
        carro1.total = 2000+(500*(carro1.tiempo-1))
    elif str(carro1.tipo) == 'bicicleta':
        carro1.total = 1000+(500*(carro1.tiempo-1))
    return render(request, 'carros/cobro.html',{'carro':carro1})


def formulario(request):
    return render(request, 'carros/formulario.html')