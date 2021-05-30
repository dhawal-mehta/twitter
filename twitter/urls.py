"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from tweets import views as tweetsViews
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tweetsViews.home_view),
    path('react/', TemplateView.as_view( template_name='tweets/react_dj.html') ),
    path('tweets/', tweetsViews.tweet_list_view),
    path('tweets/<int:id>/', tweetsViews.home_detail_view),
    path('create/', tweetsViews.tweet_create_view),
    # path('api/tweets/<int:id>/delete/', tweetsViews.tweet_delete_view),
    # path('api/tweets/action/', tweetsViews.tweet_action_view),
    path('api/tweets/', include('tweets.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
