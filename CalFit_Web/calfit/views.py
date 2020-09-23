from django.shortcuts import render
from django.contrib import auth
from django.http import *
from django.contrib.auth.decorators import login_required
from calfit.helper_methods import *
import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    if request.method == 'GET':
        context = dict()
        context["username"] = "Wayne Li"
        context["goal_today"] = "How are you doing?"
        context["current_steps"] = "This is a test message!"
        return render(request, 'index.html', {})
