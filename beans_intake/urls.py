from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('own/', views.own_intake, name='own_intake'),
   
    path('suppliers/', views.suppliers_intake, name='suppliers_intake'),
    
]