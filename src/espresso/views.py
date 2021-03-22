from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    # template = loader.get_template('index.html')
    context = {
        'latest_question_list': [],
    }
    # return HttpResponse(template.render(context, request))

    return render(request, 'index.html', context=context)
    # return HttpResponse("Hello, world. You're at the home page.")