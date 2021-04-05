from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Intake, Supplier, Employee

class SupplierIntakeForm(forms.ModelForm): 

    supervisor_name = forms.ModelChoiceField(label="Supervisor Name",
                                 queryset=Employee.objects.all().filter(is_supervisor=True), widget=forms.Select(attrs={'class':'form-control'}))

    supplier_name = forms.ModelChoiceField(label="Supplier Name",
                                queryset=Supplier.objects.all().filter(), widget=forms.Select(attrs={'class':'form-control'}))

    total_box_count= forms.IntegerField(label="Number of Boxes",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  min_value = 0)

    passed_float_box_count = forms.IntegerField(label="Number of Passed Float Boxes", required = False,
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  min_value = 0)

    is_floated = forms.BooleanField(label="Floated?", required = False,
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':"is_floated"}))

    proof_file = forms.FileField(label="Pictures of Batch", widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}))

    supervisor_signature = JSignatureField(label="Supervisor Signature")

    representative_name = forms.CharField(label="Seller Rep. Name",
                           widget=forms.TextInput(attrs={'class': 'form-control'}) )

    representative_signature = JSignatureField(label="Seller Rep. Signature")

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
                "supervisor_name", "supplier_name", "total_box_count", "passed_float_box_count", "is_floated",
                "proof_file", "supervisor_signature", "representative_name", "representative_signature"
        ]