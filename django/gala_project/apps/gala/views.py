from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Invitee, Guest, Dinner,  Hotel
from django.utils import timezone


def index(request):
    return render(request, 'gala/index.html')

def rsvp(request):
    if request.method == "POST":  
        if 'yes' in request.POST:
            try:
                invitee = Invitee.objects.get(code=request.POST['code'])
                request.session['id'] = invitee.id
                if invitee.rsvp == True:
                    response = "You've already RSVPd. Email the administrator to make changes to your response"
                    messages.success(request, response)
                else:
                    context = {
                        'invitee': invitee,
                    }
                    return render(request, 'gala/rsvp.html', context)
            except: 
                messages.error(request, "Not found. Please contact administrator.")
        if 'no' in request.POST:
            Invitee.objects.rsvp_no(request.POST)
            response = "Sorry you can't make it! Thanks for RSVPing"
            messages.success(request, response)
    return redirect(reverse('gala:index'))


def rsvp_user(request):
    if request.method == "POST":
        invitee = Invitee.objects.rsvp_user(request.POST)
        count = invitee.guests_count
        context = {
            'invitee': invitee,
            'loop': range(1, count+1),
        }
        return render(request, 'gala/rsvp_detail.html', context)
    else:
        return redirect(reverse('gala:rsvp'))

def rsvp_detail(request):
    if request.method == "POST":
        valid, response = Invitee.objects.rsvp_detail(request.POST)
        if valid:
            messages.success(request, response)
        else:
            messages.error(request, response)
        return render(request, 'gala/success.html')
    return redirect(reverse('gala:rsvp'))

def hotel(request):
    if request.method == "POST":
        valid, response = Hotel.objects.reserve(request.session['id'], request.POST)
        if valid:
            messages.success(request, response)
        else:
            messages.error(request, "Something went wrong")
        return redirect(reverse('gala:index'))
    else:
        invitee = Invitee.objects.get(pk=request.session['id'])
        context = {
            'invitee': invitee,
        }
        return render(request, 'gala/hotel.html', context)

def reports(request):
    if request.method == "POST":
        return redirect(reverse('gala:reports')) 
    else:
        dinners_count = Dinner.objects.show()
        context = {
            'invitees': Invitee.objects.all(),
            'guests': Guest.objects.all(),
            'dinners': Dinner.objects.all(),
            'dinner_subtotals': dinners_count,
            'hotels': Hotel.objects.all(),
        }
        return render(request, 'gala/reports.html', context)

# TODO: Admin Tools
#def admin(request):
    # add names
    # delete invitees, guests, hotels, dinners
    # change fields
    # delete guests

