from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Spell

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello World</h1>")

class Postlist(generic.ListView):
    model = Spell