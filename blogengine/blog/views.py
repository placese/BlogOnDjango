from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.urls import reverse

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q

def posts_list(request):
	search_query = request.GET.get('search', '')

	if search_query:
		posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
	else:
		posts = Post.objects.all()

	paginator = Paginator(posts, 3)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	return render(request, 'blog/index.html', context={'page_object': page, 'search_query': search_query})


class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	model_form = PostForm
	template = 'blog/post_create_form.html'
	raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Post
	model_form = PostForm
	template = 'blog/post_update_form.html'
	raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Post
	template = 'blog/post_delete_form.html'
	redirect_url = 'posts_list_url'
	raise_exception = True


def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	model_form = TagForm
	template = 'blog/tag_create.html'
	raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Tag
	model_form = TagForm
	template = 'blog/tag_update_form.html'
	raise_exception = True


class TagDelete(ObjectDeleteMixin, View):
	model = Tag
	template = 'blog/tag_delete_form.html'
	redirect_url = 'tags_list_url'
	raise_exception = True
