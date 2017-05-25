from __future__ import unicode_literals

from django.db import models

from ..friends.models import User


class Message(models.Model):
    wall = models.ForeignKey(User, related_name='user_wall')
    user = models.ForeignKey(User, related_name='sender')
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User)
    message = models.ForeignKey(Message)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)