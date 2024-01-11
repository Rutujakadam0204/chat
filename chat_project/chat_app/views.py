from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from rest_framework.views import APIView
from rest_framework.response import Response

from . models import RoomNames

# Create your views here.
class ChatView(APIView):
    def get(self, request):
        data = {'users':User.objects.all()}
        return render(request, 'chat_screen.html',data)

# chat/views.py
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})