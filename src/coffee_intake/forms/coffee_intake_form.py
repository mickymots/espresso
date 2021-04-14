from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Employee

from coffee_intake.models import CoffeeIntake
from django.core.exceptions import ValidationError

# Template files
coffee_intake_template = 'coffee_intake/coffee_intake.html'
coffee_intake_details_template = 'coffee_intake/coffee_intake_details.html'


class CoffeeIntakeForm(forms.ModelForm): 

    proof_files = forms.FileField(label="Pictures of Batch", widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}))

    class Meta:
        model = CoffeeIntake
        exclude = ['created_date']
       