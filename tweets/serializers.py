from rest_framework import serializers
from django.conf import settings
from .models import Tweet
from django.utils import timezone

from profiles.serializers import PublicProfileSerializer

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH

class TweetCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    
    class Meta:
        model = Tweet
        fields = ['user','id', 'content','likes', 'parent', 'timestamp']

    def get_likes(self, obj):
        # print()
        return obj.likes.count()


class TweetSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(read_only=True)
    # modified =  serializers.HiddenField(default=timezone.now)
   
    # parent = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ['user','id', 'content','likes', 'parent', 'timestamp']




    # def get_parent(self, obj):
    #     # print(obj, "in the porche")
    #     parentData = None

    #     if obj.parent:
    #         parentData =  {'id':obj.parent.id, 'content':obj.parent.content, 'likes':obj.parent.likes }
        
    #     return parentData 


    def get_likes(self, obj):
        # print()
        return obj.likes.count()


    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long.")
        return value

# class TweetLikeSerializer(serializers.ModelSerializer):
#     likes = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Tweet
#         fields = ['id', 'content','user', 'likes']

#     def get_likes(self, obj):
#         return obj.likes.count()


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    # def get_content(self, obj):
    #     return obj.content if not obj.parent else obj.parent.content

    def validate_action(self, value):
        if value in settings.TWEET_ACTIONS:
           return value

        return serializers.ValidationError("Action is not valid.")