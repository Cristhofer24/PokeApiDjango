from django import forms
from django.core.exceptions import ValidationError
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ["name", "weight", "height", "sprites"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "weight": forms.NumberInput(attrs={"class": "form-control"}),
            "height": forms.NumberInput(attrs={"class": "form-control"}),
            "sprites": forms.URLInput(attrs={"class": "form-control"}),
        }

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
