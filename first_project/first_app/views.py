from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Alhamdulillah! This is my first django page</h1>")

def about(request):
    return HttpResponse("<h3>Alhamdulillah! This is my about page</h3>")