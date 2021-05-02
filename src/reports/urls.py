from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='report_index'),
    path('<str:batch_status>/', views.get_batch_with_status, name='get_batch_list'),
    path('<str:batch_status>/<int:intake_id>/', views.get_intake_details, name='report_intake_details'),

]