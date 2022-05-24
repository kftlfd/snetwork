
from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("post/<int:post_id>", views.post_view, name="post_view"),
    path("post/add", views.post_add, name="post_add"),
    path("post/edit", views.post_edit, name="post_edit"),
    path("post/reaction", views.post_reaction, name="post_reaction"),
    path("post/comment", views.post_comment, name="post_comment"),

    path("user/<int:user_id>", views.user_view, name="user_view"),
    path("user/follow", views.user_follow, name="user_follow"),
    path("feed", views.user_feed, name="user_feed"),
    
    re_path(r'^spa/.*', views.spa, name="spa")
]
