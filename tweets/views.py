from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
from .models import Tweet

from .forms import TweetForm
from .serializers import TweetSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# def tweet_list_view_pure_django(request, *args, **kwargs):
#     allTweets = Tweet.objects.all()
#     tweet_list = [ tweet.serialize() for tweet in allTweets ]
#     data = {
#         "response": tweet_list
#     }
#     return JsonResponse(data)

# def tweet_create_view_pure_django(request, *args, **kwargs):
#     # print("ajax", request.is_ajax())
#     if not request.user.is_authenticated:
#         # print("not logged in")
#         if request.is_ajax():
#             return JsonResponse({}, status=401)
#         # have to redirect to login route
#         return redirect("/")

#     form  = TweetForm(request.POST or None)
#     # print("post data is", request.POST)
    
#     next_url = request.POST.get("n ext") or None
#     # print("next_url", next_url)
    # if form.is_valid():
    #     obj = form.save(commit=False)
    #     obj.user = request.user
    #     obj.save()
    #     # if next_url != None :
        
    #     if request.is_ajax():
    #         return JsonResponse(obj.serialize(), status=201)

    #     if next_url != None and is_safe_url(next_url, settings.ALLOWED_HOSTS):
    #         return redirect(next_url)   
             
    #     form = TweetForm()
    # else:

    #     if request.is_ajax():
    #         return JsonResponse(form.errors, status=400)

    # # if form.errors:
    # #     if

    # return render(request, 'components/form.html', context={"form":form})

# def home_detail_view_pure_django(request, id, *args, **kwargs):
#     data = {
#         "id": id,
#     }

#     status=200
#     try:
#         obj = Tweet.objects.get(id=id)
#         data["content"] = obj.content
#     except:
#         data['message'] = "Not found"
#         status = 404

#     return JsonResponse(data, status=status)

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    allTweets = Tweet.objects.all()
    serializer = TweetSerializer(allTweets, many=True)

    return Response(serializer.data)

@api_view(['GET'])  
def home_detail_view(request, id, *args, **kwargs):
    tweet = Tweet.objects.filter(id=id)

    if not tweet.exists():
        return Response({}, status=404)
   
    serializer = TweetSerializer(tweet.first())
    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    data = request.POST 
    serializer = TweetSerializer(data=data)
      
    if serializer.is_valid(raise_exception=True):
        obj = serializer.save(user=request.user)
        return Response(serializer.data, status=201)

    return Response({}, status=400)


def home_view(request, *args, **kwargs):
    return render(request, 'tweets/index.html', context={}, status=200)
