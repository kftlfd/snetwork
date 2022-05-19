from django.shortcuts import render

from .models import *
from .views_auth import *
from .views_api import *


def index(request):
    posts = Post.objects.all()
    # jposts = [p.json() for p in Post.objects.all()]

    context = {
        'posts': posts, 
        # 'jposts': jposts
    }
    return render(request, "network/index.html", context)
