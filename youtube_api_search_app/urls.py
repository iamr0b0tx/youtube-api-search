from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('authorize', views.authorize, name="authorize"),
    path('oauth2callback', views.oauth2callback, name="oauth2callback"),
    path('search/', views.search, name="search"),
    path('search/result/', views.search_result, name="search_result"),
]
