
from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("post/<int:post_id>", views.post_view, name="post_view"),
    path("user/<int:user_id>", views.user_view, name="user_view"),
    path("feed", views.user_feed, name="user_feed"),
    path("follow/<int:user_id>", views.user_follow, name="user_follow"),

    path("add-post", views.api_add_post, name="add-post"),
    path("add-reaction", views.api_add_reaction, name="add-reaction"),
    path("add-comment", views.api_add_comment, name="add-comment"),
    path("spa/post/<int:post_id>", views.api_post, name="api-post"),
    
    re_path(r'^spa.*', views.spa, name="spa")
]
