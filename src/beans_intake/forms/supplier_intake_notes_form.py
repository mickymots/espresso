from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import IntakeNotes

class SupplierIntakeNotesForm(forms.ModelForm): 

    notes = forms.CharField(label="Intake Notes", required = False,
                            widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = IntakeNotes
        fields = [ "notes" ]