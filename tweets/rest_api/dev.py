from rest_framework import authentication
from django.contrib.auth.models import User

class DevAuthentication(authentication.BasicAuthentication):

    def authenticate(self, request):
        print("lol i am here", request.data)
        qs = User.objects.all()
        user = qs.order_by("?").first()
        return (user ,None)