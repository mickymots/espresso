from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.index, name='index'),
    path('own_intake/', views.own_intake, name='own_intake'),
    path('<int:intake_id>/', views.get_intake_details, name='intake_details'),
    path('suppliers_intake/', views.suppliers_intake, name='suppliers_intake'),
    path('get_refloats/', views.get_refloats, name='get refloats'),
    path('get_refloats/<int:refloat_id>/', views.get_refloat_details, name='get refloats with id'),
    
]