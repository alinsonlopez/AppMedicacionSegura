from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Medicines, Categories
from .forms import MedicinesForm, LoginForm


# Create your views here.


def log_in(request):
    # Diccionario que almacena los datos que enviamos a la vista
    form = LoginForm(
        request.POST or None
    )
    context = {'message': None, 'form': form}
    if request.POST and form.is_valid():
        # Verificar credenciales
        # Devuelve un objeto User si las credenciales son válidas.
        # Si las credenciales no son válidas, devuelve None
        user = authenticate(**form.cleaned_data)
        if user is not None:
            # Verificar si el usuario esta activo
            if user.is_active:
                # Adjuntar usuario autenticado a la sesión actual
                login(request, user)
                # Redireccionar a una vista utilizando el nombre de la url
                return redirect('medicines:home')
            else:
                context['message'] = 'El usuario ha sido desactivado'
        else:
            context['message'] = 'Usuario o contraseña incorrecta'
    return render(request, 'medicines/login.html', context)


# decorador para restringir el acceso a solo usuarios autenticados
@login_required
def log_out(request):
    logout(request)
    return redirect('medicines:log-in')


@login_required
def movie_list(request):
    medicines = Medicines.objects.all()
    return render(request, 'medicines/index.html', {'medicines': medicines})


@login_required
def movie_detail(request, pk):
    try:
        # recuperamos el objeto mediante la
        # API de abstracción de base de datos
        # que ofrece Django
        m = Medicines.objects.get(pk=pk)
    except Medicines.DoesNotExist:
        raise Http404("Esta pelicuala no existe")

    # version con shortcuts de django, equivalente al codigo anterior
    # m = get_object_or_404(Medicines, pk=pk)
    return render(request, 'medicines/detail.html', {'movie': m})


@login_required
def movie_create(request, **kwargs):
    # Intanciamos la clase form
    # si el diccionario request.POST no esta vacio
    # la instancia se creara con dichos datos, sino estara vacia
    form = MedicinesForm(
        request.POST or None,
        request.FILES or None
    )
    # Comprobamos que la peticion es del motodo POST
    # y que el formulario es valido
    if request.POST and form.is_valid():
        # Guardamos el objeto
        form.save()
        # redirigir a una nueva URL
        return redirect('medicines:home')
    return render(request, 'medicines/form.html', {'form': form})


@login_required
def movie_update(request, **kwargs):
    # recuperamos el objeto a actualizar
    movie = Medicines.objects.get(pk=kwargs.get('pk'))
    # inicializamos el formulario con el objeto recuperado
    form = MedicinesForm(
        request.POST or None,
        instance=movie
    )
    if request.POST and form.is_valid():
        form.save()
        return redirect('medicines:home')
    return render(request, 'medicines/form.html', {'form': form})


@login_required
def movie_delete(request, **kwargs):
    movie = Medicines.objects.get(pk=kwargs.get('pk'))
    movie.delete()
    return redirect('medicines:home')


@login_required
def category_list(request):
    categories = Categories.objects.all()
    return render(request, 'medicines/category/category_list.html', {'categories': categories})