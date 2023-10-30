from django.http import HttpResponse
from rest_framework import generics
from .models import Osoba, Stanowisko
from .serializers import StanowiskoModelSerializer

#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#
#
# class StanowiskoListView(generics.ListCreateAPIView):
#     queryset = Stanowisko.objects.all()
#     serializer_class = StanowiskoModelSerializer
