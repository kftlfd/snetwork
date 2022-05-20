from django.shortcuts import render

from .models import *
from .views_auth import *
from .views_api import *
from .views_user import *
from .views_post import *


def index(request):
    posts = Post.objects.all().order_by('-id')

    context = {
        'posts': posts, 
    }
    return render(request, "network/index.html", context)
