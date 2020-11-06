from django.shortcuts import render
from transactions.models import *


def index(request):

    context = dict()

    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')

        if Person.objects.filter(name=name).exists():
            context["submit_error"] = True
        else:
            # Person.objects.create(name=name, image=image)
            Person.objects.create(name=name, number=number)
            context["submit_success"] = True

        return render(request, 'index.html', context=context)

    return render(request, 'index.html', context=context)

