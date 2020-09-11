from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
def index(request):
    ''' returns the index page (in this case no index page exists so it redirects to the serach page) '''
    return HttpResponseRedirect(reverse(search))

# Create your views here.
def search(request):
    ''' returns the html search page with an input field to receive query from user '''
    return render(request, "search.html")

# Create your views here.
def search_result(request):
    ''' returns the search result from searching youtube api as html response '''
    context = {
        "search_query": "making up shopping",
        "result": [
            {
                "title": "Full face Drug",
                "channel_name": "Christen Dominique",
                "num_of_views": 441373,
                "description": "Watch me on style code live Now and here at 9pm EST and 6pm EPN . here is my drug store vs the second drug store where we whatever",
            },
            {
                "title": "Half Full face Drug",
                "channel_name": "Christen Dominique",
                "num_of_views": 441373,
                "description": "Watch me on style code live Now and here at 9pm EST and 6pm EPN . here is my drug store vs the second drug store where we whatever"
            },
            {
                "title": "Almost Full face Drug",
                "channel_name": "Christen Dominique",
                "num_of_views": 441373,
                "description": "Watch me on style code live Now and here at 9pm EST and 6pm EPN . here is my drug store vs the second drug store where we whatever"
            },
        ]
    }
    return render(request, "search_result.html", context)