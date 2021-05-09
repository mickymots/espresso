from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Employee

from green_beans_intake.models import GreenBeansIntake
from django.core.exceptions import ValidationError


class GreenBeansIntakeUpdateForm(forms.ModelForm): 
    intake_id = forms.CharField(max_length=20)
    class Meta:
        model = GreenBeansIntake
        exclude = ['created_date', 'moisture_content','intake_type','supervisor', 'supplier', 'proof_files', 'signed_delivery_slip', 'delivery_person_pic']
        labels = {
            "supervisor": "Supervisor Name",
            "supplier": "Supplier Name",
            "grade1_weight": "Grade1 Weight(kgs)",
            "grade2_weight": "Grade2 Weight(kgs)",
            "grade3_weight": "Grade3 Weight(kgs)",
            "grade_pb_weight": "Grade PB Weight(kgs)",
            "grade_fines_weight": "Grade Fines Weight(kgs)",
            "resting_period": "Enter number of weeks rested upon receipt"
        }
       