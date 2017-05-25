from __future__ import unicode_literals

from django.db import models
from ..loginReg.models import User, UserManager

class MessageManager(models.Manager):
    def create_message(request, user_id, creator_id, postData):
        user_for = User.objects.get(id=user_id)
        creator = User.objects.get(id=creator_id)
        new_message = Message.objects.create(message=postData['message'], creator=creator)
        new_message.user_for.add(user_for)
        new_message.save()
        return True

class CommentManager(models.Manager):
    def create_comment(request, user_id, message_id, postData):
        user = User.objects.get(id=user_id)
        message = Message.objects.get(id=message_id)
        comment = Comment.objects.create(comment=postData['comment'], message=message, user=user)
        return True


class Message(models.Model):
    creator = models.ForeignKey(User, related_name="messages")
    user_for = models.ManyToManyField(User)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = MessageManager()


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User, related_name="comments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CommentManager()



