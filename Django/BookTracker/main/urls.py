from django.urls import path
from . import views

urlpatterns = [
    
    path("home/", views.home, name="home"),
    path("add/", views.add, name="links"),
    path("about/", views.about, name="about"),
    path("",views.base, name="base")
    
]