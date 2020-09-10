from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse(search))

# Create your views here.
def search(request):
    return render(request, "search.html")

# Create your views here.
def search_result(request):
    return render(request, "youtube_api_search_app/search_result.html")