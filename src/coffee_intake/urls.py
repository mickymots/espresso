from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('do_intake/', views.do_coffee_intake, name='do_coffee_intake'),
    path('<int:intake_id>/', views.coffee_intake_details, name='do_coffee_intake'),

]