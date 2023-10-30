from django.urls import path
#from .views import StanowiskoListView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('stanowisko/', StanowiskoListView.as_view(), name='stanowisko-list'),

]