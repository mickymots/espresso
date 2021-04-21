from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='parchment_index'),
    path('do_intake/', views.do_coffee_intake, name='do_intake'),
    path('<int:intake_id>/', views.coffee_intake_details, name='show_coffee_intake'),

]