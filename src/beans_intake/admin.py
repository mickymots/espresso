from django.contrib import admin

from .models import OwnIntake, Location, Batch
admin.site.register(Batch)
admin.site.register(OwnIntake)
admin.site.register(Location)