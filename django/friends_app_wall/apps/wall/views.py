from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user

from .models import User, Message, Comment
from ..friends.models import Friendship

# Create your views here.
@login_required(login_url='/')
def index(request):
    # upon login show  current users's wall
    friend = User.objects.get(id=request.user.id)
    return redirect(reverse('wall:user_wall', kwargs={'friend_id': friend.id}))

@login_required()
def user_wall(request, friend_id):
    current_user = request.user
    friend = User.objects.get(id=friend_id)
    messages = Message.objects.filter(wall=friend).order_by('-created_at')
    all_friendships = Friendship.objects.filter(user=current_user).order_by('friend__last_name')

    # TODO: add logic to verify friendship exists, else redirect 
    # for friendship in all_friendships:
    #     print friend.username == friendship.friend.username 

    comments = Comment.objects.all().order_by('created_at')
    context = {
        'messages': messages,
        'comments': comments,
        'user': friend,
        'current_user': current_user,
        'all_friendships': all_friendships,
    }
    return render(request, 'wall/wall.html', context)

@login_required()
def message_submit(request, wall_id):
    if request.method == "POST":
        current_user = request.user
        wall = User.objects.get(id=wall_id)
        message = Message.objects.create(wall=wall, user=current_user, message=request.POST['message'])
        return redirect(reverse('wall:user_wall', kwargs={'friend_id': wall.id}))

@login_required()
def comment_submit(request, message_id):
    if request.method == "POST":
        current_user = request.user
        message = Message.objects.get(id=message_id)

        comment = Comment.objects.create(user=current_user, message=message, comment=request.POST['comment'])

        return redirect(reverse('wall:user_wall', kwargs={'friend_id': message.wall.id}))

def comment_delete(request, comment_id):
    referer = request.META.get('HTTP_REFERER')
    comment = Comment.objects.get(id=comment_id)
    if comment.user.id == request.user.id:
        comment.delete()
    return redirect(referer)


def message_delete(request, message_id):
    referer = request.META.get('HTTP_REFERER')
    message = Message.objects.get(id=message_id)
    if message.user.id == request.user.id:
        message.delete()
    return redirect(referer)

