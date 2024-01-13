# from django.urls import path
# from . views import ChatView
# from django.contrib.auth.decorators import login_required
#
# urlpatterns = [
#     path('my_chat', login_required(ChatView.as_view()))
# ]

from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("", login_required(views.index), name="index"),
    path("<int:pk>/", login_required(views.room), name="room"),
]