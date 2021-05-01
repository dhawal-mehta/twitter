from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
from .models import Tweet

from .forms import TweetForm

def tweet_list_view(request, *args, **kwargs):
    allTweets = Tweet.objects.all()
    tweet_list = [tweet.serialize() for tweet in allTweets ]
    data = {
        "response": tweet_list
    }
    return JsonResponse(data)

def tweet_create_view(request, *args, **kwargs):
    # print("ajax", request.is_ajax())
    
    form  = TweetForm(request.POST or None)
    # print("post data is", request.POST)
    
    next_url = request.POST.get("next") or None
    # print("next_url", next_url)



    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        # if next_url != None :
        
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)

        if next_url != None and is_safe_url(next_url, settings.ALLOWED_HOSTS):
            return redirect(next_url)   
             
        form = TweetForm()
    else:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)

    # if form.errors:
    #     if

    return render(request, 'components/form.html', context={"form":form})

# Create your views here.
def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # test = kwargs
    # print(test, test["id"])
    # html = "<h1>Hello World!</ h1>"
    return render(request, 'tweets/index.html', context={}, status=200)


def home_detail_view(request, id, *args, **kwargs):
    data = {
        "id": id,
    }

    status=200
    try:
        obj = Tweet.objects.get(id=id)
        data["content"] = obj.content
    except:
        data['message'] = "Not found"
        status = 404

    return JsonResponse(data, status=status)