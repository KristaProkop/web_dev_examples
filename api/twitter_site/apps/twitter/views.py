
from django.shortcuts import render, redirect
from .models import Tweeter, AppOwner
from ..login.models import User
from cryptography.fernet import Fernet
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    if 'id' not in request.session:
        return redirect(reverse('login:index'))
    return render(request, 'twitter/index.html')

def generate_key(request):
    if request.method == "POST":
        owner = AppOwner.objects.create_owner(request.session['id'], request.POST)
        key, message = Tweeter.objects.generate_key(request.session['id'])
        request.session['key'] = key
        messages.warning(request, key)
    return redirect(reverse('twitter:index'))

def create_tweet(request):
    if request.method == "POST":
        try: 
            api = AppOwner.objects.authenticate(request.session['id'])
            tweet = str(request.POST['tweet'])
            key = request.session['key']
            if type(key) == unicode:
                key = key.encode()
            cipher_suite = Fernet(key)
            encrypted_tweet = cipher_suite.encrypt(tweet)
            api.update_status(status=encrypted_tweet)
            messages.success(request, "Tweet successfully sent")
        except: 
            messages.error(request, "Something went wrong; please try again")
    return redirect(reverse('twitter:index'))

def decrypt_tweet(request):
    if request.method == "POST":
        try:
            del request.session['tweet']
            del request.session['author']
            del request.session['date']
        except:
            pass
        try:
            api = AppOwner.objects.authenticate(request.session['id'])
            tweet_id = int(request.POST['tweet_id'])
            key, search_string, tweet = Tweeter.objects.get_decrypt_key(api, tweet_id)
            if type(key) == unicode:
                key = key.encode()
            cipher_suite = Fernet(key)
            decrypted_tweet = cipher_suite.decrypt(search_string)
            tweeter = str(tweet.user.screen_name)
            request.session['tweet'] = decrypted_tweet
            request.session['author'] = tweeter 
            request.session['date'] = str(tweet.created_at)
        except:
            messages.error(request, "Invalid tweet. Please double check the tweet ID.")
    return redirect(reverse('twitter:index'))

    
