from django.forms import ModelForm
from .models import *

class GvozdjeForm(ModelForm):
    class Meta:
        model = Gvozdje
        fields = '__all__'

class MrezaForm(ModelForm):
    class Meta:
        model = Mreza
        fields = '__all__'