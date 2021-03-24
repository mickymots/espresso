from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, Http404

from django.template import loader
from jsignature.utils import draw_signature

from .forms.own_intake_form import OwnIntakeForm
from .models import Intake, Location

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


def own_intake(request):
    context = { }
    intake_form = None
    if request.POST: 
        intake_form = OwnIntakeForm(request.POST, request.FILES) 
        if intake_form.is_valid(): 
           
            file_name = handle_uploaded_file(request.FILES["proof_file"])
            print(intake_form)
            intake = Intake(supervisor_name= intake_form.cleaned_data['supervisor_name'], #name,
                            lot_location = intake_form.cleaned_data['lot_location'],
                            box_count = intake_form.cleaned_data['box_count'],
                            total_weight = intake_form.cleaned_data['total_weight'],
                            discarded_weight = intake_form.cleaned_data['discarded_weight'],
                            refloated_weight = intake_form.cleaned_data['refloated_weight'],
                            proof_file = file_name,
                            supervisor_signature = intake_form.cleaned_data['supervisor_signature'],
                            representative_name = '',
                            representative_signature = ''
                            
                            )
            
            intake.save()
            
            intake = Intake.objects.get(pk=intake.id)
            print(intake)

            context['message'] = "Intake saved."
            context['intake'] = intake
            
            return render(request, f'beans_intake/intake_details.html/' , context)
        else:
            context['message'] = "Intake Failed."
            context['error'] = True
    # Create new form
    intake_form = OwnIntakeForm() 
    context['form'] =  intake_form
    
    return render(request, 'beans_intake/own_intake.html' , context)


# Show Intake details
def get_intake_details(request, intake_id):
    try:
        intake = Intake.objects.get(pk=intake_id)
    except Intake.DoesNotExist:
        raise Http404("Intake does not exist")
    return render(request, 'beans_intake/intake_details.html', {'intake': intake})


def suppliers_intake(request):
    template = loader.get_template('beans_intake/suppliers_intake.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))