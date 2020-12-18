from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.gvozdje, name='home'),
    path('mreza', views.mrezaIzmene, name='Mreza'),
    path('gvozdje', views.gvozdjeIzmene, name='Gvozdje'),
]