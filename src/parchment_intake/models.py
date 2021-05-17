from django.db import models
from beans_intake.models import Supplier, Employee
from django.utils import timezone
from jsignature.fields import JSignatureField


# Create your models here.
class ParchmentIntake(models.Model):    
    supervisor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    
    total_bags_count = models.IntegerField()
    total_weight = models.FloatField()
    moisture_content = models.FloatField(default=0.00)    
    sample_result = models.FloatField(default=0)    

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


class ParchmentIntakeFiles(models.Model):
    intake = models.ForeignKey(ParchmentIntake, on_delete=models.CASCADE)
    proof_file = models.FileField(upload_to=f'parchment-intake-files')

    def __str__(self):
        return str(self.proof_file)