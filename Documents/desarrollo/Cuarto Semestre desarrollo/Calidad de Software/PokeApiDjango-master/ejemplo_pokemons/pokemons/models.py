from django.db import models

# Create your models here.
class PokemonSprites(models.Model):
    front_default = models.URLField(null=True, blank=True)
    front_shiny = models.URLField(null=True, blank=True)
    front_female = models.URLField(null=True, blank=True)
    front_shiny_female = models.URLField(null=True, blank=True)
    back_default = models.URLField(null=True, blank=True)
    back_shiny = models.URLField(null=True, blank=True)
    back_female = models.URLField(null=True, blank=True)
    back_shiny_female = models.URLField(null=True, blank=True)
    
class PokemonTypeDetails(models.Model):
     name = models.CharField(max_length=100)
     url = models.URLField()
     
class PokemonType(models.Model):
    slot = models.IntegerField()
    type = models.ForeignKey(PokemonTypeDetails, on_delete=models.CASCADE)

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    sprites = models.OneToOneField(PokemonSprites, on_delete=models.CASCADE, null=True, blank=True)
    types = models.ManyToManyField(PokemonType)

    def __str__(self):
        return self.name
class PokemonResponse(models.Model):
    count = models.IntegerField()
    next = models.URLField(null=True, blank=True)
    previous = models.URLField(null=True, blank=True)
    results = models.ManyToManyField(Pokemon)

class PokemonListViewModel(models.Model):
    pokemons = models.ManyToManyField(Pokemon)
    current_page = models.IntegerField()
    total_pages = models.IntegerField()
    