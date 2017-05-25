from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def validate(self, postData):
        try: 
            User.objects.get(email=postData['email']) 
            response = "User already exists. Please log in instead."
        except: 
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
            NAME_REGEX = re.compile(r'[A-Za-z]{2,}')
            if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
                response = ("First and last name must be 2 or more characters.")
            elif postData['password1'] != postData['password2']:
                response = ("Passwords must match")
            elif len(postData['password1']) < 8:
                response = ("Password must be 8 or more characters")
            elif not EMAIL_REGEX.match(postData['email']):
                response = ("Invalid Email Address!")
            else:
                hashed = bcrypt.hashpw(postData['password1'].encode('utf-8'), bcrypt.gensalt())
                user = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashed)
                response = ("Successfully registered. Please log in.")
                return True, response
        return False, response

    def login(self, postData):
        try: 
            email = str(postData['email'])
            password = str(postData['password'])
            user = User.objects.get(email=email)
            userPwBytes = password.encode('utf-8')
            hashedPwBytes = user.password.encode('utf-8')
            if hashedPwBytes == (bcrypt.hashpw(userPwBytes, hashedPwBytes)):
                return True, user
            else:
                response = "Email and password don't match."
                return False, response
        except:
            response = "Email not found."
            return False, response


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()