from django.shortcuts import render, redirect
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist 
from django.http import HttpResponse, Http404
from django.views.generic.edit import FormView
from django.template import loader
from jsignature.utils import draw_signature
from .forms.own_intake_form import OwnIntakeForm
from .forms.supplier_intake_form import SupplierIntakeForm
from .forms.supplier_intake_notes_form import SupplierIntakeNotesForm
from .forms.refloat_intake_form import RefloatIntakeForm
from .models import Intake, IntakeDetails, Location, Status, Refloat, IntakeNotes,IntakeFiles


# Template files
own_intake_template = 'beans_intake/own_intake.html'
intake_details_template = 'beans_intake/intake_details.html/'

BATCH_STATUS_INTAKE = 3000000
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




def process_intake_form(is_external, intake):
    
    intake = intake.save()
    intake = Intake.objects.get(pk=intake.id)

    # set external flag
    intake.is_external = is_external
    intake.save()

    # create intake details object
    intake_details = IntakeDetails(intake= intake,
                                   status=Status.objects.get(
                                       pk=BATCH_STATUS_INTAKE),
                                   marker_placed=False
                                   )
    intake_details.save()
   
    return intake


def own_intake(request):
    context = {}

    if request.POST:
        intake_form = OwnIntakeForm(request.POST, request.FILES)
        proof_files = request.FILES.getlist('proof_file')

        if intake_form.is_valid():
            
            intake = process_intake_form(False, intake_form)

            for f in proof_files:
                 proof_file = IntakeFiles(intake= intake, proof_file=f)
                 proof_file.save()

            return redirect('intake_details', intake_id=intake.id)
        else:
            context['message'] = "Intake Failed."
            context['form'] = intake_form
    else:
        # Create new form
        context['form'] = OwnIntakeForm()
    return render(request, own_intake_template, context)


# Show Intake details
def get_intake_details(request, intake_id):
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
            print(e)
            uploaded_files = None
    except ObjectDoesNotExist:
        intake_details = None
        intake_notes  = None
        uploaded_files = None

    except Intake.DoesNotExist:
        raise Http404("Intake does not exist")
    return render(request, intake_details_template, {'intake': intake, 'intake_details': intake_details, 'intake_notes':intake_notes, 'uploaded_files': uploaded_files})



def suppliers_intake(request):
    template = 'beans_intake/suppliers_intake.html'
    context = {}

    if request.POST:
        intake_form = SupplierIntakeForm(request.POST, request.FILES)
        notes_form = SupplierIntakeNotesForm(request.POST,  request.FILES)
        proof_files = request.FILES.getlist('proof_file')


        if intake_form.is_valid() and notes_form.is_valid():

            intake = process_intake_form(True, intake_form)
            
            intake_notes = IntakeNotes(
                intake=intake, notes=notes_form.cleaned_data['notes'])
            intake_notes.save()

            for f in proof_files:
                 proof_file = IntakeFiles(intake= intake, proof_file=f)
                 proof_file.save()

            return redirect('intake_details', intake_id=intake.id)
        else:
            context['message'] = "Intake Failed."
            context['form'] = intake_form
            context['notes_form'] = notes_form
    else:
        # Create new form
        context['form'] = SupplierIntakeForm()
        context['notes_form'] = SupplierIntakeNotesForm()

    return render(request, template, context)


def get_refloats(request):
    template = 'beans_intake/refloats.html'
    context = {}
    query_results = Refloat.objects.all().filter(floated=False)
    context['query_results'] = query_results
    return render(request, template, context=context)


def get_refloat_details(request, refloat_id):
    template = 'beans_intake/refloats_intake.html'
    context = {}
    refloat = Refloat.objects.get(pk=refloat_id)

    context['refloat'] = refloat
    context['form'] = RefloatIntakeForm()

    return render(request, template, context=context)


def do_refloat_intake(request):
    # template = 'beans_intake/index.html'
    if request.POST:
        refloat_id = request.POST.get('refloat_id')
        total_weight = request.POST.get('total_weight')

        refloat = Refloat.objects.get(pk=refloat_id)
        refloat.floated = True

        batch = Batch(location=refloat.intake.lot_location,
                      batch_weight=total_weight,
                      is_second_float=True,
                      intake=refloat.intake,
                      status=Status.objects.get(pk=BATCH_STATUS_FLOATED)
                      )
        batch.save()
        refloat.save()

    context = {}
    context['message'] = f"Refloat Intake Created - Batch ID: {batch.id}"
    return redirect('get refloats')
