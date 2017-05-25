from __future__ import unicode_literals
from django.db import models
from ..login.models import User

# Create your models here.
class SecretManager(models.Manager):
    def create_secret(self, user_id, message):
        user = User.objects.get(id=user_id)
        secret = Secret.objects.create(posted_by=user, message=message)
        return True

    def delete_secret(self, secret_id):       
        Secret.objects.filter(id=secret_id).delete()
        return True

    def create_like(self, user_id, secret_id):
        user = User.objects.filter(id=user_id)
        secret = Secret.objects.get(id=secret_id)
        user = user[0]
        secret.all_likes.add(user)
        secret.save()
        return True



class Secret(models.Model):
    message = models.TextField(max_length=1000)
    posted_by = models.ForeignKey(User)
    all_likes = models.ManyToManyField(User, related_name="all_users")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = SecretManager()

    # def __str__(self):
    #     return self.secret


