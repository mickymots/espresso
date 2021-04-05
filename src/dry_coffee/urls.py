from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_batch_status/', views.update_batch_status, name='Update Batch Status'),
    path('get_batch_details/<int:batch_id>/', views.get_batch_details, name='Get Batch Details'),
    path('get_batch_with_status/<str:batch_status>/', views.get_batch_with_status, name='get_batch_with_status'),
    
]