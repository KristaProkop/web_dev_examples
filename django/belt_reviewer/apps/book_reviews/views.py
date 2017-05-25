from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Avg
from .models import Author, Book, Review
from ..login.models import User

def index(request):
    if 'id' not in request.session:
        return redirect(reverse('login:index'))
    else: 
        context = {
            'recent_books': Book.objects.all().order_by('-created_at')[:5],
            'reviews': Review.objects.all().order_by('-created_at')[:6],
        }
        for book in context['recent_books']:
            reviews = Review.objects.filter(book=book)
            book.avg_rating = (reviews.aggregate(Avg('rating')))['rating__avg']
            book.avg_rating = round(book.avg_rating, 2)
        return render(request, 'book_reviews/index.html', context)

def show_all(request):
    context = {
        'recent_books': Book.objects.all().order_by('-created_at')[:5],
        'reviews': Review.objects.all().order_by('-created_at'),
    }
    return render(request, 'book_reviews/index.html', context)

def create(request):
    if request.method == "GET":
        context = {
            'books': Book.objects.all().order_by('title'),
            'authors': Author.objects.all().order_by('name')
        }
        return render(request, 'book_reviews/add_book.html', context)
    else:
        try: 
            author = Author.objects.create_author(request.POST)
            book = Book.objects.create_book(request.POST, author)
            review = Review.objects.create_review(request.POST, book.id, request.session['id'])
            return redirect(reverse('book_reviews:index'))
        except:
            return render(request, 'book_reviews/add_book.html')

def show_book(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book,
        'author': book.author.name,
        'reviews': Review.objects.filter(book=book)
    }
    return render(request, 'book_reviews/show_book.html', context)

def create_review(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        review = Review.objects.create_review(request.POST, book.id, request.session['id'])
        return redirect(reverse('book_reviews:show_book', kwargs={'id': id})) 
    return redirect(reverse('book_reviews:index'))

def show_user(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
        'reviews': Review.objects.filter(user=user).order_by('-created_at')
    }
    return render(request, 'book_reviews/show_user.html', context)
    