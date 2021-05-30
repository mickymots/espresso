import os
from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse


# from .batch_form import BatchForm
from .forms.coffee_dry_form import CoffeeDryForm
from .forms.inventory_form import InvetoryForm

from beans_intake.models import Intake, Location, Status,  DryingBatch, IntakeDetails, Inventory, InventoryFiles
from beans_intake.views import BATCH_STATUS_DRYING, BATCH_STATUS_INTAKE, BATCH_STATUS_GRADING, BATCH_STATUS_PARCHMENT, BATCH_STATUS_RESTING


def index(request):
    template = 'dry_coffee/index.html'
    context = {}
    query_results = IntakeDetails.objects.all().order_by('intake').filter(status__in=Status.objects.filter(
        id__in=[BATCH_STATUS_INTAKE, BATCH_STATUS_DRYING])).filter(is_active_status=True)

    context['query_results'] = query_results
    context['header'] = 'List Of Intake Batches'
    context['is_actionable'] = True
    return render(request, template, context=context)



def processDrying(request, intake):
    is_marker_placed = request.POST.get('is_marker_placed')

    # intake = Intake.objects.get(pk=batch_id)
    intake_details = IntakeDetails.objects.get(
        intake=intake, is_active_status=True)

    intake_details.is_active_status = False

    if is_marker_placed == 'on':
        is_marker_placed = True
    else:
        is_marker_placed = False

    new_intake_details = IntakeDetails(intake=intake,
                                        status=get_next_status(
                                            intake_details),
                                        marker_placed=is_marker_placed
                                        )
    intake_details.save()
    new_intake_details.save()
    return 'DRYING'


def processResting(request, intake):
    
    inventory_form = InvetoryForm(request.POST, request.FILES)
    # inventory_form.intake = intake

    proof_files = request.FILES.getlist('proof_file')

    
    if inventory_form.is_valid():
        
        inventory = inventory_form.save(commit=False)
        inventory.intake = intake
        inventory.save()
        inventory = Inventory.objects.get(pk=inventory.id)

        for f in proof_files:
                proof_file = InventoryFiles(inventory= inventory, proof_file=f)
                proof_file.save()

        # update intake status to RESTING
        intake_details = IntakeDetails.objects.get(intake=intake, is_active_status=True)

        intake_details.is_active_status = False

        new_intake_details = IntakeDetails(intake=intake,
                                        status=get_next_status(intake_details),
                                        marker_placed=intake_details.marker_placed
                                        )

        intake_details.save()
        new_intake_details.save()

     
    return 'RESTING'


def update_batch_status(request):
    status='all'

    if request.POST:
        batch_id = request.POST.get('batch_id')
        intake = Intake.objects.get(pk=batch_id)
        intake_details = IntakeDetails.objects.get(
            is_active_status=True, intake=intake)

        next_status = get_next_status(intake_details)
        
        if next_status.status == 'DRYING':
            status = processDrying(request, intake)
        elif next_status.status == 'RESTING':
            status = processResting(request, intake)

    context = {}

    return redirect('get_batch_with_status', batch_status= status)


def get_batch_with_status(request, batch_status):
    template = 'dry_coffee/index.html'
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


def get_batch_details(request, batch_id):
    template = 'dry_coffee/batch_details.html'
    context = {}
    intake = Intake.objects.get(pk=batch_id)
    intake_details = IntakeDetails.objects.get(
        is_active_status=True, intake=intake)

    next_status = get_next_status(intake_details)

    # Create new form
    context['batch'] = intake_details
    context['next_status'] = next_status
    context['form'] = get_next_form(intake_details)
    return render(request, template, context=context)


def get_next_form(intake_details):
    status = intake_details.status
    if status.id == BATCH_STATUS_INTAKE:
        return CoffeeDryForm()
    elif status.id == BATCH_STATUS_DRYING:
        return InvetoryForm()
   

def get_next_status(intake_details):
    status = intake_details.status
    if status.id == BATCH_STATUS_INTAKE:
        return Status.objects.get(pk=BATCH_STATUS_DRYING)
    elif status.id == BATCH_STATUS_DRYING:
        return Status.objects.get(pk=BATCH_STATUS_RESTING)
    elif status.id == BATCH_STATUS_RESTING:
        return Status.objects.get(pk=BATCH_STATUS_PARCHMENT)
    elif status.id == BATCH_STATUS_PARCHMENT:
        return Status.objects.get(pk=BATCH_STATUS_GRADING)
    else:
        return Status.objects.get(pk=BATCH_STATUS_INTAKE)
