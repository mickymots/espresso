from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Intake, Employee

class OwnIntakeForm(forms.ModelForm): 

    # supervisor_name = forms.CharField(label="Supervisor Name",
    #                        widget=forms.TextInput(attrs={'class': 'form-control'}) )
    supervisor_name = forms.ModelChoiceField(label="Supervisor Name",
                                 queryset=Employee.objects.all().filter(is_supervisor=True), widget=forms.Select(attrs={'class':'form-control'}))

    lot_location = forms.ModelChoiceField(label="Select lot location",
                                 queryset=Location.objects.all() , widget=forms.Select(attrs={'class':'form-control'}))

    total_box_count= forms.IntegerField(label="Number of Boxes",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  min_value = 0)
    passed_float_box_count = forms.IntegerField(label="Number of Passed Float Boxes",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  min_value = 0)

    is_floated = forms.BooleanField(label="Floated?", required = False,
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':"is_floated"}))
    # total_weight = forms.IntegerField(label="Total Weight",
    #                                       widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #                                       min_value = 0) 


    # discarded_weight = forms.IntegerField(label="Weight Discarded",
    #                                       widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #                                       min_value = 0) 

    # refloated_weight = forms.IntegerField(label="Weight Refloated",
    #                                       widget=forms.NumberInput(attrs={'class': 'form-control'}),
    #                                       min_value = 0) 

    

    supervisor_signature = JSignatureField(label="Supervisor Signature")
    
    proof_file = forms.FileField(label="Picture of Batch", required = False, 
                                 widget=forms.FileInput(attrs={'class': 'form-control'})) 

    class Meta:
        model = Intake
        fields = [
                "supervisor_name", "lot_location", "total_box_count", "passed_float_box_count" , "is_floated", "supervisor_signature","proof_file",
                # "total_weight","discarded_weight", "refloated_weight",  
        ]