from .models import Spell
from django import forms


class SpellForm(forms.ModelForm):
    class Meta:
        model = Spell
        fields = ['name','excerpt','school','ap_cost','mp_cost','range','duration',
                    'concentration','description','description','ap_enhancements','mp_enhancemnets']