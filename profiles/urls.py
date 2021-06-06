from django.contrib import admin
from django.urls import path
from . import views as profileViews

urlpatterns = [
    path('edit/', profileViews.profile_update_view),   
    path('<str:username>/', profileViews.profile_view),
]
