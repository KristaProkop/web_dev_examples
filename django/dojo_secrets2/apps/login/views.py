from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
from django.core.urlresolvers import reverse


def index(request):
    if "id" not in request.session:
        return render(request, 'login/index.html')
    else: 
        return redirect(reverse('secrets:index'))

def create(request):
    valid, response = User.objects.validate(request.POST)
    if valid:
        context = {
            'event': 'registered',
            'first_name': request.POST['first_name']
        }
        messages.success(request, response)
        return redirect(reverse('login:index'))
    elif not valid: 
        messages.error(request, response)
    else:
        messages.error(request, "Something went wrong. Try again later.")
    return redirect(reverse('login:index'))
    

def login(request):
    valid, response = User.objects.login(request.POST)
    if valid:
        request.session['id'] = response.id
        request.session['name'] = response.first_name
        return redirect(reverse('secrets:index'))
    if not valid:
        messages.error(request, response)
        return redirect(reverse('login:index'))

        
def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))

