from django.core.paginator import Paginator
from django.shortcuts import render

from .apps import NetworkConfig
from .models import *
from .views_auth import *
from .views_api import *
from .views_user import *
from .views_post import *


def index(request):
    posts = Post.objects.all().order_by('-id')
    p = Paginator(posts, NetworkConfig.PAGINATION)
    page = p.page(request.GET.get('page', 1))

    context = {
        'posts': page}
    if page.has_other_pages():
        context['page'] = page
    return render(request, "network/index.html", context)

def spa(request):
    return render(request, "network/react.html")