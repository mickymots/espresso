from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Intake, Batch


class BatchForm(forms.ModelForm):

    id = forms.CharField(label="Batch ID",
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.CharField(label="Status", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:

        model = Batch
        fields=["id", "status"]
