from django.urls import path

from . import views

urlpatterns = [
    path('', views.gvozdje, name='home'),
    path('mreza', views.mrezaIzmene, name='Mreza'),
    path('gvozdje', views.gvozdjeIzmene, name='Gvozdje'),
]