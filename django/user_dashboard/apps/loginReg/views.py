from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'loginReg/index.html', )

def logoff(request):
    request.session.clear()
    return redirect(reverse('loginReg:index'))

def register(request):
    if request.method == "POST":
        valid, response = User.objects.validate(request.POST)
        if valid:
            return redirect(reverse('dashboard:index'))
        elif not valid: 
            messages.error(request, response)
            return redirect(reverse('loginReg:register'))
    else: 
        return render(request, 'loginReg/register.html')

def login(request):
    if request.method == "POST":
        valid, response = User.objects.login(request.POST)
        if valid:
            request.session['id'] = response.id
            return redirect(reverse('dashboard:index'))
        if not valid:
            messages.error(request, response)
            return redirect(reverse('loginReg:login'))
    else:
        return render(request, 'loginReg/login.html')

def update_user(request, id, category):
    valid, response = User.objects.update_user(id, category, request.POST)
    if valid:
        messages.success(request, response)
        return redirect(reverse('dashboard:index')) 
    if not valid:
        messages.error(request, response)
        return redirect(reverse('users:edit_user', kwargs={'id': id})) 

def create_user(request):
    if request.method == "POST":
        valid, response = User.objects.validate(request.POST)
        if valid:
            messages.success(request, response)
            return redirect(reverse('dashboard:index'))
        if not valid:
            messages.error(request, response)
            return redirect(reverse('dashboard:add_user'))
    else:
        return render(request, 'dashboard/add_user.html')

def destroy(request, id):
    User.objects.filter(id=id).delete()
    return redirect(reverse('dashboard:index'))

