from django.db import models
# from jsignature.models import JSignatureModel
from jsignature.fields import JSignatureField
from datetime import datetime
from django.utils import timezone


class Location(models.Model):
    location =  models.CharField(max_length=60)

    def __str__(self):
        return self.location

class Supplier(models.Model):
    name = models.CharField(max_length=60)
    address = models.TextField(max_length=120, null=True)
    phone = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=60, null=True)
    is_active = models.BooleanField(default=True)
    lot_location = models.CharField(max_length=60, null=True)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Status(models.Model):
    status = models.CharField(max_length=20)
    status_description = models.CharField(max_length=250)

    def __str__(self):
        return self.status  


class Employee(models.Model):
    name = models.CharField(max_length=60)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    is_supervisor = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Intake(models.Model):    
    supervisor_name = models.CharField(max_length=60)
    lot_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    is_floated = models.BooleanField(default=False, blank=True, null=True)
    total_box_count = models.IntegerField()
    passed_float_box_count = models.IntegerField(default=0, null=True,blank=True )
    
    supervisor_signature = JSignatureField(null=True, blank=True)
    supplier_name = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    representative_name = models.CharField(max_length=60, null=True, blank=True)
    representative_signature = JSignatureField(null=True, blank=True)
    is_external = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)


class IntakeFiles(models.Model):
    intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    proof_file = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return str(self.proof_file)


class IntakeNotes(models.Model):
    intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    notes = models.TextField(max_length=500)


class IntakeDetails(models.Model):
    intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    marker_placed = models.BooleanField(default=True)
    is_active_status = models.BooleanField(default=True)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.status)


class Inventory(models.Model):
    intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    supervisor_name = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    full_bags = models.IntegerField(default=0, null=True, blank=True)
    partial_bag_weight = models.IntegerField(default=0, null=True, blank=True)
    marker_placed = models.BooleanField(default=True)
    created_date = models.DateField(default=timezone.now)


class InventoryFiles(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    proof_file = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return str(self.proof_file)


class Refloat(models.Model):
    intake = models.ForeignKey(Intake, on_delete=models.SET_NULL, null=True)
    refloat_weight = models.IntegerField()
    floated = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)


class DryingBatch(models.Model):
    dry_coffee_weight = models.IntegerField()
    created_date = models.DateField(default=timezone.now)
    batch = models.CharField(max_length=60, null=True, blank=True)







