from django.db import models
import random
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE   )
    content = models.TextField(blank=True, null=True)  

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.content
         
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0,200)
        }