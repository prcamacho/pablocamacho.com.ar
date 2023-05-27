from django.shortcuts import render
from .models import Materia
from django.http import HttpResponse


# Create your views here.

def vista_inicial(request):
    materias=Materia.objects.all()
    return render(request,'unsa/inicio.html',{'materias':materias})
