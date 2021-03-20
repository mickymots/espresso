from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, OwnIntake

class OwnIntakeForm(forms.ModelForm): 

    name = forms.CharField(label="name",
                           widget=forms.TextInput(attrs={'class': 'form-control'}) )

    lot_location = forms.ModelChoiceField(label="Select lot",
                                 queryset=Location.objects.all() , widget=forms.Select(attrs={'class':'form-control'}))

    box_count= forms.IntegerField(label="Number of Boxes",
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

    
    signature = JSignatureField(label="Signature")

    class Meta:
        model = OwnIntake
        fields = [
                "name", "lot_location", "box_count", "discarded_weight", "refloated_weight", "proof_file", "signature"
        ]