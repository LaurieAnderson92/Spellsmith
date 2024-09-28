from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse
from .models import Spell
from .forms import SpellForm


# Homepage 
# Uses Django Generic list view
class SpellList(generic.ListView):
    model = Spell
    template_name = "spellbook/spell_list.html"
    paginate_by = 12


# Detail Page, 
# It is passed the detail of a spell a displays it in a format that matches a DC20 spell template
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


# Create Page 
# A page that uses a Crispy Form to take a new spell and POST it to the database
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

            messages.add_message(
                request, messages.SUCCESS,
                'Your spell has been scribed into the communual spellbook!'
            )
            id = spell.id
            return HttpResponseRedirect(reverse('spell_detail', kwargs={'id': id}))
        else:
            messages.add_message(
                request, messages.Error,
                'Error creating a spell, Please create a bug report <a href="https://github.com/LaurieAnderson92/Spellsmith/issues/new?assignees=&labels=&projects=&template=bug_report.md&title="> here </a>'           
            )
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
    if request.user == spell.creator:
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
    messages.add_message(
                request, messages.WARNING,
                'You do not have permission to edit this spell'           
            )
    return HttpResponseRedirect(reverse('home'))

def spell_delete(request, id):
    """
    view to delete spells
    """
    spell = get_object_or_404(Spell, pk=id)

    if spell.creator == request.user:
        spell.delete()
        messages.add_message(
                request, messages.SUCCESS,
                'The spell has been successfully removed'           
            )
        return redirect('home')

    else:
        messages.add_message(
            request, messages.WARNING,
            'You do not have permission to delete this spell'            
            )
        return redirect('home')


def spell_about(request):
    """
    View for the About Page
    """
    return render(request, "spellbook/spell_about.html",)