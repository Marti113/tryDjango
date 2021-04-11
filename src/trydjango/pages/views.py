from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    my_context = {
        "my_text": "This is about me",
        "my_number": 123,
        "my_list" : [13, 31, 71],
        "this is true": True
    }
    return render(request, "home.html", my_context)