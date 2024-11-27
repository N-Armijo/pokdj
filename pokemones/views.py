from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Pokemon
from .forms import PokemonForm
from django.contrib.auth.forms import UserCreationForm #No pertenece aqui
from django.contrib import messages

# Create your views here.
def pagina_principal(request):
    pokemones_list = Pokemon.objects.all()
    paginator = Paginator(pokemones_list, 5)  # Paginación de 5 elementos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pagina_principal.html', {
        'page_obj': page_obj,
        'user_authenticated': request.user.is_authenticated,
    })

@login_required ###########################
def listar_pokemon(request):
    pokemones = Pokemon.objects.select_related('tipo').all()
    paginator = Paginator(pokemones, 5)  # Paginación de 5 elementos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'listar_pokemon.html', {'page_obj': page_obj})

@login_required
def crear_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pokemon')
    else:
        form = PokemonForm()
    return render(request, 'crear_pokemon.html', {'form': form})

@login_required
def editar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('listar_pokemon')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'editar_pokemon.html', {'form': form})

@login_required
def eliminar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('listar_pokemon')
    return render(request, 'eliminar_pokemon.html', {'pokemon': pokemon})

#No corresponde aqui
def registro_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')  # Redirigir al login después de registro
    else:
        form = UserCreationForm()
    
    return render(request, 'registro_usuario.html', {'form': form})