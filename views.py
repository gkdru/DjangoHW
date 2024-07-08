from django.shortcuts import render
from django.http import JsonResponse
from .models import Book


def get_title(request):
    book_titles = [b.title for b in Book.objects.all()]
    return JsonResponse({"book_titles": book_titles})
