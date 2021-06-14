from django.test import TestCase

from rest_framework.test import APIClient

from .models import Tweet
from django.contrib.auth.models import User

class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testUser", password="#lolta123#")
        self.user2 = User.objects.create_user(username="testUser2", password="#lolta123#")
        
        Tweet.objects.create(content="my first tweet", user=self.user)
        Tweet.objects.create(content="my 2nd tweet", user=self.user)
        Tweet.objects.create(content="my third tweet", user=self.user2)
        
        self.currentCount = Tweet.objects.all().count()


    def test_user_created(self):
        self.assertEqual(self.user.username, "testUser")
        # self.ass ert
    
    def test_tweet_created(self):
        tweet = Tweet.objects.create(content="my testing tweet", user=self.user)
        self.assertEqual(tweet.id, 4)
        self.assertEqual(tweet.user, self.user)
    
    def get_client(self):
        client = APIClient()
        client.login(username=self.user, password="#lolta123#")

        return client

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/api/tweets/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        
        # print(response)
        # print(response.json())
    def test_like_action(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/", {"id":1, "action": "like"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likes") , 1)

        user = self.user
        usr_likes_count = user.tweetlike_set.count()
        self.assertEqual(usr_likes_count, 1)
        
        #   = user.tweet_user.count()
        # self.assertEqual(usr_likes_count, 1)

 
    def test_unlike_action(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/", {"id":1, "action": "like"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likes") , 1)
        
        response = client.post("/api/tweets/action/", {"id":1, "action": "like"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("likes") , 0)

    def test_retweet_action(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/" , {"id":1, "action": "retweet"})
        self.assertEqual(response.status_code, 201)

        response2 = client.get("/api/tweets/")
        # print(response2.data, response2.status_code)

        self.assertEqual(len(response2.json()), self.currentCount + 1)       

    def test_create(self):
        client = self.get_client()
        response = client.post("/api/tweets/create/" , {"content": "retweet"})
        self.assertEqual(response.status_code, 201)

        response2 = client.get("/api/tweets/")
        # print(response2.data, response2.status_code)

        self.assertEqual(len(response2.json()), self.currentCount + 1)  

    def test_detail(self):
        client = self.get_client()
        response = client.get("/api/tweets/1/")

        self.assertEqual(response.status_code, 200)
        res = response.json()
        # print(res, res["content"])
        self.assertEqual(res["content"], "my first tweet")

    def test_delete(self):
        client = self.get_client()
        response = client.delete("/api/tweets/1/delete/")
        self.assertEqual(response.status_code, 200)

        # print(response.json())
        self.assertEqual(response.json()["message"], "Tweet has been deleted.")

        response = client.delete("/api/tweets/1/delete/")
        self.assertEqual(response.status_code, 404)

        response = client.delete("/api/tweets/3/delete/")
        self.assertEqual(response.status_code, 401)
    
    def test_tweet_created(self):
        user = self.user
        self.assertEqual(user.tweets.count(), 2)

