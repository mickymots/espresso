from django.db import models
from beans_intake.models import Supplier, Employee
from django.utils import timezone
from jsignature.fields import JSignatureField


# Create your models here.
class GreenBeansIntake(models.Model):
    INTAKE_TYPE = (
        ('S',  'Hulled, graded and sorted'),
        ('N', 'Hulled, graded NOT sorted'),
    )

    supervisor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    
    moisture_content = models.FloatField(default=0.00)  
    intake_type = models.CharField(max_length=1, choices=INTAKE_TYPE)

    grade1_weight = models.FloatField(default=0.00) 
    grade2_weight = models.FloatField(default=0.00) 
    grade3_weight = models.FloatField(default=0.00) 
    grade_pb_weight = models.FloatField(default=0.00) 
    grade_fines_weight = models.FloatField(default=0.00) 

    resting_period = models.IntegerField()
    
    supervisor_signature = JSignatureField(null=True, blank=True)
    
    delivery_person_name = models.CharField(max_length=60, null=True, blank=True)
    delivery_person_signature = JSignatureField(null=True, blank=True)

    created_date = models.DateField(default=timezone.now)

    signed_delivery_slip = models.FileField(upload_to=f'delivery-slips')
    delivery_person_pic = models.FileField(upload_to=f'delivery-persons')

    marker_placed = models.BooleanField(default=False)
    intake_note = models.TextField(null=True, blank=True)

    def _str__(self):
        return str(self.id)


class GreenBeansIntakeFiles(models.Model):
    intake = models.ForeignKey(GreenBeansIntake, on_delete=models.CASCADE)
    proof_file = models.FileField(upload_to=f'green-beans-intake-files')

    def __str__(self):
        return str(self.proof_file)