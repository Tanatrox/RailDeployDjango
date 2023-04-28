from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import *
from .models import *
import datetime
from django.contrib.auth import views as auth_views

# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("pelisyseries:index")
		messages.error(request, "Registro sin éxito. Datos proporcionados no válidos.")
	form = NewUserForm()
	return render (request=request, template_name="pelisyseries/register.html", context={"form":form})


def login_request(request):
	if request.method == "POST":
		form = IniciarSesionForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("pelisyseries:index")
			else:
				messages.info(request,"Nombre de usuario o contraseña incorrectos.")
		else:
			messages.info(request,"Nombre de usuario o contraseña incorrectos.")
	form = IniciarSesionForm()
	return render(request=request, template_name="pelisyseries/login.html", context={"form":form})

class EditarPerfil(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'pelisyseries:login'
    form_class=EditarPerfilForm
    template_name='pelisyseries/EditarPerfil.html'
    success_url= reverse_lazy('pelisyseries:perfil')

    def get_object(self):
        return self.request.user

# @login_required(login_url='pelisyseries:home')
def logout_request(request):
    logout(request)
    return redirect('pelisyseries:login')


def home(request):
    if request.user.is_authenticated:
        return redirect('pelisyseries:index')
    else:
        return render(request, 'pelisyseries/home.html')


@login_required(login_url='pelisyseries:login')
def index(request):
    contenido = Contenido.objects.all()
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/index.html', context)

@login_required(login_url='pelisyseries:home')
def peliculas(request):
    contenido = Contenido.objects.filter(tipo='Pelicula')
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/peliculas.html', context)

@login_required(login_url='pelisyseries:home')
def series(request):
    contenido = Contenido.objects.filter(tipo='Serie')
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/series.html', context)

@login_required(login_url='pelisyseries:home')
def categorias(request):
    return render(request, 'pelisyseries/categorias.html')

@login_required(login_url='pelisyseries:home')
def recientes(request):
    d = datetime.date(2022, 9, 1)
    contenido = Contenido.objects.all()
    context = {
        'contenido': contenido,
        'fecha': d
    }
    return render(request, 'pelisyseries/recientes.html', context)

@login_required(login_url='pelisyseries:home')
def accion(request):
    contenido = Contenido.objects.filter(genero='Acción')
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/accion.html', context)

@login_required(login_url='pelisyseries:home')
def animacion(request):
    contenido = Contenido.objects.filter(genero="Animación")
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/animacion.html', context)

@login_required(login_url='pelisyseries:home')
def aventura(request):
    contenido = Contenido.objects.filter(genero="Aventura")
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/aventura.html', context)

@login_required(login_url='pelisyseries:home')
def terror(request):
    contenido = Contenido.objects.filter(genero="Terror")
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/terror.html', context)

@login_required(login_url='pelisyseries:home')
def ciencia_ficcion(request):
    contenido = Contenido.objects.filter(genero="Ciencia Ficción")
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/ciencia_ficcion.html', context)

@login_required(login_url='pelisyseries:home')
def comedia(request):
    contenido = Contenido.objects.filter(genero="Comedia")
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/comedia.html', context)

@login_required(login_url='pelisyseries:home')
def drama(request):
    contenido = Contenido.objects.filter(genero="Drama")
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/drama.html', context)

@login_required(login_url='pelisyseries:home')
def familiar(request):
    contenido = Contenido.objects.filter(genero="Familiar")
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/familiar.html', context)

@login_required(login_url='pelisyseries:home')
def fantasia(request):
    contenido = Contenido.objects.filter(genero="Fantasía")
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/fantasia.html', context)

@login_required(login_url='pelisyseries:home')
def misterio(request):
    contenido = Contenido.objects.filter(genero="Misterio")
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/misterio.html', context)

@login_required(login_url='pelisyseries:home')
def musicales(request):
    contenido = Contenido.objects.filter(genero="Musicales")
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/musicales.html', context)

@login_required(login_url='pelisyseries:home')
def perfil(request):
    return render(request, 'pelisyseries/perfil.html')

@login_required(login_url='pelisyseries:home')
def Reproduccion(request, id):
    contenido = Contenido.objects.get(id=id)
    me_gusta = False
    fav = False

    if contenido.meGusta.filter(id=request.user.id).exists():
        me_gusta = False
    else:
        me_gusta = True

    if contenido.favoritos.filter(id=request.user.id).exists():
        fav = False
    else:
        fav = True

    context = {
        'contenido':contenido,
        'me_gusta':me_gusta,
        'fav':fav,
        }
    return render(request, 'pelisyseries/reproductor.html', context)

@login_required(login_url='pelisyseries:home')
def Me_gusta(request, id):
    contenido = get_object_or_404(Contenido, id=request.POST.get('contenido_id'))
    if contenido.meGusta.filter(id=request.user.id).exists():
        contenido.meGusta.remove(request.user)
    else:
        contenido.meGusta.add(request.user)
    return HttpResponseRedirect(reverse('pelisyseries:reproducir', args=[str(id)]))

@login_required(login_url='pelisyseries:home')
def Favoritos(request, id):
    contenido = get_object_or_404(Contenido, id=request.POST.get('contenido_id'))
    if contenido.favoritos.filter(id=request.user.id).exists():
        contenido.favoritos.remove(request.user)
    else:
        contenido.favoritos.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    # return HttpResponseRedirect(reverse('pelisyseries:reproducir', args=[str(id)]))

@login_required(login_url='pelisyseries:home')
def Favoritos_lista(request):
    user = request.user
    contenido = user.favoritos.all()
    context = {'contenido': contenido}
    return render(request, 'pelisyseries/favoritas.html', context)

@login_required(login_url='pelisyseries:home')
def Busqueda(request):
    if request.method == 'POST':
        buscar = request.POST['buscar']
        contenido = Contenido.objects.filter(nombre__icontains=buscar)
        return render(request, 'pelisyseries/busqueda.html', {'buscar':buscar, 'contenido':contenido})
    else:
        return render(request, 'pelisyseries/busqueda.html', {'buscar':buscar, 'contenido':contenido})

    

