from django.shortcuts import render
# Create your views here.


# def show_index(req):
#     return render(req, 'server/index.html')
#
#
# def show_home(req):
#     return render(req, 'server/home.html')
#
#
# def show_create(req):
#     return render(req, 'server/create.html')

from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
