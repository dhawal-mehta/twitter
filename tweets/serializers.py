from rest_framework import serializers
from django.conf import settings
from .models import Tweet

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH

class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'content','likes']

    def get_likes(self, obj):
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
    # likes = serializers.IntegerField()
    content = serializers.CharField(allow_blank=True, required=False)

    # def get_content(self, obj):
    #     return obj.content if not obj.parent else obj.parent.content

    def validate_action(self, value):
        if value in settings.TWEET_ACTIONS:
           return value

        return serializers.ValidationError("Action is not valid.")