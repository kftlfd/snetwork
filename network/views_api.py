from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from .models import *
import json


def api_get_posts(request):
    posts = Post.objects.all()
    posts = json.dumps(posts)
    return JsonResponse(posts)


def api_add_post(request):
    if request.method == 'POST':
        u = request.user
        c = request.POST['content']
        new_post = Post(user=u, content=c)
        new_post.save()
    return HttpResponse(status=204)


def api_add_reaction(request):
    if request.method == 'POST':
        u = request.user
        p = Post.objects.get(pk=request.POST['post'])
        t = request.POST['type']
        a = request.POST['action']
        if a == 'add':
            new_reaction = Reaction(user=u, post=p, type=t)
            new_reaction.save()
        if a == 'remove':
            reaction = Reaction.objects.filter(user=u, post=p).first()
            reaction.delete()
    # return HttpResponse(status=204)
    return redirect('post_view', post_id=p.id)


def api_add_comment(request):
    if request.method == 'POST':
        u = request.user
        p = Post.objects.get(pk=request.POST['post'])
        c = request.POST['content']
        new_comment = Comment(user=u, post=p, content=c)
        new_comment.save()
    return HttpResponse(status=204)
