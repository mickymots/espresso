from django.shortcuts import render, redirect
from django.db import transaction
from django.http import HttpResponse, Http404
from django.template import loader
from jsignature.utils import draw_signature
from .forms.own_intake_form import OwnIntakeForm
from .forms.supplier_intake_form import SupplierIntakeForm
from .forms.refloat_intake_form import RefloatIntakeForm
from .models import Intake, Location, Status, Batch, Refloat


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


def handle_uploaded_file(request):
    if request.FILES:
        filedata = request.FILES["proof_file"]

        file_name = 'uploads/'+filedata.name
        with open(file_name, 'wb+') as destination:
            for chunk in filedata.chunks():
                destination.write(chunk)
        return file_name
    

def get_intake_model(intake_form):
    pass

def process_intake_form(is_external, intake_form, file_name):

    # intake_form.cleaned_data['representative_name']
    representative_name = ''
    representative_signature = ''

    if is_external:
         representative_name = intake_form.cleaned_data['representative_name']
         representative_signature=intake_form.cleaned_data['representative_signature']
    
    intake = Intake(supervisor_name=intake_form.cleaned_data['supervisor_name'],  # name,
                    lot_location=intake_form.cleaned_data['lot_location'],
                    total_box_count=intake_form.cleaned_data['box_count'],
                    is_floated = intake_form.cleaned_data['is_floated'],
                   
                    proof_file=file_name,
                    supervisor_signature=intake_form.cleaned_data['supervisor_signature'],
                    representative_name= representative_name,
                    representative_signature = representative_signature,
                    is_external = is_external
                    )
                    
    # batch = Batch(location = intake.lot_location, 
    #               batch_weight = intake.total_weight - (intake.discarded_weight + intake.refloated_weight),
    #               is_second_float = False,
    #               intake = intake,
    #               status = Status.objects.get(pk=BATCH_STATUS_FLOATED)
    #             )

    with transaction.atomic():
        intake.save()
        # batch.save()
        # if intake.refloated_weight > 0:
        #     refloat = Refloat(intake = intake, refloat_weight = intake.refloated_weight)
        #     refloat.save()
                
    intake = Intake.objects.get(pk=intake.id)
    return intake


def own_intake(request):
    context = {}
    
    if request.POST:
        intake_form = OwnIntakeForm(request.POST, request.FILES)

        if intake_form.is_valid():
            
            file_name = handle_uploaded_file(request)
            intake = process_intake_form(False, intake_form, file_name)

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
    template = 'beans_intake/suppliers_intake.html'
    context = {}
    
    if request.POST:
        intake_form = SupplierIntakeForm(request.POST, request.FILES)

        if intake_form.is_valid():
            file_name = handle_uploaded_file(request.FILES["proof_file"])
            intake = process_intake_form(True, intake_form, file_name)

            context['message'] = "Intake saved."
            context['intake'] = intake

            return render(request, intake_details_template, context)
        else:
            context['message'] = "Intake Failed."
            context['error'] = True
    
    # Create new form
    context['form'] = SupplierIntakeForm()
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
    refloat  = Refloat.objects.get(pk=refloat_id)

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

        batch = Batch(location = refloat.intake.lot_location, 
                  batch_weight = total_weight,
                  is_second_float = True,
                  intake = refloat.intake,
                  status = Status.objects.get(pk=BATCH_STATUS_FLOATED)
                )
        batch.save()
        refloat.save()

    context = {}
    context['message'] = f"Refloat Intake Created - Batch ID: {batch.id}"
    return redirect('get refloats')