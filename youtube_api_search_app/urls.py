from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('search/result/', views.search_result, name="search_result"),
]
