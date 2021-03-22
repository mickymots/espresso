from django.db import models
# from jsignature.models import JSignatureModel
from jsignature.fields import JSignatureField
from datetime import datetime
from django.utils import timezone


class Location(models.Model):
    location =  models.CharField(max_length=60)

    def __str__(self):
        return self.location


class OwnIntake(models.Model):    
    name = models.CharField(max_length=60)
    lot_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    box_count = models.IntegerField()
    discarded_weight = models.IntegerField()
    refloated_weight = models.IntegerField()
    proof_file = models.CharField(max_length=500)
    signature = JSignatureField()
    created_date = models.DateField(default=timezone.now)
    

class Batch(models.Model):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    created_date = models.DateField(default=timezone.now)
    intake = models.ForeignKey(OwnIntake, on_delete=models.CASCADE, null=True)