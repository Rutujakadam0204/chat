from django.contrib import admin
from django.urls import path
from .views import Signup, SignIn, user_logout

urlpatterns = [
    path('', SignIn.as_view()),
    path('sign-up', Signup.as_view()),
    path('logout', user_logout)
]