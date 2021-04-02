from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Intake


class CoffeeDryForm(forms.ModelForm):

    is_marker_placed = forms.BooleanField(label="Have placed marker at batch?", 
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':"is_marker_placed"}))
    class Meta:
        model = Intake
        fields = [
            "is_marker_placed"
        ]
