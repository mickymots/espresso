from django.contrib import admin

from .models import Intake, Location,  Status, Refloat, Supplier, Employee
admin.site.register(Intake)
admin.site.register(Location)
admin.site.register(Refloat)
admin.site.register(Status)
admin.site.register(Supplier)
admin.site.register(Employee)
