from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.user.is_authenticated:
        return redirect("BookStore:home-index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "auth/login.html", messages)
        return redirect("BookStore:home-index")
    else:
        return render(request, "auth/login.html")



def user_logout(request):
    pass

def user_signup(request):
    pass