from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'gvozdje'
urlpatterns = [

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.gvozdje, name='home'),
    path('user', views.userPage, name='userPage'),
    path('mreza', views.createMreza, name='Mreza'),
    path('gvozdje', views.createGvozdje, name='Gvozdje'),

    path('update_mreza/<int:mreza_id>/', views.updateMreza, name='UpdateM'),
    path('update_gvozdje/<int:gvozdje_id>/', views.updateGvozdje, name='UpdateG'),

    path('deleteMreza/<int:mreza_id>/', views.deleteMreza, name='DeleteM'),
    path('deleteGvozdje/<int:gvozdje_id>/', views.deleteGvozdje, name='DeleteG')

]