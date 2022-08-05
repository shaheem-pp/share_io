from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    short = models.CharField(max_length = 350)
    description = models.CharField(max_length = 10000)
    name = models.CharField(max_length = 10000)
    image = models.ImageField(default = "dummy-image.jpeg")
    date = models.DateTimeField()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Blog, on_delete = models.CASCADE)
