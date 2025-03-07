import requests
from ..models import Pokemon, PokemonSprites, PokemonType, PokemonTypeDetails

API_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_all_pokemons():
    """Obtiene todos los Pokémon desde la API (paginas)"""
    pokemons = []
    next_url = f"{API_URL}?limit=100"  # Puedes ajustar el límite a 100 o el máximo permitido por la API
    
    while next_url:
        response = requests.get(next_url)
        if response.status_code == 200:
            data = response.json()
            pokemons.extend(data["results"])
            next_url = data["next"]  # El URL para la siguiente página de resultados
        else:
            break
    
    return pokemons

def get_pokemon_details(pokemon_id):
    """Obtiene detalles de un Pokémon por su ID"""
    response = requests.get(f"{API_URL}{pokemon_id}/")
    if response.status_code == 200:
        return response.json()
    return None

def load_pokemons():
    """Carga todos los Pokémon en la base de datos"""
    if Pokemon.objects.exists():
        return "Los Pokémon ya están cargados."

    pokemons_data = get_all_pokemons()  # Obtiene todos los Pokémon
    loaded_count = 0

    for pokemon in pokemons_data:
        # Obtener detalles del Pokémon por su URL
        details = requests.get(pokemon["url"]).json()
        if not details:
            continue

        # Crear sprites
        sprites = PokemonSprites.objects.create(
            front_default=details["sprites"].get("front_default"),
            front_shiny=details["sprites"].get("front_shiny"),
            front_female=details["sprites"].get("front_female"),
            front_shiny_female=details["sprites"].get("front_shiny_female"),
            back_default=details["sprites"].get("back_default"),
            back_shiny=details["sprites"].get("back_shiny"),
            back_female=details["sprites"].get("back_female"),
            back_shiny_female=details["sprites"].get("back_shiny_female"),
        )

        # Crear Pokémon
        pokemon_obj = Pokemon.objects.create(
            id=details["id"],
            name=details["name"],
            weight=details["weight"],
            height=details["height"],
            sprites=sprites
        )

        # Guardar tipos
        for type_data in details.get("types", []):
            type_detail, _ = PokemonTypeDetails.objects.get_or_create(
                name=type_data["type"]["name"],
                url=type_data["type"]["url"]
            )
            PokemonType.objects.create(
                slot=type_data["slot"],
                type=type_detail,
                pokemon=pokemon_obj
            )

        loaded_count += 1

    return f"{loaded_count} Pokémon cargados exitosamente."
