from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User, Friendship

def index(request):
    if "id" not in request.session:
        return render(request, 'friends/index.html')
    else:
        return redirect(reverse('friends:friends'))

def friends(request):
    user = User.objects.get(id=request.session['id'])
    all_users = User.objects.all()
    my_friendships = Friendship.objects.filter(user=user) 
    # gather the user's friends' IDs, then create a new list of all non-friends
    friend_ids = []
    for friendship in my_friendships:
        friend_ids.append(friendship.friend.id)
    non_friends = []
    for user in all_users:
        if user.id != request.session['id']:
            if user.id not in friend_ids:
                non_friends.append(user)
    context = {
        'current_user' : user,
        'friends': my_friendships,
        'users' : non_friends,
    }
    return render(request, 'friends/friends.html', context)

def register(request):
    if request.method == 'POST':
        valid, response = User.objects.validate(request.POST)
        if valid:
            messages.success(request, response)
            return redirect(reverse('friends:login'))
        if not valid:
            for issue in response:
                messages.error(request, issue)

            return redirect(reverse('friends:login'))
    else:
        return render(request, 'friends/index.html')

def login(request):
    if request.method == "POST":
        print 'post'
        valid, response = User.objects.login(request.POST)
        if valid:
            request.session['id'] = response.id
            request.session['name'] = response.first_name
            return redirect(reverse('friends:friends'))
        if not valid:
            messages.error(request, response)
            return redirect(reverse('friends:login'))
    else:
        return render(request, 'friends/index.html')

def logout(request):
    request.session.clear()
    return redirect(reverse('friends:index'))

def show_friend(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'friends/profile.html', context)

def create_friend(request, id):
    if request.method == "POST":
         User.objects.addFriend(request.session['id'], id)
    return redirect(reverse('friends:friends'))

def destroy_friend(request, id):
    if request.method == "POST":
        User.objects.removeFriend(request.session['id'], id)
    return redirect(reverse('friends:friends'))