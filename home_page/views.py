from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def starting_page(request):
    return HttpResponse('hello this is home')