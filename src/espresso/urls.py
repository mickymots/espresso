"""espresso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', include('homepage.urls')),    
    path('parchment_intake/', include('parchment_intake.urls')),
    path('green_beans_intake/', include('green_beans_intake.urls')),
    path('beans_intake/', include('beans_intake.urls')),
    path('dry_coffee/', include('dry_coffee.urls')),    
    path('reports/', include('reports.urls')),    
    path('hull_grade/', include('hull_grade.urls')),    
    path('admin/', admin.site.urls),
]
