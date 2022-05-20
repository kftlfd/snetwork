from django.shortcuts import render

from .models import *
from .views_auth import *
from .views_api import *
from .views_user import *


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts, 
    }
    return render(request, "network/index.html", context)

def post_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "network/post.html", {'post': post})
