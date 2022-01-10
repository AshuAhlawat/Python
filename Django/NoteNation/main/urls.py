from django.urls import path
from . import views

urlpatterns = [
    # path("home/", views.home, name="home"),
    path("allnotes/", views.allnotes, name="links"),
    # path("",views.base, name="base")
]