from django.shortcuts import render

from beans_intake.models import Intake

def index(request):
    context = {}
    query_results = Intake.objects.all()
    context['query_results'] =  query_results
    return render(request, 'homepage/index.html', context=context)
