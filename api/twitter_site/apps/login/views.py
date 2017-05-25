from django.shortcuts import render, redirect
from .models import User
from ..twitter.models import Tweeter, AppOwner
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import RegisterForm, LoginForm

def index(request):
    # user = User.objects.get(handle='johndoh99')
    # AppOwner.objects.get(user=user).delete()
    # Tweeter.objects.get(user=user).delete()

    if "id" not in request.session:
        regForm = RegisterForm()
        logForm = LoginForm()
        context = { 
            "regForm": regForm,
            "logForm": logForm
        }
        return render(request, 'login/index.html', context)
    else: 
        return redirect(reverse('twitter:index'))

def create(request):
    if request.method == "POST":
        valid, response = User.objects.validate(request.POST)
        if valid:
            context = {
                'event': 'registered',
            }
            messages.success(request, response)
            return redirect(reverse('login:index'))
        elif not valid: 
            messages.error(request, response)
        else:
            messages.error(request, "Something went wrong. Try again later.")
    return redirect(reverse('login:index'))
    

def login(request):
    if request.method == "POST":
        valid, response = User.objects.login(request.POST)
        if valid:
            request.session['id'] = response.id
            request.session['handle'] = response.handle
            try:
                tweeter = Tweeter.objects.get(user=response)
                key = tweeter.key
                request.session['key'] = key
            except:
                return redirect(reverse('twitter:index'))
        if not valid:
            messages.error(request, response)
    return redirect(reverse('login:index'))

        
def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))


