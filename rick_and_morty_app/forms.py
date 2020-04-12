from django import forms
# from .models import Character
from rick_and_morty_app.models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'lastEpisode', 'images']