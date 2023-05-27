from django.contrib import admin
from .models import Materia
# Register your models here.

class MateriaAdmin(admin.ModelAdmin):
    list_display=['nombre']
    search_fields=['nombre']
    list_filter=[]

admin.site.register(Materia)
