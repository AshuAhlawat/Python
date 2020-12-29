from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(response):
    return HttpResponse("<h2> Login </h2>")

def home(response):
    return HttpResponse("<h1><center> Home </center></h1>")

def signup(response):
    return HttpResponse("<h2> Sign-up </h2>")