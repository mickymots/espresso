from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Intake

class OwnIntakeForm(forms.ModelForm): 

    supervisor_name = forms.CharField(label="Supervisor Name",
                           widget=forms.TextInput(attrs={'class': 'form-control'}) )

    lot_location = forms.ModelChoiceField(label="Select lot location",
                                 queryset=Location.objects.all() , widget=forms.Select(attrs={'class':'form-control'}))

    box_count= forms.IntegerField(label="Number of Boxes",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  min_value = 0)

    total_weight = forms.IntegerField(label="Total Weight",
                                          widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                          min_value = 0) 


    discarded_weight = forms.IntegerField(label="Weight Discarded",
                                          widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                          min_value = 0) 

    refloated_weight = forms.IntegerField(label="Weight Refloated",
                                          widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                          min_value = 0) 

    proof_file = forms.FileField(label="Picture of Batch",
                                 widget=forms.FileInput(attrs={'class': 'form-control'})) 

    supervisor_signature = JSignatureField(label="Supervisor Signature")

    class Meta:
        model = Intake
        fields = [
                "supervisor_name", "lot_location", "box_count", "total_weight","discarded_weight", 
                "refloated_weight", "proof_file", "supervisor_signature"
        ]