from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Employee

from parchment_intake.models import ParchmentIntake
from django.core.exceptions import ValidationError


class ParchmentIntakeForm(forms.ModelForm): 

    proof_files = forms.FileField(label="Pictures of Batch", widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}))

    signed_delivery_slip = forms.FileField(label="Delivery Slip Pic", widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    delivery_person_pic = forms.FileField(label="Delivery Person Pic", widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    marker_placed = forms.BooleanField(label="Have you added ID number to batch?", 
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':"is_marker_placed"}))


    intake_note = forms.CharField(label="Intake Notes", 
                                  widget=forms.Textarea(attrs={'rows':'3', 'class': 'form-control', 'id':"intake_note"}))
    
    class Meta:
        model = ParchmentIntake
        exclude = ['created_date']
        labels = {
            "supervisor": "Supervisor Name",
            "supplier": "Supplier Name",
            "resting_period": "Enter number of weeks rested upon receipt",
             "sample_result" :"From sample batch record the % of Grade 1 ((grade 1 / total batch)*100)"             
        }
       



    #    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    
    # total_bags_count = models.IntegerField()
    # total_weight = models.IntegerField()
    # moisture_content = models.FloatField(default=0.00)    
    # sample_result = models.FloatField(default=0)    

    # resting_period = models.IntegerField()
    
    # supervisor_signature = JSignatureField(null=True, blank=True)
    
    # delivery_person_name = models.CharField(max_length=60, null=True, blank=True)
    # delivery_person_signature = JSignatureField(null=True, blank=True)

    # created_date = models.DateField(default=timezone.now)

    # signed_delivery_slip = models.FileField(upload_to=f'delivery-slips')
    # delivery_person_pic = models.FileField(upload_to=f'delivery-persons')
