from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # test = kwargs
    # print(test, test["id"])
    html = "<h1>Hello World!</ h1>"
    return HttpResponse(html)

def home_detail_view(request, id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=id)
    except:
        raise Http404

    html = "<p> " + str(id)+ obj.content+ " </ h1>"
    return HttpResponse(html)