from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    following = models.ManyToManyField('User', symmetrical=False, related_name='followers')


class Post(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_posts')
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=timezone.now())
    edited = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=timezone.now())


class Reaction(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_reactions')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_reactions')
    type = models.IntegerField() # for future multiple reactions


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_comments')
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=timezone.now())
