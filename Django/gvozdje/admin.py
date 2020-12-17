from django.contrib import admin

# Register your models here.

from .models import Gvozdje, Mreza

admin.site.register(Gvozdje)
admin.site.register(Mreza)