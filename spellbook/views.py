from django.shortcuts import render
from django.views import generic
from .models import Spell

# Create your views here.

class SpellList(generic.ListView):
    model = Spell
    template_name = "spellbook/spell_list.html"