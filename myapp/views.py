from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import io
from django.template import loader

# Create your views here.



# this functions main I create a new page
def home(request) :
    if request.method == "POST" :
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.content = content
        contact.save()
    
    image = {'Image' : Image.objects.all()}
    activitie = {'Activitie' : Activitie.objects.all()}
    context = {**image, **activitie}
    return render(request, 'myApp/home.html', context)

def about(request):
    ressources = {'Ressources' : Resshaumains.objects.all}
    revenus =  {'Revenus' : Revenus.objects.all}
    depenses =  {'Depenses' : Depenses.objects.all}
    dettes =  {'Dettes' : Dettes.objects.all}
    dialyse =  {'DialyseDataYear' : DialyseDataYear.objects.all}
    cout =  {'CoutDePatients' : CoutDePatients.objects.all}
    
    context = {**ressources, **revenus, **depenses, **dettes, **dialyse, **cout}
    # Render the template using the combined context
    return render(request, 'myApp/about.html', context)
     
def contact(request) :
    return render(request, 'myApp/contact.html')


def service(request) :
    activitie = {'Activitie' : Activitie.objects.all()}
    context = {**activitie}
    return render(request, 'myApp/service.html', context)


def service1(request) :
    activitie = {'Service' : Service.objects.all()}
    context = {**activitie}
    return render(request, 'myApp/service.html', context)


def service2(request) :
    activitie = {'Service' : Service.objects.all()}
    context = {**activitie}
    return render(request, 'myApp/service2.html', context)


def service3(request) :
    activitie = {'Service' : Service.objects.all()}
    context = {**activitie}
    return render(request, 'myApp/service3.html', context)


def service4(request) :
    activitie = {'Service' : Service.objects.all()}
    context = {**activitie}
    return render(request, 'myApp/service4.html', context)