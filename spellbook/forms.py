from .models import Spell
from django import forms


class SpellForm(forms.ModelForm):
    class Meta:
        model = Spell
        fields = ['name', 'excerpt', 'school', 'ap_cost', 'mp_cost', 'range',
                  'duration', 'concentration', 'description', 'description',
                  'ap_enhancements', 'mp_enhancements']

        # This adds form validation feedback on submit
        widgets = {
            'ap_cost': forms.NumberInput(attrs={'min':1, 'max':4}),
            'mp_cost': forms.NumberInput(attrs={'min':0, 'max':10})
        }
