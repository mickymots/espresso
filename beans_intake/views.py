from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from jsignature.utils import draw_signature

from .forms.own_intake_form import OwnIntakeForm
from .models import OwnIntake, Location

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
            
            intake_data = OwnIntake(name= intake_form.cleaned_data['name'], #name,
                                    lot_location = intake_form.cleaned_data['lot_location'],
                                    
                                    box_count = intake_form.cleaned_data['box_count'],
                                    discarded_weight = intake_form.cleaned_data['discarded_weight'],
                                    refloated_weight = intake_form.cleaned_data['refloated_weight'],
                                    proof_file = file_name,
                                    signature = intake_form.cleaned_data['signature']
                                    )
            
            intake_data.save()
            
            context['message'] = "Intake saved."
        else:
            print(intake_form)
    # Create new form
    intake_form = OwnIntakeForm() 
    context['form'] =  intake_form
    
    return render(request, 'beans_intake/own_intake.html' , context)



def suppliers_intake(request):
    template = loader.get_template('beans_intake/suppliers_intake.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))