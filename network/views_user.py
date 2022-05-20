from django.shortcuts import render
from .models import User, Post


def user_view(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "network/user.html", {'user': user})

def user_feed(request):
    posts = Post.objects.filter(user__in=request.user.following.all()).order_by('-id')
    return render(request, "network/feed.html", {'posts': posts})
