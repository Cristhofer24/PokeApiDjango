from django.db import models

class PokemonSprites(models.Model):
    front_default = models.URLField(null=True, blank=True)
    front_shiny = models.URLField(null=True, blank=True)
    front_female = models.URLField(null=True, blank=True)
    front_shiny_female = models.URLField(null=True, blank=True)
    back_default = models.URLField(null=True, blank=True)
    back_shiny = models.URLField(null=True, blank=True)
    back_female = models.URLField(null=True, blank=True)
    back_shiny_female = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Sprites for {self.id}"

class PokemonTypeInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name

class PokemonType(models.Model):
    slot = models.IntegerField()
    type_info = models.ForeignKey(PokemonTypeInfo, on_delete=models.CASCADE, related_name="pokemon_types")

    class Meta:
        unique_together = ('slot', 'type_info')

    def __str__(self):
        return f"{self.type_info.name} (Slot {self.slot})"

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    weight = models.FloatField()
    height = models.FloatField()
    sprites = models.OneToOneField(PokemonSprites, on_delete=models.CASCADE)
    types = models.ManyToManyField(PokemonType, related_name="pokemons")

    def __str__(self):
        return self.name

class PokemonResponse(models.Model):
    count = models.IntegerField()
    next = models.URLField(null=True, blank=True)
    previous = models.URLField(null=True, blank=True)
    results = models.ManyToManyField(Pokemon, related_name="responses")

    def __str__(self):
        return f"Response with {self.count} results"

class PokemonListViewModel(models.Model):
    pokemons = models.ManyToManyField(Pokemon, related_name="list_views")
    current_page = models.IntegerField()
    total_pages = models.IntegerField()

    def __str__(self):
        return f"Page {self.current_page} of {self.total_pages}"

    @property
    def has_next(self):
        return self.current_page < self.total_pages

    @property
    def has_previous(self):
        return self.current_page > 1
