from django.shortcuts import render, get_object_or_404, redirect
from .models import Pokemon
from django.core.paginator import Paginator
from .forms import PokemonForm
from .services.pokemons_services import load_pokemons  # Ensure the service is used for data population
# List all Pokémon with pagination
def pokemon_list(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    pokemons = Pokemon.objects.all()

    # Filtrar los Pokémon si se proporciona un término de búsqueda
    if query:
        pokemons = pokemons.filter(name__icontains=query)

    paginator = Paginator(pokemons, 12)  # Mostrar 12 Pokémon por página
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'pokemon_list.html', {'page_obj': page_obj, 'query': query})

# Show details for a single Pokémon
def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})

# Create a new Pokémon
def pokemon_create(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pokemon_list")
    else:
        form = PokemonForm()
    return render(request, "pokemon_form.html", {"form": form})

# Update an existing Pokémon
def pokemon_update(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == "POST":
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect("pokemon_list")
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, "pokemon_form.html", {"form": form})

# Delete a Pokémon
def pokemon_delete(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    pokemon.delete()
    return redirect('pokemon_list')