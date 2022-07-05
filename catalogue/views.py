from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

def categoty_list(request):

    cat_list = Category.objects.all()

    return HttpResponse(cat_list)
