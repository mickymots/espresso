from django.shortcuts import render, redirect, reverse

# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.template import loader
# from .batch_form import BatchForm
from .forms.coffee_dry_form import CoffeeDryForm
from beans_intake.models import Intake, Location, Status, Batch, DryingBatch
from beans_intake.views import BATCH_STATUS_DRYING, BATCH_STATUS_FLOATED, BATCH_STATUS_GRADING, BATCH_STATUS_PARCHMENT, BATCH_STATUS_RESTING


def index(request):
    template = 'dry_coffee/index.html'
    context = {}
    query_results = Batch.objects.all().filter(status=Status.objects.get(pk=BATCH_STATUS_FLOATED))
    context['query_results'] = query_results
    return render(request, template, context=context)


def update_batch_status(request):
    
    if request.POST:
        batch_id = request.POST.get('batch_id')
        total_weight = request.POST.get('total_weight')
        batch = Batch.objects.get(pk=batch_id)

        batch.status = get_next_status(batch)

        if batch.status.id == BATCH_STATUS_DRYING:
            drying_batch = DryingBatch(
                dry_coffee_weight = total_weight,
                batch = batch
            )

            drying_batch.save()

        batch.save()

    context = {}
    query_results = Batch.objects.all()
    context['query_results'] = query_results
    return redirect('index')



def get_batch_details(request, batch_id):
    template = 'dry_coffee/batch_details.html'
    context = {}
    batch = Batch.objects.get(pk=batch_id)
    next_status =  get_next_status(batch)
    # Create new form
    context['batch'] = batch
    context['next_status'] = next_status
    context['form'] = CoffeeDryForm()
    return render(request, template, context=context)


def get_next_status(batch):
    status = batch.status
    if status.id == BATCH_STATUS_FLOATED:
        return Status.objects.get(pk=BATCH_STATUS_DRYING)
    elif status.id == BATCH_STATUS_DRYING:
        return Status.objects.get(pk=BATCH_STATUS_RESTING)
    elif status.id == BATCH_STATUS_RESTING:
        return Status.objects.get(pk=BATCH_STATUS_PARCHMENT)
    elif status.id == BATCH_STATUS_PARCHMENT:
        return Status.objects.get(pk=BATCH_STATUS_GRADING)
    else:
        return Status.objects.get(pk=BATCH_STATUS_FLOATED)
