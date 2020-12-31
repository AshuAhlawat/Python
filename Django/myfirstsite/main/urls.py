from django.urls import  path
from . import views

urlpatterns = [
    path("myfirstsite", views.home, name = "home"),
    path("myfirstsite/login", views.login, name = "login"),
    path("myfirstsite/signup", views.signup, name = "signup"),          path("id/all", views.indexall, name = "indeall"),
    path("myfirstsite/id/<int:id>", views.index, name = "index")
]