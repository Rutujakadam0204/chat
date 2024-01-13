from django.contrib import admin
from django.urls import path
from .views import Signup, SignIn, user_logout
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', SignIn.as_view()),
    path('sign-up', Signup.as_view()),
    path('logout', login_required(user_logout))
]