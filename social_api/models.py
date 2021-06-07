from datetime import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    votes = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='blog_post')


    def __str__(self):
        return self.title

