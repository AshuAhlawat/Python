from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def signup(response):
    
    if response.method == 'POST':
        form=RegisterForm(response.POST)
        
        if form.is_valid():
            form.save()
    else:
        form=RegisterForm()    
        
    return render(response,'register/signup.html', {"form":form})

def login(response):
    return render(response,'register/login.html')