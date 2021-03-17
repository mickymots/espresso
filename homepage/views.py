from django.shortcuts import render

# Create your views here.
def index(request):
    # template = loader.get_template('index.html')
    context = {
        'latest_question_list': [],
    }
    # return HttpResponse(template.render(context, request))

    return render(request, 'homepage/index.html', context=context)
    # return HttpResponse("Hello, world. You're at the home page.")