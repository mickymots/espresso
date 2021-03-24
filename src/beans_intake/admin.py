from django.contrib import admin

from .models import Intake, Location, Batch, Refloat
admin.site.register(Batch)
admin.site.register(Intake)
admin.site.register(Location)
admin.site.register(Refloat)
