from django.contrib import admin
from django.urls import path
from . import views as profileViews

urlpatterns = [
       
    path('<str:username>/', profileViews.profile_view),

]
