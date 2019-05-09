from django import forms

from .models import Mascota

estados=(
    ('Rescatado','Rescatado'),
    ('Disponible','Disponible'),
    ('Adoptado','Adoptado'),
)



#Class agregarusuarios para agregar usuarios con sus atributos
class AgregarUsuario(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")

#Class login con sus atributos para logearse
class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

#Class Mascotas con sus atributos para agregar
class Mascotas(forms.Form):

    fotoMascota=forms.ImageField()
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre Mascota")
    razaMascota=forms.CharField(widget=forms.TextInput(),label="Raza Mascota")
    descripcionMascota=forms.CharField(widget=forms.TextInput(),label="Descripcion")
    estado=forms.ChoiceField(choices=estados, initial='Rescatado')
    