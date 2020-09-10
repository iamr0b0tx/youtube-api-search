from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('search/', views.search),
    path('search/result/', views.search_result),
]
