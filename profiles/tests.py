from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User 



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
