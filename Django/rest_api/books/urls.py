from django.urls import path,include
from . import views

urlpatterns = [
    # path('data/',views.data_all, name = "data_all"),
    path('all/',views.allNovelAPIView.as_view()),
    # path('data/<str:username>/',views.data_one, name = "data_one")
    path('username/<str:username>/',views.oneNovelAPIView.as_view(), name = "data_one")
]
