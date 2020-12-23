from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import *


from .models import *


def gvozdje(request):
    gvozdje = Gvozdje.objects.all()
    mreza = Mreza.objects.all()
    return render(request, 'gvozdje/dashboard.html', {'gvozdje': gvozdje, 'mreza': mreza})

def createMreza(request):
    form = MrezaForm()
    if request.method == 'POST':
        form = MrezaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)

    context = {'form': form}

    return render(request, 'gvozdje/mreza.html', context)

def createGvozdje(request):

    form = GvozdjeForm()
    if request.method == 'POST':
        form = GvozdjeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)

    context = {'form':form}

    return render(request, 'gvozdje/gvozdje.html', context)

def updateMreza(request, mreza_id):

    mreza = Mreza.objects.get(id = mreza_id)
    form = MrezaForm(instance=mreza)
    if request.method == "POST":
        form = MrezaForm(request.POST, instance=mreza)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)


    context = {'form':form}
    return render(request, 'gvozdje/mreza.html', context)


def updateGvozdje(request, gvozdje_id):

    gvozdje = Gvozdje.objects.get(id = gvozdje_id)
    form = GvozdjeForm(instance=gvozdje)
    if request.method == "POST":
        form = GvozdjeForm(request.POST, instance=gvozdje)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(ValueError)


    context = {'form':form}
    return render(request, 'gvozdje/gvozdje.html', context)

def deleteMreza(request, mreza_id):
    mreza = Mreza.objects.get(id=mreza_id)
    if request.method == "POST":
        mreza.delete()
        return redirect('/')

    context = {'item': mreza}
    return  render(request, 'gvozdje/delete_mreza.html', context)

def deleteGvozdje(request, gvozdje_id):

    gvozdje = Gvozdje.objects.get(id=gvozdje_id)

    if request.method == "POST":
        gvozdje.delete()
        return redirect('/')

    context = {'item': gvozdje}
    return  render(request, 'gvozdje/delete_gvozdje.html', context)