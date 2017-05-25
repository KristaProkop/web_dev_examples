from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Secret
from ..login.models import User
from django.db.models import Count
from datetime import datetime

# Create your views here.
def index(request):
    if 'id' not in request.session:
        return redirect(reverse('login:index'))
    else: 
        context = {
            'secrets': Secret.objects.all().order_by('-created_at')[:10],
            'users': User.objects.all()
        }
        for secret in context['secrets']:
            print secret.created_at
            print datetime.now()
            # add logic to calculate time elapsed
            if secret.posted_by.id == request.session['id']:
                secret.user_auth = True
            for user in secret.all_likes.all():
                if user.id == request.session['id']:
                    secret.liked = True
        return render(request, 'secrets/index.html', context)

def most_popular(request):
    context = {
        'secrets': Secret.objects.all().annotate(num_likes=Count('all_likes')).order_by('-num_likes', '-created_at'),
    }
    for secret in context['secrets']:
        if secret.posted_by.id == request.session['id']:
            secret.user_auth = True
        for user in secret.all_likes.all():
            if user.id == request.session['id']:
                secret.liked = True
    return render(request, 'secrets/popular_secrets.html', context)

def create_secret(request, id):
    Secret.objects.create_secret(message=request.POST['message'], user_id=id)
    return redirect(reverse('secrets:index'))

def delete_secret(request, id):
    referrer = request.POST.get('next', '/')
    Secret.objects.delete_secret(secret_id=id)
    if referrer == "/secrets/":    
        return redirect(reverse('secrets:most_popular'))
    else:
        return redirect(reverse('secrets:index'))

def create_like(request, user_id, secret_id):
    referrer = request.POST.get('next', '/')
    Secret.objects.create_like(user_id=user_id, secret_id=secret_id)
    if referrer == "/secrets/":    
        return redirect(reverse('secrets:most_popular'))
    else:
        return redirect(reverse('secrets:index'))


