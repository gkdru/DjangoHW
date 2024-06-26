from django.shortcuts import render
from .models import IceCream
from django.http import HttpResponse
from django.db.models import Sum


def get_id(request):
    i1 = IceCream.objects.get(pk=1)
    return HttpResponse(f"ID:{i1.id}, Flavor:{i1.flavor}")


def get_sum(request):
    return HttpResponse(f"Sum:{IceCream.objects.aggregate(Sum("price"))["price__sum"]}")
