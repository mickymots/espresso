from django import forms 

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from beans_intake.models import Location, Employee

from hull_grade.models import HullGradeIntake
from django.core.exceptions import ValidationError

from hull_grade.models import GradedBeans

class HullGradeResultForm(forms.ModelForm): 

    class Meta:
        model = GradedBeans
        exclude = ['created_date']
        labels = {}



