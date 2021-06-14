from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User 

from rest_framework.test import APIClient


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testUser", password="#lolta123#")
        self.user2 = User.objects.create_user(username="testUser2", password="#lolta123#")
#         # Tweet.objects.create(content= "my first tweet", user=self.user)
#         # Tweet.objects.create(content="my 2nd tweet", user=self.user)
#         # Tweet.objects.create(content="my third tweet", user=self.user2)  
#         # self.currentCount = Tweet.objects.all().count()

    def test_profile_created(self):
        self.assertEqual(Profile.objects.count() , 2)

    def test_following(self):
        first = self.user
        second = self.user2
        self.assertEqual( second.following.count() , 0)
        first.profile.followers.add(second)
        self.assertEqual( second.following.count() , 1)
        self.assertEqual( first.following.count() , 0)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user, password="#lolta123#")
        return client

    def test_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(f"/api/profile/{ self.user2.username }/follow/", {
            "action": "follow"
        })
        
        data = response.json()
        count = data.get("followers")

        # print(data, response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(count, 1)

    def test_follow_sameuser_api_endpoint(self):
        client = self.get_client()
        response = client.post(f"/api/profile/{ self.user.username }/follow/", {
            "action": "follow"
        })
        
        data = response.json()
        count = data.get("followers")

        # print(data, response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(count, 1)

    def test_unfollow_api_endpoint(self):

        self.user.profile.followers.add(self.user2)
        
        client = self.get_client()        
        response = client.post(f"/api/profile/{ self.user2.username }/follow/", {
            "action": "unfollow"
        })
        
        data = response.json()
        count = data.get("followers")

        # print(data, response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(count, 0)  