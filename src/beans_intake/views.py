from django.shortcuts import render, redirect
from django.db import transaction
from django.http import HttpResponse, Http404
from django.template import loader
from jsignature.utils import draw_signature
from .forms.own_intake_form import OwnIntakeForm
from .models import Intake, Location, Status, Batch


# Template files
own_intake_template = 'beans_intake/own_intake.html'
intake_details_template = 'beans_intake/intake_details.html/'

BATCH_STATUS_FLOATED = 3000000
BATCH_STATUS_DRYING = 3000001
BATCH_STATUS_RESTING = 3000002
BATCH_STATUS_PARCHMENT = 3000003
BATCH_STATUS_GRADING = 3000004


def index(request):
    template = loader.get_template('beans_intake/index.html')
    context = {
        'message': [],
    }
    return HttpResponse(template.render(context, request))


def handle_uploaded_file(f):
    file_name = 'uploads/'+f.name
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_name

def get_intake_model(intake_form):
    pass

def process_intake_form(intake_form, file_name):
    
    intake = Intake(supervisor_name=intake_form.cleaned_data['supervisor_name'],  # name,
                    lot_location=intake_form.cleaned_data['lot_location'],
                    box_count=intake_form.cleaned_data['box_count'],
                    total_weight=intake_form.cleaned_data['total_weight'],
                    discarded_weight=intake_form.cleaned_data['discarded_weight'],
                    refloated_weight=intake_form.cleaned_data['refloated_weight'],
                    proof_file=file_name,
                    supervisor_signature=intake_form.cleaned_data['supervisor_signature'],
                    representative_name='',
                    representative_signature=''
                    )
                    
    batch = Batch(location = intake.lot_location, 
                  batch_weight = intake.total_weight - (intake.discarded_weight + intake.refloated_weight),
                  is_second_float = False,
                  intake = intake,
                  status = Status.objects.get(pk=BATCH_STATUS_FLOATED)
                )

    with transaction.atomic():
        intake.save()
        batch.save()
    
    
    intake = Intake.objects.get(pk=intake.id)
    return intake


def own_intake(request):
    context = {}
    
    if request.POST:
        intake_form = OwnIntakeForm(request.POST, request.FILES)

        if intake_form.is_valid():
            file_name = handle_uploaded_file(request.FILES["proof_file"])
            intake = process_intake_form(intake_form, file_name)

            context['message'] = "Intake saved."
            context['intake'] = intake

            return render(request, intake_details_template, context)
        else:
            context['message'] = "Intake Failed."
            context['error'] = True
    
    # Create new form
    context['form'] = OwnIntakeForm()

    return render(request, own_intake_template, context)


# Show Intake details
def get_intake_details(request, intake_id):
    try:
        intake = Intake.objects.get(pk=intake_id)
    except Intake.DoesNotExist:
        raise Http404("Intake does not exist")
    return render(request, intake_details_template, {'intake': intake})


def suppliers_intake(request):
    template = loader.get_template('beans_intake/suppliers_intake.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))
