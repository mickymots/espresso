from django.contrib import admin

# Register your models here.


from .models import GreenBeansIntake, GreenBeansIntakeFiles
admin.site.register(GreenBeansIntake)
admin.site.register(GreenBeansIntakeFiles)
