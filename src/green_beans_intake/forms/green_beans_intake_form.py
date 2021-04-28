from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Employee

from green_beans_intake.models import GreenBeansIntake
from django.core.exceptions import ValidationError


class GreenBeansIntakeForm(forms.ModelForm): 

    proof_files = forms.FileField(label="Pictures of Batch", widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}))

    signed_delivery_slip = forms.FileField(label="Delivery Slip Pic", widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    delivery_person_pic = forms.FileField(label="Delivery Person Pic", widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    marker_placed = forms.BooleanField(label="Have you added ID number to batch?", 
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':"is_marker_placed"}))


    intake_note = forms.CharField(label="Intake Notes", 
                                  widget=forms.Textarea(attrs={'rows':'3', 'class': 'form-control', 'id':"intake_note"}))
    
    class Meta:
        model = GreenBeansIntake
        exclude = ['created_date']
        labels = {
            "supervisor": "Supervisor Name",
            "supplier": "Supplier Name",
            "resting_period": "Enter number of weeks rested upon receipt"
        }
       