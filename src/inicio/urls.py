from django.urls import path
from .views import vista_inicio

app_name='inicio'

urlpatterns = [
    path('',vista_inicio, name='vista_inicio')
]
