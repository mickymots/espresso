from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .forms.green_beans_intake_form import GreenBeansIntakeForm
from green_beans_intake.models import GreenBeansIntake, GreenBeansIntakeFiles

# Create your views here.
# Template files
green_beans_intake_template = 'green_beans_intake/green_beans_intake.html'
green_beans_details_template = 'green_beans_intake/green_beans_intake_details.html'

def index(request):

    context = {}
    query_results = GreenBeansIntake.objects.all()
    context['query_results'] =  query_results
    return render(request, 'green_beans_intake/index.html', context=context)



def process_intake_form(is_external, intake):
    intake = intake.save()
    intake = GreenBeansIntake.objects.get(pk=intake.id)
    return intake



def do_green_beans_intake(request):
    context = {}

    if request.POST:
        intake_form = GreenBeansIntakeForm(request.POST, request.FILES)
        proof_files = request.FILES.getlist('proof_files')

        if intake_form.is_valid():
            
            intake = process_intake_form(False, intake_form)

            for file_obj in proof_files:
            
                proof_file = GreenBeansIntakeFiles(intake= intake, proof_file=file_obj)
                proof_file.save()

            # return redirect('intake_details', intake_id=intake.id)
            return redirect('green_beans_index')

        else:
            context['message'] = "Intake Failed."
            context['form'] = intake_form
    else:
        # Create new form
        context['form'] = GreenBeansIntakeForm()
    return render(request, green_beans_intake_template, context)



def green_beans_intake_details(request, intake_id):
    try:
        intake = GreenBeansIntake.objects.get(pk=intake_id)
        try:
            proof_files = GreenBeansIntakeFiles.objects.all().filter(intake=intake)
        except ObjectDoesNotExist as e:
            proof_files = None
            
    except GreenBeansIntake.DoesNotExist:
        raise Http404("parchment Intake does not exist")
    return render(request, green_beans_details_template, {'intake': intake, 'proof_files': proof_files})

