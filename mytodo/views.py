from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    text = "This is a notes App in work"
    return HttpResponse(text)