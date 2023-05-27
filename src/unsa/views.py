from django.shortcuts import render
from .models import Materia
from django.http import HttpResponse


# Create your views here.

def listar_materias(request):
    materias=Materia.objects.all()
    return render(request,'unsa/listado_materias.html',{'materias':materias})
