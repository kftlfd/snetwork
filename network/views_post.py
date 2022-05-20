from django.shortcuts import render
from .models import *


def post_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "network/post-page.html", {'post': post})
