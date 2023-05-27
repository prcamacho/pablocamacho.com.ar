from django.shortcuts import render

# Create your views here.

def vista_inicial(request):
    return render(request,'argentina_programa/inicio.html')
