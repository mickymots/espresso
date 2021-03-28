from django.db import models
# from jsignature.models import JSignatureModel
from jsignature.fields import JSignatureField
from datetime import datetime
from django.utils import timezone


class Location(models.Model):
    location =  models.CharField(max_length=60)

    def __str__(self):
        return self.location


class Intake(models.Model):    
    supervisor_name = models.CharField(max_length=60)
    lot_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    box_count = models.IntegerField()
    total_weight = models.IntegerField()
    discarded_weight = models.IntegerField()
    refloated_weight = models.IntegerField()
    proof_file = models.CharField(max_length=500)
    supervisor_signature = JSignatureField()
    representative_name = models.CharField(max_length=60, null=True, blank=True)
    representative_signature = JSignatureField(null=True, blank=True)
    is_external = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)

class Status(models.Model):
    status = models.CharField(max_length=20)
    status_description = models.CharField(max_length=250)
    def __str__(self):
        return self.status   

class Batch(models.Model):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    batch_weight = models.IntegerField()
    
    is_second_float = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)
    intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)


class Refloat(models.Model):
    intake = models.ForeignKey(Intake, on_delete=models.SET_NULL, null=True)
    refloat_weight = models.IntegerField()
    floated = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)

class DryingBatch(models.Model):
    dry_coffee_weight = models.IntegerField()
    created_date = models.DateField(default=timezone.now)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True)


class Sorter(models.Model):
    name = models.CharField(max_length=60)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(default=timezone.now)