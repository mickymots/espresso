from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Employee

from hull_grade.models import HullGradeIntake
from django.core.exceptions import ValidationError

from hull_grade.models import HullGradeIntake
from beans_intake.models import Inventory
from parchment_intake.models import ParchmentIntake

 
from functools import reduce

class HullGradeIntakeForm(forms.ModelForm): 

    def clean(self):
        
        cleaned_data = super().clean()
        no_of_full_bags = cleaned_data.get("no_of_full_bags")
        
        batch_type = cleaned_data.get("batch_type")
        intake_id = cleaned_data.get("intake_id")

        total_bags = getIntakeBagsCount(batch_type, intake_id)

        (total_hulled_graded_bags,partial_intake_exists) = getHullGradeIntakes(intake_id)

        if no_of_full_bags == 0.0:
            partial_weight = cleaned_data.get("partial_weight")
            
            if partial_weight == 0:
                msg = "Select a full bag or partial weight to for intake"
                self.add_error('partial_weight', msg)
                
            elif partial_intake_exists:
                msg = "Partial weight already hulled and graded"
            
                self.add_error('partial_weight', msg)

        elif total_hulled_graded_bags + no_of_full_bags >  total_bags:
            msg = f" {total_bags - total_hulled_graded_bags} available for hulling / grading. Please correct bag count"
            self.add_error('no_of_full_bags', msg)

    class Meta:
        model = HullGradeIntake
        exclude = ['created_date']
        labels = {}



def getIntakeBagsCount(batch_type, intake_id):
    if batch_type == 'CH':
        intake =  Inventory.objects.get(id=intake_id)
        return intake.full_bags

    elif batch_type == 'PH':
        intake = ParchmentIntake.objects.get(id=intake_id)
        return intake.total_bags_count


def getHullGradeIntakes(intake_id):
    partial_intake_exists = False
    hulled_graded_intakes = HullGradeIntake.objects.filter(intake_id=intake_id)
    total_bags = 0.0

    for intake in hulled_graded_intakes:
        total_bags += intake.no_of_full_bags
        if intake.partial_weight > 0:
            partial_intake_exists = True
    return (total_bags,partial_intake_exists)