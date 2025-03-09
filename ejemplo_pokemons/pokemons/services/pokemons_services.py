import requests
from ..models import Pokemon, PokemonSprites, PokemonType, PokemonTypeDetails

API_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_all_pokemons(limit=100, offset=0):
    url = f"{API_URL}?limit={limit}&offset={offset}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    return []

def get_pokemon_details(pokemon_id):
    response = requests.get(f"{API_URL}{pokemon_id}/")
    if response.status_code == 200:
        return response.json()
    return None

def load_pokemons():
    if Pokemon.objects.exists():
        return "Los Pokémon ya están cargados."

    pokemons_data = get_all_pokemons()  
    loaded_count = 0

    for pokemon in pokemons_data:
        details = get_pokemon_details(pokemon["name"])  
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