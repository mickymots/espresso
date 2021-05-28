from django.contrib import admin

# Register your models here.

from .models import ParchmentIntake, ParchmentIntakeFiles
admin.site.register(ParchmentIntake)
admin.site.register(ParchmentIntakeFiles)
