from django.contrib.auth.decorators import login_required
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
        title = {
                "title": "Shareio | Home",
                "data": data,
                "blogs": blogs

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
        blogObj.image = request.POST.get('imagelink')
        blogObj.name = request.user.get_full_name()
        blogObj.date = datetime.now()
        # x = datetime.datetime.now()
        # blogObj.date = x.strftime("%d %B %Y")
        blogObj.save()
        return redirect('/')


@login_required
def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Blog.objects.get(id = post_id)
        profile = User.objects.get(username = user)
        if profile in post_obj.likes.all():
            post_obj.likes.remove(profile)
        else:
            post_obj.likes.add(profile)
        like, created = Like.objects.get_or_create(user = profile, post_id = post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'
            post_obj.save()
            like.save()
    return redirect('home:index')


@login_required
def read_blog(request, id):
    blog = Blog.objects.get(id = id)
    blog_likes = blog.total_likes()
    context = {
            "blog": blog,
            "title": "Shareio | " + blog.title,
            "blog_likes": blog_likes,
            "profile": User.objects.get(username = request.user)
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
