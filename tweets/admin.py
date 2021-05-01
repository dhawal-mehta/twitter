from django.contrib import admin

# Register your models here.
from .models import Tweet
# admin.site.register(Tweet)

class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['user__username', 'user__email']
    class Meta:
        model = Tweet

admin.site.register(Tweet, TweetAdmin)
# admin.site.register()

