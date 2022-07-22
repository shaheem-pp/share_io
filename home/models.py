from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    short = models.CharField(max_length=350)
    description = models.CharField(max_length=10000)
    name = models.CharField(max_length=10000)
    image = models.CharField(max_length=1000)
    date = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name="blog_post")

    def total_likes(self):
        return self.likes.count()
