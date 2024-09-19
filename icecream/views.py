from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import IceCream, Customer
from .serializer import IceCreamSerializer, CustomerSerializer

class IceCreamViewSet(ModelViewSet):    
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

