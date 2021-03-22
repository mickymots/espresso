from django.shortcuts import render

from beans_intake.models import OwnIntake

def index(request):
    context = {}
    query_results = OwnIntake.objects.all()
    context['query_results'] =  query_results
    return render(request, 'homepage/index.html', context=context)
