from django.db import models
import random
from django.contrib.auth.models import User
# Create your models here.

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='tweets'  )
    content = models.TextField(blank=True, null=True)  
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike  )
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-id"]
    
    @property
    def is_retweet(self):
        return self.parent != None


    # def __str__(self):
    #     return self.content
    

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "content": self.content,
    #         "likes": random.randint(0,200)
    #     }