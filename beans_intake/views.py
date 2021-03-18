from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .forms.own_intake_form import OwnIntakeForm

def index(request):
    template = loader.get_template('beans_intake/index.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))


def handle_uploaded_file(f):   
    with open('uploads/'+f.name, 'wb+') as destination:   
        for chunk in f.chunks(): 
            destination.write(chunk)   



def own_intake(request):
    template = loader.get_template('beans_intake/own_intake.html')
    context = { }

    if request.POST: 
        form = OwnIntakeForm(request.POST, request.FILES) 
        if form.is_valid(): 
            print(form)
            handle_uploaded_file(request.FILES["proof_file"]) 
    else: 
        form = OwnIntakeForm() 

    context['form'] =  form
    
    return HttpResponse(template.render(context, request))


def suppliers_intake(request):
    template = loader.get_template('beans_intake/suppliers_intake.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))