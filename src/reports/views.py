from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist 

from beans_intake.models import Intake, IntakeNotes, IntakeFiles, Location, Status,  DryingBatch, IntakeDetails, Inventory, InventoryFiles
from beans_intake.views import BATCH_STATUS_DRYING, BATCH_STATUS_INTAKE, BATCH_STATUS_GRADING, BATCH_STATUS_PARCHMENT, BATCH_STATUS_RESTING
from hull_grade.models import GradedBeans
from parchment_intake.models import ParchmentIntake, ParchmentIntakeFiles

intake_details_template = 'intake_details.html/'
parchment_intake_details_template = 'parchment_intake_details.html'





def index(request):
    context = {}
    return render(request, 'index.html', context=context)



def get_batch_with_status(request, batch_status):
    template = 'batch_list.html'
    context = {}
    query_results = IntakeDetails.objects.all().filter(is_active_status=True)
    
    status = None
            
    if batch_status == 'DRYING':
        status = Status.objects.get(pk=BATCH_STATUS_DRYING)

    elif batch_status == 'RESTING':
        status = Status.objects.get(pk=BATCH_STATUS_RESTING)
    elif 'GRADED' in batch_status:
        query_results = GradedBeans.objects.all()
        template = 'hulled_graded_report.html'
    
    if status:
        query_results = query_results.filter(status=status)

    context['query_results'] = query_results
    context['header'] = f'List Of {batch_status} Batches'
    context['batch_status'] = batch_status
    context['is_actionable'] = False
    return render(request, template, context=context)


# Show Intake details
def get_intake_details(request, batch_status, intake_id):
    try:
        
        if batch_status == 'PH_GRADED':
            intake = ParchmentIntake.objects.get(pk=intake_id)
            uploaded_files = ParchmentIntakeFiles.objects.all().filter(intake=intake)
            return render(request, parchment_intake_details_template, {'intake': intake, 'uploaded_files': uploaded_files, 'batch_status':batch_status})

        elif batch_status == 'GRADED':
            inventory = Inventory.objects.get(pk=intake_id)
            intake = inventory.intake
        else:
            intake = Intake.objects.get(pk=intake_id)
        
        intake_details, intake_notes, uploaded_files, inventory, inventory_files = get_additonal_details(intake, batch_status)
    except ObjectDoesNotExist:
        intake_details = None
        intake_notes  = None
        uploaded_files = None

    except Intake.DoesNotExist:
        raise Http404("Intake does not exist")
    return render(request, intake_details_template, {'intake': intake, 'intake_details': intake_details, 
        'intake_notes':intake_notes, 'uploaded_files': uploaded_files, 'inventory': inventory,'inventory_files': inventory_files, 'batch_status':batch_status})


def get_additonal_details(intake, batch_status):
    if batch_status != 'PH_GRADED':

        intake_details = IntakeDetails.objects.get(
            is_active_status=True, intake=intake)
        try:
            intake_notes = IntakeNotes.objects.get(intake=intake)
            
        except ObjectDoesNotExist as e:
            intake_notes = None
        try:
            uploaded_files = IntakeFiles.objects.all().filter(intake=intake)
        except ObjectDoesNotExist as e:
            uploaded_files = None
        try:
            inventory = Inventory.objects.get(intake=intake)
            inventory_files = InventoryFiles.objects.all().filter(inventory=inventory)
        except ObjectDoesNotExist as e:
            inventory = None
            inventory_files =None
    
        return intake_details, intake_notes, uploaded_files, inventory, inventory_files