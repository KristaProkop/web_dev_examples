from __future__ import unicode_literals
from django.db import models
from ..login.models import User
import tweepy
from tweepy import OAuthHandler
from cryptography.fernet import Fernet

class AppOwnerManager(models.Manager):

    def authenticate(request, id):
        user = User.objects.get(id=id)
        owner = AppOwner.objects.get(user=user)
        auth = tweepy.OAuthHandler(owner.consumer_key, owner.consumer_secret)
        auth.set_access_token(owner.access_token, owner.access_token_secret)
        api = tweepy.API(auth)
        return api


    def create_owner(request, id, postData):
        consumer_key = postData['consumer_key']
        consumer_secret = postData['consumer_secret']
        access_token = postData['access_token']
        access_token_secret = postData['access_token_secret']
        user = User.objects.get(id=id)
        owner = AppOwner.objects.create(user=user, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)


class TweeterManager(models.Manager):
    def generate_key(request, id):
        key = Fernet.generate_key()
        user = User.objects.get(id=id)
        tweeter = Tweeter.objects.create(user=user, key=key)
        message = "Encryption Key successfully generated"
        return key, message


    def get_decrypt_key(request, api, tweet_id):
        tweet = api.get_status(tweet_id)
        search_string = str(tweet.text)
        handle = tweet.user.screen_name
        tweeter = Tweeter.objects.get(user__handle=handle)
        key = tweeter.key
        return key, search_string, tweet
        

class Tweeter(models.Model):
    user = models.OneToOneField(User)
    key = models.TextField()
    objects = TweeterManager()

class AppOwner(models.Model):
    user = models.OneToOneField(User)
    consumer_key = models.TextField()
    consumer_secret = models.TextField()
    access_token = models.TextField()
    access_token_secret = models.TextField()
    objects = AppOwnerManager()

