from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index')
    path('suiviDon', views.suiviDon, name='suiviDon')
    
]