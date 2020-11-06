from django.shortcuts import render
from transactions.models import *


def index(request):

    context = dict()

    if request.method == 'POST':
        name = request.POST.get('name')
        # image = request.FILES['image']
        #
        # if not (image.name.endswith("png") or image.name.endswith("jpg")):
        #     context["file_error"] = True
        #     return render(request, 'new_car.html', context=context)

        if Person.objects.filter(name=name).exists():
            context["submit_error"] = True
        else:
            # Person.objects.create(name=name, image=image)
            Person.objects.create(name=name)
            context["submit_success"] = True

        return render(request, 'index.html', context=context)

    return render(request, 'index.html', context=context)

