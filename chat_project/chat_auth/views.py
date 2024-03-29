from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.views import APIView
from rest_framework.response import Response

from . models import Profile, Interest
from . serializers import SignUpSerializer, ProfileSerializer

"""
Signup
Enter email address and it will be checked in sign up view, whether it is present or not.
If present then display message for same, if not then save data to database.
"""
class Signup(APIView):
    def post(self, request):
        if User.objects.filter(email=request.data['email']).exists():
            messages.error(request, 'User already present')
        else:
            user_signup = SignUpSerializer(data=request.data)
            if user_signup.is_valid():
                user_signup.save(username=request.data['email'], password=make_password(request.data['password']))
                user = User.objects.get(username=request.data['email'])
                profile = ProfileSerializer(data=request.data)

                if profile.is_valid():
                    profile.save(user=user)
                messages.success(request, 'You have signed up successfully !!!')

            else:
                messages.error(request, 'Please enter data correctly !!')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class SignIn(APIView):
    def get(self, request):
        data = {'interest': Interest.objects.all()}
        return render(request, 'login_signup.html', data)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            verify_password = check_password(password, user.password)
            print(verify_password)
            if verify_password:
                login(request, user)
                Profile.objects.filter(user=request.user).update(is_online=True)
                return redirect('/chat/')
            else:
                messages.error(request, 'Password is wrong')
        else:
            messages.error(request, 'This email is not registered with us.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


def user_logout(request):
    Profile.objects.filter(user=request.user).update(is_online=False)
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('/')