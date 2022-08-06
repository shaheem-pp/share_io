import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from home.models import *
from datetime import datetime
from django.contrib.postgres.search import SearchVector


# Create your views here.
@login_required
def index(request):
    if request.method == "GET":
        data = request.user.id
        blogs = Blog.objects.all().order_by('-date')
        likes = Like.objects.all()
        for blog in blogs:
            blog.liked_count = 0
            blog.is_liked = False
            for like in likes:
                if blog.id == like.post_id:
                    blog.liked_count += 1
                    # blog.liked_count = Like.objects.filter(post_id = blog.id).count()
                    # blog.is_liked = Like.objects.filter(user = request.user, post_id = blog.id).exists()
        title = {
                "title": "Shareio | Home",
                "data": data,
                "blogs": blogs,
        }
        return render(request, "home/index.html", title)
    return redirect('/user/login')


@login_required
def new_blog(request):
    if request.method == "GET":
        title = {
                "title": "Shareio | Home",
        }
        return render(request, "home/new_blog.html", title)
    if request.method == "POST":
        blogObj = Blog()
        blogObj.userid = request.user
        blogObj.title = request.POST.get('title')
        blogObj.short = request.POST.get('short')
        blogObj.description = request.POST.get('blogcontent')
        blogObj.image = request.FILES.get('imagelink')
        blogObj.name = request.user.get_full_name()
        blogObj.date = datetime.now()
        blogObj.save()
        return redirect('/')


@login_required
def like(request):
    user = request.user
    id = request.POST.get("blogId", None)
    if Like.objects.filter(user = user, post_id = id).exists():
        Like.objects.get(user = user, post_id = id).delete()
        liked = False
    else:
        Like.objects.create(user = user, post_id = id)
        liked = True
    like_count = Like.objects.filter(post_id = id).count()
    ctx = {
            "liked": liked,
            "like_count": like_count
    }
    return JsonResponse(ctx, safe = False)


@login_required
def read_blog(request, id):
    blog = Blog.objects.get(id = id)
    context = {
            "blog": blog,
            "title": "Shareio | " + blog.title,
            "profile": User.objects.get(username = request.user),
            "like_count": Like.objects.filter(post_id = id).count(),
            "is_liked": Like.objects.filter(user = request.user, post_id = blog.id).exists(),
    }
    return render(request, "home/read_blog.html", context)


@login_required
def edit_blog(request, id):
    if request.method == "GET":
        blog = Blog.objects.get(id = id)
        context = {
                "title": "Edit Blog | " + blog.title,
                "blog": blog
        }
        return render(request, "home/edit_blog.html", context)
    if request.method == "POST":
        blog = Blog.objects.get(id = id)
        blog.title = request.POST.get('title')
        blog.short = request.POST.get('short')
        blog.description = request.POST.get('blogcontent')
        blog.image = request.POST.get('imagelink')
        blog.save()
        return redirect('home:read_blog', id = id)


@login_required
def delete_blog(request, id):
    blog = Blog.objects.get(id = id)
    blog.delete()
    return redirect('/user/')


def search(request):
    if request.GET['keyword'] == "":
        return redirect('login')
    else:
        blogs = Blog.objects.annotate(search = SearchVector('description', 'short', 'name', 'title',
                                                            'userid', 'userid__first_name')).filter(
                search = request.GET['keyword'])
        return render(request, "home/index.html", {"blogs": blogs})
