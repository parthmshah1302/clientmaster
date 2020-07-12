from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from pages.views import home_view

def home_view(*args, **kwargs ):
    return HttpResponse("<h1> Hello World </h1>")

def contact_view(*args, **kwargs ):
    return HttpResponse("<h1> Contact Views </h1>")
