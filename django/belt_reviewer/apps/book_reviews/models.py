from __future__ import unicode_literals
from django.db import models
from ..login.models import User

class BookManager(models.Manager):
    def create_book(request, postData, author):
        try: 
            book = Book.objects.get(title=postData['title'])
        except:
            book = Book.objects.create(title=postData['title'], author=author)
        return book

class AuthorManager(models.Manager):
    def create_author(request, postData):
        if postData['new_author']:
            author = Author.objects.create(name=postData['new_author'])
        elif postData['existing_author']: 
            author = Author.objects.get(name=postData['existing_author'])
        return author

class ReviewManager(models.Manager):
    def create_review(request, postData, book_id, user_id):
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=user_id)
        review = Review.objects.create(book=book, review_content=postData['review'], rating=postData['rating'], user=user)
        return True

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = AuthorManager()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews')
    review_content = models.TextField(max_length=1000)
    rating = models.IntegerField()
    user = models.ForeignKey(User, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()
