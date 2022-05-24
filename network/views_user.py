from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
import json

from .apps import NetworkConfig
from .models import User, Post


def user_view(request, user_id):
    user = User.objects.get(pk=user_id)
    posts = user.user_posts.all().order_by('-id')
    p = Paginator(posts, NetworkConfig.PAGINATION)
    page = p.page(request.GET.get('page', 1))
    
    context = {
        'u': user, 
        'posts': page}
    if page.has_other_pages():
        context['page'] = page
    return render(request, "network/user.html", context)


def user_feed(request):
    posts = Post.objects.filter(user__in=request.user.following.all()).order_by('-id')
    p = Paginator(posts, NetworkConfig.PAGINATION)
    page = p.page(request.GET.get('page', 1))

    context = {
        'posts': page}
    if page.has_other_pages():
        context['page'] = page
    return render(request, "network/feed.html", context)


def user_follow(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        follow = data.get('user')
        try:
            u = User.objects.get(pk=follow)
        except:
            return HttpResponse(status=404)
        if data.get('follow') == 'true':
            try:
                request.user.following.add(u)
                request.user.save()
                return HttpResponse(status=201)
            except:
                return HttpResponse(status=500)
        elif data.get('follow') == 'false':
            try:
                request.user.following.remove(u)
                request.user.save()
                return HttpResponse(status=201)
            except:
                return HttpResponse(status=500)
    return HttpResponse(status=400)
