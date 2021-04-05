from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Intake, Employee
from django.core.exceptions import ValidationError

# Template files
own_intake_template = 'beans_intake/own_intake.html'
intake_details_template = 'beans_intake/intake_details.html/'


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
    
                                 
    proof_file = forms.FileField(label="Pictures of Batch", widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}))


    def clean(self):
        cleaned_data = super().clean()
        total_box_count = cleaned_data.get("total_box_count")
        passed_float_box_count = cleaned_data.get("passed_float_box_count")

        if total_box_count and passed_float_box_count:
            # Only do something if both fields are valid so far.
            if passed_float_box_count >  total_box_count:
                msg = "Passed float count can not be more than total box count"
                self.add_error('passed_float_box_count', msg)
               

    class Meta:
        model = Intake
        fields = [
                "supervisor_name", "lot_location", "total_box_count", "passed_float_box_count" , "is_floated", "supervisor_signature","proof_file",
        ]