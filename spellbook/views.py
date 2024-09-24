from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Spell
from .forms import SpellForm

# Create your views here.

class SpellList(generic.ListView):
    model = Spell
    template_name = "spellbook/spell_list.html"

def spell_detail(request, id):
    """
    Display an individual spell.

    **Context**

    ``spell``
        An instance of a spell model.

    **Template:**

    :template:`spellbook/spell_detail.html`
    """

    queryset = Spell.objects.all()
    spell = get_object_or_404(queryset, id=id)

    return render(
        request,
        "spellbook/spell_detail.html",
        {"spell": spell},
    )

def spell_create (request):
    """
    A function that displays the spell_create
    """
    spell_form = SpellForm()

    return render(
        request,
        "spellbook/spell_create.html"
)