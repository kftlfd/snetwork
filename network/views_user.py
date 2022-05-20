from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Post


def user_view(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "network/user.html", {'u': user})

def user_feed(request):
    posts = Post.objects.filter(user__in=request.user.following.all()).order_by('-id')
    return render(request, "network/feed.html", {'posts': posts})

def user_follow(request, user_id):
    if request.method == 'POST':
        u = User.objects.get(pk=user_id)
        if request.POST['follow'] == 'true':
            request.user.following.add(u)
            request.user.save()
        elif request.POST['follow'] == 'false':
            request.user.following.remove(u)
            request.user.save()
    return HttpResponse(status=204)