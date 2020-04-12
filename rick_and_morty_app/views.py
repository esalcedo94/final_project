# from django.shortcuts import render, redirect, get_object_or_404
from .forms import CharacterForm
from rick_and_morty_app.models import Character

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy # new
# Create your views here.

class HomePageView(ListView):
    model = Character
    template_name = 'character_list.html'

class CreateCharacterView(CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'character_form.html'
    success_url = reverse_lazy('character_list')

class CharacterDetailView(DetailView):
    model = Character
    template_name = 'character_details.html'

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'lastEpisode']
    template_name = 'character_update.html'
    success_url = reverse_lazy('character_list')

class DeleteCharacter(DeleteView):
    model = Character
    template_name = 'character_delete.html'
    success_url = reverse_lazy('character_list')
