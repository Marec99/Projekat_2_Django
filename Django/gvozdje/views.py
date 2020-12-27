from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from .decorators import unauthentificated_user, allow_users, admin_only
from .forms import *

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *

@unauthentificated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='customer')
                user.groups.add(group)

                messages.success(request, 'Account created for ' + username)

                return redirect('gvozdje:login')

        context = {'form':form}
        return render(request, 'gvozdje/register.html', context)

@unauthentificated_user
def loginPage(request):
        if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')

           user = authenticate(request, username=username, password=password)

           if user is not None:
               login(request, user)
               return redirect('gvozdje:home')
           else:
               messages.info(request, 'Username or Password is incorect')

        context = {}
        return render(request, 'gvozdje/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('gvozdje:login')

@login_required(login_url='gvozdje:login')
@admin_only
def gvozdje(request):
    gvozdje = Gvozdje.objects.all()
    mreza = Mreza.objects.all()
    return render(request, 'gvozdje/dashboard.html', {'gvozdje': gvozdje, 'mreza': mreza})

def userPage(request):
    gvozdje = Gvozdje.objects.all()
    mreza = Mreza.objects.all()
    return render(request, 'gvozdje/user.html', {'gvozdje': gvozdje, 'mreza': mreza})

@login_required(login_url='gvozdje:login')
@allow_users(allowed_roles=['admin'])
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

@login_required(login_url='gvozdje:login')
@allow_users(allowed_roles=['admin'])
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

@login_required(login_url='gvozdje:login')
@allow_users(allowed_roles=['admin'])
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

@login_required(login_url='gvozdje:login')
@allow_users(allowed_roles=['admin'])
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

@login_required(login_url='gvozdje:login')
@allow_users(allowed_roles=['admin'])
def deleteMreza(request, mreza_id):
    mreza = Mreza.objects.get(id=mreza_id)
    if request.method == "POST":
        mreza.delete()
        return redirect('/')

    context = {'item': mreza}
    return  render(request, 'gvozdje/delete_mreza.html', context)

@login_required(login_url='gvozdje:login')
@allow_users(allowed_roles=['admin'])
def deleteGvozdje(request, gvozdje_id):

    gvozdje = Gvozdje.objects.get(id=gvozdje_id)

    if request.method == "POST":
        gvozdje.delete()
        return redirect('/')

    context = {'item': gvozdje}
    return  render(request, 'gvozdje/delete_gvozdje.html', context)