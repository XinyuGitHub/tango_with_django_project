from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requset):
    return HttpResponse("Rango says hey there partner!<br><a href='/rango/about/'>About</a>")

def about(requset):
    return HttpResponse("Rango says here is the about page.<br><a href='/rango/'>Index</a>")