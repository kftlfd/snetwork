from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
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
