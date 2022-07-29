from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
        path('', views.index, name = "index"),
        path('new_blog/', views.new_blog, name = "new_blog"),
        path('read_blog/<int:id>', views.read_blog, name = "read_blog"),
        path('edit_blog/<int:id>', views.edit_blog, name = "edit_blog"),
        path('delete_blog/<int:id>', views.delete_blog, name = "delete_blog"),
        path('search/', views.search, name = "search"),
        path('liked/', views.like_unlike_post, name = 'like-post-view'),
]
