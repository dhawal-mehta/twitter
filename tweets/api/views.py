from django.shortcuts import render, redirect
import json

from ..models import Tweet

from ..forms import TweetForm
from ..serializers import TweetSerializer, TweetActionSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    paginator = PageNumberPagination()
    paginator.page_size = 20

    allTweets = Tweet.objects.all()
    username = request.GET.get('username')  
    if username != None:
        allTweets = allTweets.filter(user__username=username) 

    paginated_qs = paginator.paginate_queryset(allTweets, request)

    # print(allTweets)
    serializer = TweetSerializer(paginated_qs, many=True)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])  
def home_detail_view(request, id, *args, **kwargs):
    tweet = Tweet.objects.filter(id=id)

    if not tweet.exists():
        return Response({}, status=404)
   
    serializer = TweetSerializer(tweet.first())
    return Response(serializer.data, status=200)

@api_view(['POST'])
# @authentic  ation_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    data = request.data
    
    # print(data)
    
    serializer = TweetSerializer(data=data)
       
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)

    return Response({}, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  
def tweet_delete_view(request, id, *args, **kwargs):
    tweet = Tweet.objects.filter(id=id)

    if not tweet.exists():
        return Response({}, status=404)
    
    tweet = tweet.filter(user=request.user)
    if not tweet.exists():
        return Response({}, status=401)
    
    obj = tweet.first()
    obj.delete()
 
    return Response({"message": "Tweet has been deleted."}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def tweet_action_view(request, *args, **kwargs):
    # print(request.data)

    serializer = TweetActionSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # print(serializer , "data")
        data = serializer.validated_data
        # print(data , "data")
        id = data.get("id")
        action = data.get("action")
        content = Tweet.objects.get(id=id).content
        
        # print( content )
        # content = data.get("content")

        tweet = Tweet.objects.get(id=id)
        if not tweet:
            return Response({}, status=404)

        if action == "like":
            
            # print("likes are here", TweetLikeSerialize(tweet) )
            tweetSerializer = TweetSerializer(tweet)
            if request.user in tweet.likes.all():
                tweet.likes.remove( request.user )
            else:
                tweet.likes.add(request.user)
                # print(serializer.data )
            
            return Response(tweetSerializer.data, status=200)
          
        
        elif action == "retweet":
            print("retweeting", content)
            new_tweet = Tweet.objects.create(user=request.user, parent=tweet,content=content)
            serializer = TweetSerializer( new_tweet )

            # print(serializer.data)
            return Response(serializer.data, status=201)

    return Response({}, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def tweet_feed_view(request, *args, **kwargs):
    paginator = PageNumberPagination()
    paginator.page_size = 2

    user = request.user
    allTweets = Tweet.objects.feed(user)
    
    
    paginated_qs = paginator.paginate_queryset(allTweets, request)

    # print(allTweets)
    serializer = TweetSerializer(paginated_qs, many=True)

    return paginator.get_paginated_response(serializer.data)