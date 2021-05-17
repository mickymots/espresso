from django.db import models
from beans_intake.models import Employee
from django.utils import timezone

# Create your models here.
class HullGradeIntake(models.Model): 
    PARTIAL_SELECTION = (
        (0,  'Partial Bag not picked'),
        (1, 'Partial Bag picked'),
    )

    batch_type =  models.CharField(max_length=2)
    intake_id = models.IntegerField()
    supervisor_name = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    no_of_full_bags  = models.FloatField(default=0.00, null=True, blank=True)
    partial_weight = models.IntegerField(default=0, null=True, blank=True, max_length=1, choices=PARTIAL_SELECTION)
    hulled_graded = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)

    def _str__(self):
        return str(self.id)


# Create your models here.
class GradedBeans(models.Model): 
    
    hull_grade_intake = models.ForeignKey(HullGradeIntake, on_delete=models.SET_NULL, null=True)
    
    supervisor_name = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    
    kgs_grade_1  = models.FloatField(default=0.00, null=True, blank=True)
    
    kgs_grade_2  = models.FloatField(default=0.00, null=True, blank=True)

    kgs_grade_3  = models.FloatField(default=0.00, null=True, blank=True)

    kgs_grade_pb  = models.FloatField(default=0.00, null=True, blank=True)

    kgs_grade_fines  = models.FloatField(default=0.00, null=True, blank=True)

    kgs_grade_non_exp  = models.FloatField(default=0.00, null=True, blank=True)

    kgs_grade_trash  = models.FloatField(default=0.00, null=True, blank=True)

    created_date = models.DateField(default=timezone.now)

    def _str__(self):
        return str(self.id)