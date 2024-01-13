from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response

from . models import RoomNames, MessageHistory
from chat_auth.models import Profile

def index(request):
    data = {'users':Profile.objects.all().exclude(user=request.user)}
    return render(request, "chat/index.html", data)

def room(request, pk):
    if User.objects.filter(id=pk).exists():
        other_user = User.objects.get(id=pk)
        if RoomNames.objects.filter(Q(my_user=request.user, other_user=other_user) | Q(my_user=other_user, other_user=request.user)):
            room_name = RoomNames.objects.get(Q(my_user=request.user, other_user=other_user) | Q(my_user=other_user, other_user=request.user)).group_name
        else:
            room_name = RoomNames.objects.create(my_user=request.user, other_user=other_user, group_name=str(pk)+str(request.user.id))
            room_name = room_name.group_name
        history = MessageHistory.objects.filter(room__group_name=room_name)
        return render(request, "chat/room.html", {"room_name": room_name, 'history':history})
    else:
        return redirect('index')