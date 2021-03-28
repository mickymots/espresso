from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Batch


class CoffeeDryForm(forms.ModelForm):

    total_weight = forms.IntegerField(label="Total Weight",
                                      widget=forms.NumberInput(
                                          attrs={'class': 'form-control'}),
                                      min_value=0)

    class Meta:
        model = Batch
        fields = [
            "total_weight"
        ]
