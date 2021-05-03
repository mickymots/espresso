from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist 

from parchment_intake.models import ParchmentIntake, ParchmentIntakeFiles
from green_beans_intake.models import GreenBeansIntake, GreenBeansIntakeFiles
from beans_intake.models import Intake, IntakeNotes, IntakeFiles, Location, Status,  DryingBatch, IntakeDetails, Inventory, InventoryFiles
from beans_intake.views import BATCH_STATUS_DRYING, BATCH_STATUS_INTAKE, BATCH_STATUS_GRADING, BATCH_STATUS_PARCHMENT, BATCH_STATUS_RESTING

intake_details_template = 'intake_details.html/'

# Index page
def index(request):
    context = {}

    parchments = ParchmentIntake.objects.all()
    green_beans = GreenBeansIntake.objects.all()
    inventory = Inventory.objects.all()

    context['parchments'] = parchments
    context['green_beans'] = green_beans
    context['inventory'] = inventory



    return render(request, 'haul_grade/index.html', context=context)
