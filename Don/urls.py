from django.urls import path
from . import views

urlpatterns = [
    path('Don/', views.suiviDon, name='suiviDon'),
    path('inscription/', views.inscription, name='inscription'),
    
]