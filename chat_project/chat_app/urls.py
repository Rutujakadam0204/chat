# from django.urls import path
# from . views import ChatView
# from django.contrib.auth.decorators import login_required
#
# urlpatterns = [
#     path('my_chat', login_required(ChatView.as_view()))
# ]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]