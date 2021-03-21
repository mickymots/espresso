from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.index, name='index'),
    path('own/', views.own_intake, name='own_intake'),
    path('<int:intake_id>/', views.get_intake_details, name='intake_details'),
    path('suppliers/', views.suppliers_intake, name='suppliers_intake'),
    
]