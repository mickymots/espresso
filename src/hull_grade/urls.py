from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='haul_grade_index'),
    # path('<str:batch_status>/', views.get_batch_with_status, name='get_batch_list'),
    path('<str:batch_type>/<int:intake_id>/', views.select_for_processing, name='select_for_processing'),
]