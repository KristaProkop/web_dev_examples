from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import RegisterForm, LoginForm

def index(request):
    if "id" not in request.session:
        regForm = RegisterForm()
        logForm = LoginForm()
        context = { 
            "regForm": regForm,
            "logForm": logForm
        }
        return render(request, 'login/index.html', context)
    else: 
        return redirect(reverse('book_reviews:index'))

def create(request):
    if request.method == "POST":
        valid, response = User.objects.validate(request.POST)
        if valid:
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
            request.session['name'] = response.first_name
            return redirect(reverse('book_reviews:index'))
        if not valid:
            messages.error(request, response)
    return redirect(reverse('login:index'))

        
def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))


