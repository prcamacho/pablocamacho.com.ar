from django.urls import path
from .views import vista_inicial

app_name='unsa'

urlpatterns = [
    path('',vista_inicial,name='vista_inicial')
]
