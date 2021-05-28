from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .forms.coffee_intake_form import ParchmentIntakeForm
from parchment_intake.models import ParchmentIntake, ParchmentIntakeFiles

# Template files
parchment_intake_template = 'parchment_intake/parchment_intake.html'
parchment_intake_details_template = 'parchment_intake/parchment_intake_details.html'

def index(request):

    context = {}
    query_results = ParchmentIntake.objects.all().order_by('id')
    context['query_results'] =  query_results
    return render(request, 'parchment_intake/index.html', context=context)



def process_intake_form(is_external, intake):
    intake = intake.save()
    intake = ParchmentIntake.objects.get(pk=intake.id)
    return intake



def do_coffee_intake(request):
    context = {}

    if request.POST:
        intake_form = ParchmentIntakeForm(request.POST, request.FILES)
        proof_files = request.FILES.getlist('proof_files')

        if intake_form.is_valid():
            
            intake = process_intake_form(False, intake_form)

            for file_obj in proof_files:
            
                proof_file = ParchmentIntakeFiles(intake= intake, proof_file=file_obj)
                proof_file.save()

            # return redirect('intake_details', intake_id=intake.id)
            return redirect('parchment_index')

        else:
            context['message'] = "Intake Failed."
            context['form'] = intake_form
    else:
        # Create new form
        context['form'] = ParchmentIntakeForm()
    return render(request, parchment_intake_template, context)



def coffee_intake_details(request, intake_id):
    try:
        intake = ParchmentIntake.objects.get(pk=intake_id)
        try:
            proof_files = ParchmentIntakeFiles.objects.all().filter(intake=intake)
        except ObjectDoesNotExist as e:
            proof_files = None
            
    except ParchmentIntake.DoesNotExist:
        raise Http404("parchment Intake does not exist")
    return render(request, parchment_intake_details_template, {'intake': intake, 'proof_files': proof_files})

