from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoby/', views.osoba_list),
    path('stanowiska/', views.stanowisko_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('stanowiska/<int:pk>/', views.stanowisko_detail)
]