from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('beans_intake/index.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))