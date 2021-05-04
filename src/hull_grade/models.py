from django.db import models
from beans_intake.models import Employee
from django.utils import timezone

# Create your models here.
class HullGradeIntake(models.Model): 

    batch_type =  models.CharField(max_length=2)
    intake_id = models.IntegerField()
    supervisor_name = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    no_of_full_bags  = models.FloatField(default=0.00, null=True, blank=True)
    partial_weight = models.IntegerField(default=0, null=True, blank=True)
    
    created_date = models.DateField(default=timezone.now)

    def _str__(self):
        return str(self.id)