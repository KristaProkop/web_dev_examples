# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class FriendshipManager(models.Manager):
    def addFriend(self, user_id, friend_id):
        user = User.objects.get(pk=user_id)
        friend = User.objects.get(pk=friend_id)
        Friendship.objects.create(user=user, friend=friend)
        Friendship.objects.create(user=friend, friend=user)

    def removeFriend(self, user_id, friend_id):
        user = User.objects.get(pk=user_id)
        friend = User.objects.get(pk=friend_id)
        friendship1 = Friendship.objects.get(user=user, friend=friend)
        friendship2 = Friendship.objects.get(user=friend, friend=user)
        friendship1.delete()
        friendship2.delete()


class Friendship(models.Model):
    user = models.ForeignKey(User, related_name='requester')
    friend = models.ForeignKey(User, related_name='accepter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FriendshipManager()


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    birthday = models.DateField(blank=True)
    photo = models.ImageField(upload_to='images/profiles/')


