from django.shortcuts import render
from django.http import HttpResponse


def gvozdje(request):
    return render(request, 'home.html')

def mrezaIzmene(request):
    return render(request, 'mrezaIzmene.html')

def gvozdjeIzmene(request):
    return render(request, 'gvozdjeIzmene.html')