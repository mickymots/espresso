from django.shortcuts import render, redirect, reverse

# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.template import loader
# from .batch_form import BatchForm
from .forms.coffee_dry_form import CoffeeDryForm
from beans_intake.models import Intake, Location, Status,  DryingBatch, IntakeDetails
from beans_intake.views import BATCH_STATUS_DRYING, BATCH_STATUS_INTAKE, BATCH_STATUS_GRADING, BATCH_STATUS_PARCHMENT, BATCH_STATUS_RESTING


def index(request):
    template = 'dry_coffee/index.html'
    context = {}
    query_results = IntakeDetails.objects.all().filter(status=Status.objects.get(pk=BATCH_STATUS_INTAKE)).filter(is_active_status=True)
    context['query_results'] = query_results
    return render(request, template, context=context)


def update_batch_status(request):
    
    if request.POST:
        batch_id = request.POST.get('batch_id')
        is_marker_placed = request.POST.get('is_marker_placed')

        intake = Intake.objects.get(pk=batch_id)
        intake_details = IntakeDetails.objects.get(intake=intake, is_active_status=True)
        
        intake_details.is_active_status = False

        if is_marker_placed == 'on':
            is_marker_placed = True
        else:
            is_marker_placed = False


        new_intake_details = IntakeDetails(intake = intake, 
                status = get_next_status(intake_details),
                marker_placed = is_marker_placed
            )

# intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
#     status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
#     marker_placed = models.BooleanField(default=True)
#     is_active_status = models.BooleanField(default=True)
#     created_date = models.DateField(default=timezone.now)

        intake_details.save()
        new_intake_details.save()

    context = {}
    # query_results = Intake.objects.all()
    # context['query_results'] = query_results
    return redirect('index')



def get_batch_details(request, batch_id):
    template = 'dry_coffee/batch_details.html'
    context = {}
    intake = Intake.objects.get(pk=batch_id)
    intake_details = IntakeDetails.objects.get(is_active_status=True, intake=intake)

    next_status = get_next_status(intake_details)

    # Create new form
    context['batch'] = intake_details
    context['next_status'] = next_status
    context['form'] = CoffeeDryForm()
    return render(request, template, context=context)


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
