from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.
class Contenido(models.Model):
    nombre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    estreno = models.DateField(auto_now_add=False, blank=True, null=True)
    descripcion = models.TextField()
    video = models.IntegerField(null=True, blank=True, default=1)
    caratula = models.ImageField(null=True, blank=True, upload_to='myimg')
    tipo = models.CharField(max_length=50, null=True, blank=True)
    genero = models.CharField(max_length=255, null=True, blank=True)
    anio = models.IntegerField(null=True, blank=True)
    meGusta = models.ManyToManyField(User, related_name='Me_Gusta')
    favoritos = models.ManyToManyField(User, related_name='favoritos')

    def __str__(self):
        return f'{self.nombre} : {self.genero}' 

    def me_gusta_total(self):
        return self.meGusta.count()
    



