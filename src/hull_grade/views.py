from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist 

from parchment_intake.models import ParchmentIntake
from green_beans_intake.models import GreenBeansIntake
from beans_intake.models import Intake, IntakeNotes, IntakeFiles, Location, Status,  DryingBatch, IntakeDetails, Inventory, InventoryFiles

from hull_grade.forms.hull_grade_intake_form import HullGradeIntakeForm
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



    return render(request, 'hull_grade/index.html', context=context)


def select_for_processing(request, batch_type, intake_id):
    template = 'hull_grade/hull_grade_intake.html'
    context = {}

    if request.POST:
        intake_form = HullGradeIntakeForm(request.POST)
       
        if intake_form.is_valid() :
            intake_form.save()

            return redirect('haul_grade_index')
        else:
            context['message'] = "Intake Failed."
            context['form'] = intake_form
           
    else:
        # Create new form
        context['form'] = HullGradeIntakeForm(initial={'batch_type': batch_type, 'intake_id': intake_id})
        

    return render(request, template, context)
