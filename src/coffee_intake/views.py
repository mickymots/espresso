from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .forms.coffee_intake_form import CoffeeIntakeForm
from coffee_intake.models import CoffeeIntake, CoffeeIntakeFiles

# Template files
coffee_intake_template = 'coffee_intake/coffee_intake.html'
coffee_intake_details_template = 'coffee_intake/coffee_intake_details.html'

def index(request):

    context = {}
    query_results = CoffeeIntake.objects.all()
    context['query_results'] =  query_results
    return render(request, 'coffee_intake/index.html', context=context)



def process_intake_form(is_external, intake):
    intake = intake.save()
    intake = CoffeeIntake.objects.get(pk=intake.id)
    return intake



def do_coffee_intake(request):
    context = {}

    if request.POST:
        intake_form = CoffeeIntakeForm(request.POST, request.FILES)
        proof_files = request.FILES.getlist('proof_files')

        if intake_form.is_valid():
            
            intake = process_intake_form(False, intake_form)

            for file_obj in proof_files:
            
                proof_file = CoffeeIntakeFiles(intake= intake, proof_file=file_obj)
                proof_file.save()

            # return redirect('intake_details', intake_id=intake.id)
            return redirect('index')

        else:
            context['message'] = "Intake Failed."
            context['form'] = intake_form
    else:
        # Create new form
        context['form'] = CoffeeIntakeForm()
    return render(request, coffee_intake_template, context)



def coffee_intake_details(request, intake_id):
    try:
        intake = CoffeeIntake.objects.get(pk=intake_id)
        try:
            proof_files = CoffeeIntakeFiles.objects.all().filter(intake=intake)
        except ObjectDoesNotExist as e:
            proof_files = None
            
    except CoffeeIntake.DoesNotExist:
        raise Http404("Coffee Intake does not exist")
    return render(request, coffee_intake_details_template, {'intake': intake, 'proof_files': proof_files})

