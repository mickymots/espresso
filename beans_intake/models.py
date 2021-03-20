from django.db import models
# from jsignature.models import JSignatureModel
from jsignature.fields import JSignatureField
from datetime import datetime

class OwnIntake(models.Model):
    
    name = models.CharField(max_length=60)
    lot_detail = models.CharField(max_length=60)
    box_count = models.IntegerField()
    discarded_weight = models.IntegerField()
    refloated_weight = models.IntegerField()
    proof_file = models.CharField(max_length=500)
    signature = JSignatureField()
    


