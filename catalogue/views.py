from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("this is test for catalogue/list....")