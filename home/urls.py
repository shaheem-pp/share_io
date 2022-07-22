"""ExploreBikes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('Blog/', include('Blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new_blog/', views.new_blog, name="new_blog"),
    path('liked/<int:id>', views.liked),
    path('read_blog/<int:id>', views.read_blog, name="read_blog"),
    path('edit_blog/<int:id>', views.edit_blog, name="edit_blog"),
    path('delete_blog/<int:id>', views.delete_blog, name="delete_blog"),
    path('like/<int:pk>', views.liked, name="like_post"),
    path('search/', views.search, name="search")
]
