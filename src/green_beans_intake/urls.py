from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='green_beans_index'),
    path('do_intake/', views.do_green_beans_intake, name='do_intake'),
    path('<int:intake_id>/', views.green_beans_intake_details, name='show_intake'),

    
]