from django.urls import path
from .views import listar_materias

app_name='unsa'

urlpatterns = [
    path('',listar_materias,name='listar_materias')
]
