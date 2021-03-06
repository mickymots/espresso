from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget



class RefloatIntakeForm(forms.ModelForm):

    total_weight = forms.IntegerField(label="Total Weight",
                                      widget=forms.NumberInput(
                                          attrs={'class': 'form-control'}),
                                      min_value=0)


