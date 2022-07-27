from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from home.models import *


# Create your views here.
@login_required
def profile(request):
    if request.method == 'GET':
        userid = request.user.id
        data = User.objects.get(id = userid)
        blogObj = Blog.objects.filter(userid = userid).order_by('-id')
        context = {
                "title": "Shareio | Home",
                "data": data,
                "blogs": blogObj
        }
        return render(request, "user/profile.html", context)


def login(request):
    if 'username' in request.session:
        return redirect('/')
    if request.method == "GET":
        context = {
                "title": "Shareio | Login"
        }
        return render(request, "user/login.html", context)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            request.session['username'] = username
            auth.login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'User Not Found!')
            return render(request, 'user/login.html', {'title': "Shareio Signin"})


def signup(request):
    if 'username' in request.session:
        return redirect('/')
    if request.method == "GET":
        context = {
                "title": "Shareio | Signup"
        }
        return render(request, "user/signup.html", context)
    if request.method == "POST":
        user = User.objects.create_user(
                first_name = request.POST.get('fullname'),
                username = request.POST.get('username'),
                email = request.POST.get('email'),
                password = request.POST.get('password1'))
        user.save()
        messages.success(request, 'User Created!')
        return redirect('/user/login')


@login_required
def signout(request):
    if 'username' in request.session:
        auth.logout(request)
        messages.success(request, 'User Logged Out!')
        return redirect('/user/login')


@login_required
def change_password(request, id):
    if request.method == "POST":
        data = User.objects.get(id = id)
        if data.check_password(request.POST.get('currentPass')):
            data.set_password(request.POST.get('newPass'))
            data.save()
            messages.success(request, 'Password Changed!')
            # messages.info("request", "password changed")
            # update_session_auth_hash(request, data)
            # print("password changed successfully")
            return redirect('/user/')
        else:
            # print("wrong pass")
            return redirect('/user/')
