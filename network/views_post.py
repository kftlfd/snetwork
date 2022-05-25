from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json

from .models import *


def post_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = post.post_comments.order_by('-id')
    return render(request, "network/post-page.html", {'post': post, 'comments': comments})


def post_add(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        u = request.user
        c = data.get('content', None)
        try:
            new_post = Post(user=u, content=c)
            new_post.save()
            return HttpResponse(
                render(request, "network/post.html", {'post': new_post, 'user': request.user}), 
                status=201)
        except:
            return HttpResponse(status=500)
    return HttpResponse(status=400)


def post_edit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        post_id = data.get('post', None)
        if not post_id:
            return HttpResponse(status=400)

        try:
            post = Post.objects.get(pk=post_id)
        except:
            return HttpResponse(status=404)

        if request.user != post.user:
            return HttpResponse(status=403)
            
        try:
            post.content = data.get('content', post.content)
            post.edited = True
            post.save()
            return HttpResponse(status=201)
        except:
            return HttpResponse(status=500)
    return HttpResponse(status=400)


def post_reaction(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)

        post_id = data.get('post', None)
        a = data.get('action', None)
        if not post_id or not a:
            return HttpResponse(status=400)
        
        try:
            post = Post.objects.get(pk=post_id)
        except:
            return HttpResponse(status=404)

        u = request.user
        r = post.post_reactions.filter(user=u)

        if not r and a == 'add':
            try:
                new_reaction = Reaction(user=u, post=post)
                new_reaction.save()
                return HttpResponse(status=201)
            except:
                return HttpResponse(status=500)

        elif r:
            try:
                reaction = r.all()
                reaction.delete()
                return HttpResponse(status=204)
            except:
                return HttpResponse(status=500)

    return HttpResponse(status=400)


def post_comment(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        u = request.user
        post_id = data.get('post')
        content = data.get('content')
        if not post_id or not content:
            return HttpResponse(status=400)

        try:
            post = Post.objects.get(pk=post_id)
        except:
            return HttpResponse(status=404)

        try:
            new_comment = Comment(user=u, post=post, content=content)
            new_comment.save()
            return HttpResponse(
                render(request, "network/comment.html", {'comment': new_comment}), 
                status=201)
        except:
            return HttpResponse(status=500)
    return HttpResponse(status=400)
