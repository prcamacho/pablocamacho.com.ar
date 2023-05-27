from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre=models.CharField(max_length=30)
    cuatrimestre=models.PositiveSmallIntegerField()
    creado=models.DateTimeField(auto_now_add=True)
    modificado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        ordering=['nombre']

class Clase(models.Model):
    materia=models.ForeignKey(Materia,on_delete=models.CASCADE)
    unidad=models.CharField(max_length=50)
    temas=models.TextField()
    link=models.URLField()

    def __str__(self):
        return f"{self.materia}-{self.unidad}"