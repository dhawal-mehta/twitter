from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

from .forms import TweetForm

def tweet_list_view(request, *args, **kwargs):
    allTweets = Tweet.objects.all()
    tweet_list = [{"id":tweet.id, "content": tweet.content, "likes": 9 } for tweet in allTweets ]
    data = {
        "response": tweet_list
    }
    return JsonResponse(data)

def tweet_create_view(request, *args, **kwargs):
    form  = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()

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