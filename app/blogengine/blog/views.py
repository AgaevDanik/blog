from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import View

from .utils import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    template = 'blog/post_detail.html'
    model = Post


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    template = 'blog/tag_detail.html'
    model = Tag
