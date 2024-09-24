from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views import generic
from django.urls import reverse
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

def spell_create(request):
    """
    A function that displays the spell_create
    """
    spell_form = SpellForm()

    if request.method == "POST":
        spell_form = SpellForm(data=request.POST)
        if spell_form.is_valid():
            spell = spell_form.save(commit=False)
            spell.creator = request.user
            spell.save()
            return HttpResponseRedirect('spell_list')

    return render(
        request,
        "spellbook/spell_create.html",
        {"spell_form": spell_form}
)

def spell_edit(request, id):
    """
    View to edit spells
    """
    spell = get_object_or_404(Spell, pk=id)
    if request.method == "POST":
        spell_form = SpellForm(data=request.POST, instance=spell)
        if spell_form.is_valid():
            spell.save()
            return HttpResponseRedirect(reverse('spell_detail', kwargs={'id': id}))
    spell_form = SpellForm(instance=spell)
    
    return render(
        request,
        "spellbook/spell_create.html",
        {"spell_form": spell_form}
    )

def spell_delete(request, id):
    """
    view to delete spells
    """
    spell = get_object_or_404(Spell, pk=id)

    if spell.creator == request.user:
        spell.delete()

    return redirect('home')
