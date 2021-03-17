from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('dry_coffee/index.html')
    context = {
        'latest_question_list': [],
    }
    return HttpResponse(template.render(context, request))