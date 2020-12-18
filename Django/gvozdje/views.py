from django.shortcuts import render


from Django.gvozdje.models import Mreza


def gvozdje(request):
    return render(request, 'home.html')

def mrezaIzmene(request):
    if request == "POST":
        naziv = request.POST['Naziv']
        dimenzijeKocke = request.POST['DimenzijeKocke']
        dimenzije = request.POST['Dimenzije']
        jedinicaMere = request.POST['JedinicaMere']
        cena_DIN = request.POST['cena']
        proizvedeno_Od = request.POST['gvozdje']
        inc = Mreza(naziv=naziv, dimenzije=dimenzije, dimenzijeKocke=dimenzijeKocke, jedinicaMere=jedinicaMere, cena_DIN=cena_DIN,proizvedeno_Od=proizvedeno_Od)
        inc.save()
    return render(request, 'mrezaIzmene.html')

def gvozdjeIzmene(request):
    return render(request, 'gvozdjeIzmene.html')