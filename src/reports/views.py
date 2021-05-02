from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist 


from beans_intake.models import Intake, IntakeNotes, IntakeFiles, Location, Status,  DryingBatch, IntakeDetails, Inventory, InventoryFiles
from beans_intake.views import BATCH_STATUS_DRYING, BATCH_STATUS_INTAKE, BATCH_STATUS_GRADING, BATCH_STATUS_PARCHMENT, BATCH_STATUS_RESTING

intake_details_template = 'intake_details.html/'


def index(request):

    context = {}
    # query_results = ParchmentIntake.objects.all()
    # context['query_results'] =  query_results
    return render(request, 'index.html', context=context)



# def get_batch_with_status():
#     template = 'dry_coffee/index.html'
#     context = {}
#     query_results = IntakeDetails.objects.all().filter(status__in=Status.objects.filter(
#         id__in=[BATCH_STATUS_INTAKE, BATCH_STATUS_DRYING])).filter(is_active_status=True)

#     context['query_results'] = query_results
#     context['header'] = 'List Of Intake Batches'
#     context['is_actionable'] = True
#     return render(request, template, context=context)



def get_batch_with_status(request, batch_status):
    template = 'batch_list.html'
    context = {}
    query_results = IntakeDetails.objects.all().filter(is_active_status=True)
    
    status = None
            
    if batch_status == 'DRYING':
        status = Status.objects.get(pk=BATCH_STATUS_DRYING)

    elif batch_status == 'RESTING':
        status = Status.objects.get(pk=BATCH_STATUS_RESTING)

    
    if status:
        query_results = query_results.filter(status=status)

    context['query_results'] = query_results
    context['header'] = f'List Of {batch_status} Batches'
    context['is_actionable'] = False
    return render(request, template, context=context)


# Show Intake details
def get_intake_details(request, batch_status, intake_id):
    try:
        intake = Intake.objects.get(pk=intake_id)
        intake_details = IntakeDetails.objects.get(
            is_active_status=True, intake=intake)
        try:
            intake_notes = IntakeNotes.objects.get(intake=intake)
            
        except ObjectDoesNotExist as e:
            print(e)
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
    except ObjectDoesNotExist:
        intake_details = None
        intake_notes  = None
        uploaded_files = None

    except Intake.DoesNotExist:
        raise Http404("Intake does not exist")
    return render(request, intake_details_template, {'intake': intake, 'intake_details': intake_details, 
        'intake_notes':intake_notes, 'uploaded_files': uploaded_files, 'inventory': inventory,'inventory_files': inventory_files, 'batch_status':batch_status})
