from django.urls import path, include

urlpatterns = [
    path('', include('youtube_api_search_app.urls')),
]
