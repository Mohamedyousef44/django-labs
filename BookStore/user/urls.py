from django.urls import path
from . import views

app_name = "BookStore"

urlpatterns = [
    path("login" , views.user_login , name="user-login"),
    path("logout" , views.user_logout , name="user-logout"),
    path("signup" , views.user_signup , name="user-signup"),
]