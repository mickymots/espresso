from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

class OwnIntakeForm(forms.Form): 
    name = forms.CharField(label="name",
                           widget=forms.TextInput(attrs={'class': 'form-control'}) )

    lot_detail = forms.CharField(label="Select lot",
                                  widget=forms.TextInput(attrs={'class': 'form-control'}) )
   

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