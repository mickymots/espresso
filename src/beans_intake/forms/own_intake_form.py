from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Intake, Employee

class OwnIntakeForm(forms.ModelForm): 
    
    supervisor_name = forms.ModelChoiceField(label="Supervisor Name",
                                 queryset=Employee.objects.all().filter(is_supervisor=True), widget=forms.Select(attrs={'class':'form-control'}))

    lot_location = forms.ModelChoiceField(label="Select lot location",
                                 queryset=Location.objects.all() , widget=forms.Select(attrs={'class':'form-control'}))

    total_box_count= forms.IntegerField(label="Number of Boxes",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  min_value = 0)
    passed_float_box_count = forms.IntegerField(label="Number of Passed Float Boxes", required = False,
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  min_value = 0)

    is_floated = forms.BooleanField(label="Floated?", required = False,
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':"is_floated"}))

    supervisor_signature = JSignatureField(label="Supervisor Signature")
    
    proof_file = forms.FileField(label="Picture of Batch", required = False, 
                                 widget=forms.FileInput(attrs={'class': 'form-control'})) 

    class Meta:
        model = Intake
        fields = [
                "supervisor_name", "lot_location", "total_box_count", "passed_float_box_count" , "is_floated", "supervisor_signature","proof_file",
        ]