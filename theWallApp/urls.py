from django.urls import path, include
from . import views

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login',views.login),
    path('logout', views.logout),
    path('wall', views.viewWall),
    path('addMessage', views.addMessage),
    path('likeMessage/<int:messageID>', views.likeMessage),
    path('dislikeMessage/<int:messageID>', views.dislikeMessage),
    path('deleteMessage/<int:messageID>', views.deleteMessage),
    path('addComment/<int:messageID>', views.addComment)
]