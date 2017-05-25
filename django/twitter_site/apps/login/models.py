from __future__ import unicode_literals
import re
from django.db import models
import bcrypt



class UserManager(models.Manager):        

    def validate(self, postData):
        try: 
            User.objects.get(handle=postData['handle']) 
            response = "User already exists. Please log in instead."
        except: 
            if postData['password1'] != postData['password2']:
                response = ("Passwords must match")
            elif len(postData['password1']) < 8:
                response = ("Password must be 8 or more characters")
            elif len(postData['handle']) < 1:
                response = ("Invalid handle!")
            else:
                hashed = bcrypt.hashpw(postData['password1'].encode('utf-8'), bcrypt.gensalt())
                user = User.objects.create(handle=postData['handle'], password=hashed)
                response = ("Successfully registered. Please log in.")
                return True, response
        return False, response

    def login(self, postData):
        try: 
            handle = str(postData['handle'])
            password = str(postData['password'])
            user = User.objects.get(handle=handle)
            userPwBytes = password.encode('utf-8')
            hashedPwBytes = user.password.encode('utf-8')
            if hashedPwBytes == (bcrypt.hashpw(userPwBytes, hashedPwBytes)):
                return True, user
            else:
                response = "Handle and password don't match."
                return False, response
        except:
            response = "Handle not found."
            return False, response


class User(models.Model):
    handle = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()