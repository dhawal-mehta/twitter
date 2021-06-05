from django.shortcuts import render

def profile_view(request, username ,*args, **kwargs):
    context = {"username": username, "title": "Profile"}
    return render(request, 'profiles/profile.html', context)
