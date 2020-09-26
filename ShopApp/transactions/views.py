from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from transactions.helper_methods import *
from transactions.models import *


def registration(request):
    context = {}

    if request.method == 'GET':
        return render(request, 'registration.html', context)

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        context["username_value"] = username
        context["password_value"] = password
        context["confirm_password_value"] = confirm_password

        # User object here is default by Django
        if username_exist(username):
            context["duplicated_username"] = True
            return render(request, "registration.html", context)

        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if password matches
        if password == confirm_password and password is not "" or None:
            User.objects.create_user(username=username, password=password)
            return render(request, "login.html", context)
        else:
            context["psw_not_match"] = True
            return render(request, "registration.html", context)


def login(request):
    """
    :param request: request received
    :return: http response about logging in
    """
    context = {}

    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect('/transactions/index')
        return render(request, 'login.html', context)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        context["username_value"] = username

        if not username_exist(username):
            context["user_not_exist"] = True
            return render(request, 'login.html', context)

        # Check username and password, if valid, return a User object
        user = auth.authenticate(username=username, password=password)
        if user:
            # If success
            auth.login(request, user)
            if username == "admin":
                return HttpResponseRedirect('/transactions/merchandise/')
            else:
                return HttpResponseRedirect('/transactions/index/')
        else:
            context["psw_not_match"] = True
            return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/transactions/login/')


def index(request):
    return render(request, 'index.html', context={})


def product_details(request, product_idx):
    context = dict()

    if request.method == 'GET':
        try:
            product = Product.objects.get(idx=product_idx)
            context["product"] = product
        except Exception as e:
            print(e)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        try:

            print("\n----------------------------")
            print(quantity)
            print(product_idx)
            print(Product.objects.get(idx=product_idx).stock)

            product = Product.objects.get(idx=product_idx)
            product.stock = 0 if product.stock < quantity else product.stock - quantity
            product.update()
            product.save()
            context["product"] = product
        except Exception as e:
            print(e)

    return render(request, 'product-details.html', context=context)


def merchandise(request):
    context = dict()
    if request.method == 'GET':
        context["products"] = Product.objects.all()
        context["limit"] = Product.objects.all()[0].limit

    if request.method == 'POST':
        limit = int(request.POST.get('limit'))
        for product in Product.objects.all():
            product.limit = limit
            product.update()
            product.save()
        context["products"] = Product.objects.all()
        context["limit"] = Product.objects.all()[0].limit
    return render(request, 'cart.html', context=context)
