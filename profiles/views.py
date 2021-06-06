from django.shortcuts import render, redirect
from django.http import Http404
from .forms import ProfileForm
from .models import Profile

def profile_update_view(request, *args, **kwargs):
    # print(request.POST)

    if not request.user.is_authenticated:
        return redirect("/account/login/")
     
    user = request.user
    user_profile = request.user.profile
    user_data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "location": user_profile.location,
        "bio": user_profile.bio 
    }
    form = ProfileForm(request.POST or None , instance=user_profile, initial=user_data)

    if form.is_valid():
        
        profile_obj = form.save(commit=False)
        
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        
        user.save() 
        profile_obj.save()

        redirect("/")

    context = {
        "form": form,
        "btn_label": "Update",
        "title": "Update Profile" }

    return render(request, 'profiles/profileupdate.html', context)
    

def profile_view(request, username ,*args, **kwargs):
    qs = Profile.objects.filter(user__username=username)
    
    if not qs.exists():
        raise Http404
    
    profile_obj = qs.first()
    context = {"username": username, "profile": profile_obj, "title": "Profile"}
    return render(request, 'profiles/profile.html', context)
