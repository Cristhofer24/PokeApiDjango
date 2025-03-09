from django.shortcuts import render ,get_object_or_404
from .models import Pokemon
from django.core.paginator import Paginator
# Create your views here.
def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    paginator = Paginator(pokemons, 12)  
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'pokemon_list.html', {'page_obj': page_obj})

def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})
