from django import forms
from django.core.exceptions import ValidationError
from .models import Pokemon, PokemonSprites

class PokemonForm(forms.ModelForm):
    # Agregar campos para las URLs de los sprites
    front_default = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Front Default URL"})
    )
    front_shiny = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Front Shiny URL"})
    )

    class Meta:
        model = Pokemon
        fields = ["name", "weight", "height"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "weight": forms.NumberInput(attrs={"class": "form-control"}),
            "height": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres")
        return name

    def clean_weight(self):
        weight = self.cleaned_data["weight"]
        if weight <= 0:
            raise forms.ValidationError("El peso debe ser mayor que 0")
        return weight

    def clean_height(self):
        height = self.cleaned_data["height"]
        if height <= 0:
            raise forms.ValidationError("La altura debe ser mayor que 0")
        return height

    def save(self, commit=True):
        # Guardar el Pokémon
        pokemon = super().save(commit=False)

        # Obtener los valores de las URLs de los sprites
        front_default = self.cleaned_data.get("front_default")
        front_shiny = self.cleaned_data.get("front_shiny")

        # Crear o actualizar el objeto PokemonSprites
        if front_default or front_shiny:
            sprites, created = PokemonSprites.objects.get_or_create(
                front_default=front_default,
                front_shiny=front_shiny,
                defaults={
                    "front_default": front_default,
                    "front_shiny": front_shiny,
                }
            )
            pokemon.sprites = sprites

        if commit:
            pokemon.save()
            self.save_m2m()  # Guardar relaciones ManyToMany si existen

        return pokemon
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres")
        return name

    def clean_weight(self):
        weight = self.cleaned_data["weight"]
        if weight <= 0:
            raise ValidationError("El peso debe ser mayor que 0")
        return weight

    def clean_height(self):
        height = self.cleaned_data["height"]
        if height <= 0:
            raise ValidationError("La altura debe ser mayor que 0")
        return height
