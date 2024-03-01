from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(" <h1>Search for love -> Tinder.<br> Search for lost -> Finder.</h1>")

def about(request):
    return HttpResponse(" Get to know us more")