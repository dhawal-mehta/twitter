from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)


def  user_did_save(sender, instance, created, *args, **kwargs):
    Profile.objects.get_or_create(user=instance)

post_save.connect(user_did_save, sender=User)