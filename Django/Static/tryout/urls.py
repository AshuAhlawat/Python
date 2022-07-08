from django.contrib import admin
from django.urls import path
from django.shortcuts import render

from django.conf import settings
from django.conf.urls.static import static


def home(r):
    return render(r, "home.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
] 

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
