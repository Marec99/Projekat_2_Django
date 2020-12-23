from django.db import models

# Create your models here.


class Gvozdje(models.Model):
    naziv = models.CharField(max_length=50)
    jedinicaMere = models.CharField(max_length=4)
    cena_DIN = models.IntegerField(default=0)

    def __str__(self):
        return self.naziv

class Mreza(models.Model):
    naziv = models.CharField(max_length=100)
    dimenzijeKocke = models.CharField(max_length=50)
    dimenzije = models.CharField(max_length=50)
    jedinicaMere = models.CharField(max_length=4)
    cena_DIN = models.IntegerField(default=0)
    proizvedeno_Od = models.ForeignKey(Gvozdje, on_delete = models.CASCADE)

    def __str__(self):
        return self.naziv