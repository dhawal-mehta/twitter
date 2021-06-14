from django.shortcuts import render, redirect
import json

from ..models import Profile
from django.contrib.auth.models import User

# from ..serializers import TweetSerializer, TweetActionSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


@api_view(['POST'])
# @authentic  ation_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def user_follow_view(request, username, *args, **kwargs):
    current_user = request.user
    other_user_qs =  User.objects.filter(username=username)
    
    if not other_user_qs.exists():
        return Response({}, status=404)

    profile = other_user_qs.first().profile  

    if username == current_user:
        return Response({"followers": profile.followers.count() }, status=200)

    data = request.data or {}
      
    action = data.get("action")

    # print( action, current_user,  username, profile )

    if action == "unfollow":
        profile.followers.remove(current_user)
        # print("test!!!")
    elif action == "follow":
        profile.followers.add(current_user)

    return Response({"followers": profile.followers.count() }, status=200)


# @api_view(['GET'])
# # @authentic  ation_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def user_profile_get_view(request, *args, **kwargs):
#     current_user = request.user
#     to_follow_user = 
#     return Response({}, status=200)
