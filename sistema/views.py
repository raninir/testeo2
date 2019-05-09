from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
from .forms import Mascotas,AgregarUsuario, Login
from .models import Mascota, Usuario
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


acciones=[
   {'Mostrar':'Home','url':'inicio'}
]


#view para ingresar al index.html
def index(request):
    return render(request, "index.html")

def formulario(request):
    return render(request, "formulario.html")
#view para ingresar al ADMIN
def admin(request):
    return render(request, "/admin")


#view para poder salir de la cuenta
def salir(request):
    logout(request)
    return redirect('/')   

#view para poder registrar un nuevo usuario
def registrarse(request):
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        regDB=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        usuario=Usuario(user=regDB)
        regDB.save()
        usuario.save()
    usuarios=Usuario.objects.all()
    form=AgregarUsuario()
    return render(request,"registrarse.html",{'form':form,'usuarios':usuarios,'acciones':acciones,})

#view para ingresar 
def ingresar(request):
    form=Login(request.POST or None )
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('inicio')
    return render(request,"login.html",{'form':form,})


#Funcion que requiere estar iniciado sesion 
@login_required(login_url='login')
#View de mascota que se encuentran disponibles
def lista(request):
    actual=request.user
    form=Mascotas(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        mascota=Mascota(codigoMascota=data.get("codigoMascota"),fotoMascota=data.get("fotoMascota"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),descripcionMascota=data.get("descripcionMascota"),estado=data.get("estado"))
        mascota.save()
        #Filtro para que muestren mascota disponible
    mascota=Mascota.objects.filter(estado='disponible')
    #Paginador de la lista de mascota
    paginator = Paginator(mascota, 3)
    page = request.GET.get('page')
    mascota = paginator.get_page(page)
    form=AgregarUsuario()
    return render(request,"listaMascota.html",{'paginator':paginator,'actual':actual,'form':form,'mascota':mascota,'acciones':acciones,})


@login_required(login_url='login')
#View para cambiar la password 
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Tu contraseña se ha actualizado'))
            return redirect('change_password')
        else:
            messages.error(request, ('Por favor corrija el error .'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {
        'form': form
    })
