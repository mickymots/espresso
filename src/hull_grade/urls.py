from django.urls import path

from . import views


urlpatterns = [
    path('batch_list', views.get_batch_list, name='hull_grade_batch_list'),
    path('', views.get_dashboard, name='hull_grade_index'),
    path('grading_intake/<str:batch_type>/<int:intake_id>/', views.get_intake_form, name='select_for_processing'),
    path('grading_intake_update/<int:intake_id>/', views.get_intake_update_form, name='select_for_intake_update'),
    path('grading_result/<int:intake_id>/', views.get_record_result_form, name='record_grading_result'),

]