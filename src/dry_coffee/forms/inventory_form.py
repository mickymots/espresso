from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Inventory, Employee, Intake


class InvetoryForm(forms.ModelForm):

    supervisor_name = forms.ModelChoiceField(label="Supervisor Name",
                                 queryset=Employee.objects.all().filter(is_supervisor=True), widget=forms.Select(attrs={'class':'form-control'}))

    full_bags_count= forms.IntegerField(label="Number of 25Kg Bags",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  min_value = 0)

    partial_bag_weight = forms.FloatField(label="Partial bag weight (Kgs)", required = False,
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  min_value = 0.0, max_value=24.99)

    moisture_content = forms.FloatField(label="Moisture Content", required = True,
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  min_value = 0)

    is_marker_placed = forms.BooleanField(label="Have placed marker at batch?", 
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':"is_marker_placed"}))


    proof_file = forms.FileField(label="Pictures of Batch", widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}))


    class Meta:
        model = Inventory
        exclude = ('intake',)
        fields = [ "supervisor_name", "full_bags_count", "partial_bag_weight", "moisture_content", "is_marker_placed", "proof_file" ]
