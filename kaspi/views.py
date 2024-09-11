from django.shortcuts import render
from django.shortcuts import render
from .models import Good, KaspiShop

from django.http import HttpResponse
from .serializer import GoodSerializer, KaspiSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class ApiGoodsViewSet(ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

class ApiGoodsViewSetReadOnly(ReadOnlyModelViewSet):
    queryset = KaspiShop.objects.all()
    serializer_class = KaspiSerializer


# class APIGoods(generics.ListAPIView):
#     queryset = Good.objects.all()
#     serializer_class = GoodSerializer




# class APIGoodsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Good.objects.all()
#     serializer_class = GoodSerializer


# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def api_good_detail(request, pk):
#     good = Good.objects.get(pk=pk)
#     if request.method == "GET":
#         serializer = GoodSerializer(good)
#         return Response(serializer.data)
#     elif request.method == "PUT" or request.method == "PATCH":
#         serializer = GoodSerializer(good, data=request.data, partial=True   )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         good.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def api_goods(request):
#     if request.method == "GET":
#         goods = Good.objects.all()
#         serializer = GoodSerializer(goods, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = GoodSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)