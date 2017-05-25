# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .forms import EditProfileForm, EditProfileImageForm
from .models import User, Friendship, UserProfile
from ..wall.models import Message, Comment

# TODO: Add registration validation

def index(request):
    return render(request, 'friends/login.html')

def user_authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    return user

def user_login(request):
    try:
        user = user_authenticate(request)
        if user is not None:
            login(request, user)
            return redirect(reverse('wall:index'))
        else:
            messages.error(request, "User not found. Check username and password.")
            return redirect(reverse('friends:index'))
    except:
        messages.error(request, "Something went wrong")
        return redirect(reverse('friends:index'))
    
def user_logout(request):
    logout(request)
    return redirect(reverse('friends:index'))

        
def register(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password )
            messages.success(request, "Successfully registered. Please log in.")
            return redirect(reverse('friends:index'))
        except IntegrityError:
            messages.error(request, "That username is taken. Try again.")
            return redirect(reverse('friends:register'))
    return render(request, 'friends/register.html')


@login_required(login_url='/')
def friends(request):
    current_user = request.user
    all_users = User.objects.all()
    my_friendships = Friendship.objects.filter(user=current_user).order_by('friend__username')
    # gather the user's friends' IDs, then create a new list of all non-friends 
    friend_ids = []
    for friendship in my_friendships:
        friend_ids.append(friendship.friend.id)
    non_friends = []
    for one_user in all_users:
        if one_user.id != current_user.id:
            if one_user.id not in friend_ids:
                non_friends.append(one_user)
    context = {
        'current_user' : current_user,
        'friends': my_friendships,
        'users' : non_friends,
    }
    return render(request, 'friends/friends.html', context)

@login_required(login_url='/')
def show_user(request, id):
    user = User.objects.get(id=id)
    messages = Message.objects.filter(user=user)
    comments = Comment.objects.filter(user=user)
    context = {
        'user': user,
        'messages': messages,
        'comments': comments,
    }
    return render(request, 'friends/profile.html', context)

def create_friendship(request, id):
    if request.method == "POST":
        current_user = request.user
        Friendship.objects.addFriend(current_user.id, id)
    return redirect(reverse('friends:friends'))

def destroy_friendship(request, id):
    if request.method == "POST":
        current_user = request.user
        Friendship.objects.removeFriend(current_user.id, id)
    return redirect(reverse('friends:friends'))


 # TODO: Finish function to handle edit profile/image. Only save form fields that are filled in.
# def edit_profile(request, id):
#     if request.method == "POST":
#         instance = request.user
#         form = EditProfileForm(request.POST or None, instance=instance)
#         if form.is_valid():
#               form.save()
#         return render(request, 'friends/edit_profile.html')
#     else:
#         #Only allow edit current user profile
#         if request.user.id == int(id):
#             profile_form = EditProfileForm()
#             image_form = EditProfileImageForm()
#             user_profile = UserProfile.objects.filter(user=request.user)
#             context = {
#                 'profile_form': profile_form,
#                 'image_form': image_form,
#                 'user_profile': user_profile,
#             }
#             return render(request, 'friends/edit_profile.html', context)
#         else:
#             return redirect(reverse('friends:friends'))

# TODO: HANDLE IMAGE UPLOADS
# def edit_profile_image(request, id):
#     if request.method == 'POST':
#         instance = request.user
#         form = EditProfileImageForm(request.FILES or None, instance=instance)
#         if form.is_valid():
#             form.save()
#         return redirect(reverse('friends:edit_profile', kwargs={'id': request.user.id} ))


