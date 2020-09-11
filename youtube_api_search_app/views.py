from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse(search))

# Create your views here.
def search(request):
    return render(request, "search.html")

# Create your views here.
def search_result(request):
    context = {
        "search_query": "making up shopping",
        "result": [
            {
                "title": "Full face Drug",
                "channel_name": "Christen Dominique",
                "num_of_views": 441373,
                "description": "Watch me on style code live Now and here at 9pm EST and 6pm EPN . here is my drug store vs the second drug store where we whatever"
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