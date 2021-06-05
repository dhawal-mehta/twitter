from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")

    context = {'form': form,
        'btn_label': "Login",
        'title': "Login"}

    return render(request, "accounts/login.html", context)


def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/account/login/")

    context = {'form': None,
        'btn_label': "Are you Sure",
        'title': "Logout"}
    
    return render(request, "accounts/logout.html" , context)


def register_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True) 
        # we can send confirmation email here
        login(request, user)
        
        return redirect("/account/login/")

    context = {'form': form,
        'btn_label': "Sign Up",
        'title': "Take me in"}
    return render(request, "accounts/register.html", context)
