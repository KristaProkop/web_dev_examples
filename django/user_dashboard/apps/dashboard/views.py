from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse
from .models import Message, Comment
from ..loginReg.models import User

def index(request):
    if 'id' not in request.session:
        return redirect(reverse('loginReg:login'))
    else:
        current_user = User.objects.get(id=request.session['id'])
        if current_user.level == "ADMIN":
            return redirect(reverse('dashboard:admin'))   
        else:
            context = {
                'users': User.objects.all(),
                'level': current_user.level
            }   
            return render(request, 'dashboard/dashboard.html', context)

def admin(request):
    context = {
                'users': User.objects.all(),
                'level': "ADMIN"
            }  
    return render(request, 'dashboard/dashboard.html', context)

def create_user(request):
    return render(request, 'dashboard/add_user.html')

def edit_user(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
    }
    return render(request, 'dashboard/update_profile.html', context)

def show_user(request, id):
    user = User.objects.get(id=id)
    messages = Message.objects.filter(user_for=user)
    comments = Comment.objects.all()
    context = {
        'user': user,
        'messages': messages,
        'comments': comments,
    }
    return render(request, 'dashboard/show_user.html', context)

def create_message(request, user_id, creator_id):
    message = Message.objects.create_message(user_id, creator_id, request.POST)
    return redirect(reverse('users:show_user', kwargs={'id': user_id})) 

def create_comment(request, user_id, message_id, origin_id):
    comment = Comment.objects.create_comment(user_id, message_id, request.POST)
    return redirect(reverse('users:show_user',kwargs={'id': origin_id})) 



