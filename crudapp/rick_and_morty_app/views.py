from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from rick_and_morty_app.models import Character
# Create your views here.

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'lastEpisode', 'images']

def character_list(request, template_name='character/character_list.html'):
    characters = Character.objects.all()
    data = {}
    data ['object_list'] = characters
    return render(request, template_name, data)
