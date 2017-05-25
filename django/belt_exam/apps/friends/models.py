from __future__ import unicode_literals
import bcrypt
from django.db import models
import re


class UserManager(models.Manager):
    def validate(self, postData):
        errors = []
        try: 
            User.objects.get(email=postData['email']) 
            errors.append("User already exists. Please log in instead.")
        except: 
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
            NAME_REGEX = re.compile(r'[A-Za-z]{2,}')
            if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
                errors.append("First and last name must be 2 or more characters.")
            if re.match(NAME_REGEX, postData['alias']):
                errors.append("Alias must be 2 or more characters")
            if postData['password'] != postData['confirm_password']:
                errors.append("Passwords must match")
            if len(postData['password']) < 8:
                errors.append("Password must be 8 or more characters")
            if not EMAIL_REGEX.match(postData['email']):
                errors.append("Invalid Email Address!")
            else:
                hashed = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())
                user = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], alias=postData['alias'], email=postData['email'], birthday=postData['birthday'],password=hashed)
                errors.append("Successfully registered. Please log in.")
                return True, errors
        return False, errors
    
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

    def addFriend(self, user_id, friend_id):
        user = User.objects.get(id=user_id)
        friend = User.objects.get(id=friend_id)
        Friendship.objects.create(user=user, friend=friend)
        Friendship.objects.create(user=friend, friend=user)

    def removeFriend(self, user_id, friend_id):
        user = User.objects.get(id=user_id)
        print user
        friend = User.objects.get(id=friend_id)
        print friend
        friendship1 = Friendship.objects.get(user=user, friend=friend)
        friendship2 = Friendship.objects.get(user=friend, friend=user)
        friendship1.delete()
        friendship2.delete()

class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Friendship(models.Model):
    user = models.ForeignKey(User, related_name='requester')
    friend = models.ForeignKey(User, related_name='accepter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # remove this line?
    objects = models.Manager()
