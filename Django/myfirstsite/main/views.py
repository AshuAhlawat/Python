from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def login(response):
    return HttpResponse("<h2> Login </h2>")

def home(response):
    return render(response, "main/home.html", {})

def signup(response):
    return HttpResponse("<h2> Sign-up </h2>")

def indexall(response):
    todos = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"todo":todos})

def index(response, id):
    index = ToDoList.objects.get(id=id)
    return HttpResponse("<h2> Index : %s </h2>" %index.name) 