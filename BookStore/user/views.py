from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm , SignUpForm


def user_login(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return redirect("BookStore:home-index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "accounts/login.html", {"form": form})
        return redirect("BookStore:home-index")
    else:
        return render(request, "accounts/login.html" , {"form": form})



def user_logout(request):
    logout(request)
    return redirect("login")

def user_signup(request):
    form = SignUpForm()
    if request.method == "POST":
        pass
    else:
        return render(request, "accounts/signup.html" , {"form": form})