from django.shortcuts import get_object_or_404, render
from .models import *
from django.http import Http404
# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except:
#         raise Http404('No Post found')
#     return render(request, 'blog/post/detail.html')

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day)
    return render(request, 'blog/post/detail.html', {'post': post})