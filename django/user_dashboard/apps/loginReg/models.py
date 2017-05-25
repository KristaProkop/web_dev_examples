from __future__ import unicode_literals
import re
from django.db import models
import bcrypt
# need to add session id
class UserManager(models.Manager):
    def validate(self, postData):
        try: 
            User.objects.get(email=postData['email']) 
            response = "User already exists."
        except: 
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
            NAME_REGEX = re.compile(r'[A-Za-z]{2,}')
            if not EMAIL_REGEX.match(postData['email']):
                response = ("Invalid Email Address!")
            elif not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
                response = ("First and last name must be 2 or more characters.")
            elif postData['password'] != postData['confirm_password']:
                response = ("Passwords must match")
            elif len(postData['password']) < 8:
                response = ("Password must be 8 or more characters")
            else:
                hashed = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())
                user = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashed, level='NORMAL')
                response = ("Successfully registered.")
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

    def update_user(self, id, category, postData):
        # category 1 = description; category 2 = information, category 3 = password
        if category == '1':
            user = User.objects.filter(id=id).update(description=postData['description'])
            response = "Description successfully updated"
        if category == '2':
            user = User.objects.filter(id=id).update(email=postData['email'], first_name=postData['first_name'], last_name=postData['last_name'])
            response = "Information successfully updated"
        if category == '3':
            if postData['password'] != postData['confirm_password']:
                response = ("Passwords must match")
            elif len(postData['password']) < 8:
                response = ("Password must be 8 or more characters")
            else:
                hashed = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())
                user = User.objects.filter(id=id).update(password=hashed)
                response = ("Successfully updated.")
                return True, response
            return False, response
        return True, response

    # def update_description(self, id, description):
    #     user = User.objects.filter(id=id).update(description=description)
    #     return True

    # def update_information(self, id, postData):
    #     user = User.objects.filter(id=id).update(email=postData['email'], first_name=postData['first_name'], last_name=postData['last_name'])
    #     return True

    # def update_password(self, id, postData):
    #     if postData['password'] != postData['confirm_password']:
    #         response = ("Passwords must match")
    #     elif len(postData['password']) < 8:
    #         response = ("Password must be 8 or more characters")
    #     else:
    #         hashed = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())
    #         user = User.objects.filter(id=id).update(password=hashed)
    #         response = ("Successfully updated.")
    #         return True, response
    #     return False, response

class User(models.Model):
    NORMAL = "Normal"
    ADMIN = 'Admin'
    LEVEL_CHOICES = (
        (NORMAL, 'Normal'),
        (ADMIN, 'Admin'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    level = models.CharField(
        choices=LEVEL_CHOICES,
        default=NORMAL,
        max_length=6,
    )
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def is_admin(self):
        return self.level in (self.ADMIN)