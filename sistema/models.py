from django.db import models
from django.contrib.auth.models import User

#Class mascota con sus atributos
class Mascota (models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    fotoMascota = models.ImageField(upload_to="fotos/")
    nombreMascota=models.CharField(max_length=20,verbose_name="Nombre Mascota")
    razaMascota=models.CharField(max_length=30,default="",verbose_name="Raza Mascota")
    descripcionMascota=models.CharField(max_length=50,default="",verbose_name="Descripcion")
    estado=models.CharField(max_length=20,verbose_name="Estado")
#Class usuario con sus atributos generados 
class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null = True)


