from django.shortcuts import render


from .models import Mreza


def gvozdje(request):
    return render(request, 'home.html')

def mrezaIzmene(request):
    if request.method == "POST":

        naziv = request.POST['naziv']
        dimenzijeKocke = request.POST['kocka']
        dimenzije = request.POST['dimenzije']
        jedinicaMere = request.POST['jedinicaMere']
        cena_DIN = request.POST['cena']
        proizvedeno_Od = request.POST['gvozdje']
        inc = Mreza(naziv=naziv, dimenzije=dimenzije, dimenzijeKocke=dimenzijeKocke, jedinicaMere=jedinicaMere, cena_DIN=cena_DIN,proizvedeno_Od=proizvedeno_Od)
        inc.save()
        print("Mreza je dodata!!!")
    return render(request, 'mrezaIzmene.html')

def gvozdjeIzmene(request):
    return render(request, 'gvozdjeIzmene.html')