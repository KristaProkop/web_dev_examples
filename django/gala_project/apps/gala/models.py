from __future__ import unicode_literals
from django.db import models
from django.db.models import Count
from django.utils import timezone


class InviteeManager(models.Manager):
    def rsvp_user(self, postData):
        invitee = Invitee.objects.get(code=postData['code'])
        Invitee.objects.select_related().filter(code=postData['code']).update(email=postData['email'], address=postData['address'],guests_count=int(postData['guests_count']), rsvp=True)
        invitee = Invitee.objects.get(code=postData['code'])
        return invitee

    def rsvp_no(self, postData):
        invitee = Invitee.objects.get(code=postData['code'])
        invitee.rsvp_date = timezone.now()
        invitee.rsvp = False
        invitee.save()
        guests = Guest.objects.filter(invitee=invitee).delete()
        dinners = Dinner.objects.filter(invitee=invitee).delete()
        hotels = Hotel.objects.filter(invitee=invitee).delete()


    def rsvp_detail(self, postData):
        # initialize dictionary from post querydict and delete token key and code. Iterate through dictionary to create new "guests" dictionary organized by guest response
        post_dict = dict(postData.iterlists())
        del post_dict['csrfmiddlewaretoken']
        del post_dict['code']
        num_guests = len(post_dict['name'])
        guests = {}
        for i in range(0, num_guests):
            guests[i] = {}
            for key in post_dict:
                guests[i][key] = post_dict[key][i]
        invitee = Invitee.objects.get(code=postData['code'])
        invitee.rsvp_date = timezone.now()
        invitee.save()
        # create dinner objects for all, create guest objects for guests only
        for key, value in guests.iteritems():
            name = value['name']
            dinner = value['dinner']
            notes = value['restrictions']
            dinner = Dinner.objects.create(preferred_name=name,dinner=dinner,notes=notes, invitee=invitee)
            if key != 0:
                guest = Guest.objects.create(name=name, invitee=invitee)
        response = "Successfully registered!"
        return True, response

class GuestManager(models.Manager):
    def show(self):
        return True

class DinnerManager(models.Manager):
    def show(self):
        fieldname = 'dinner'
        dinners = Dinner.objects.values(fieldname).order_by(fieldname).annotate(the_count=Count(fieldname))
        return dinners

class HotelManager(models.Manager):
    # need to add logic to replace hotel reservations if already submitted once
    def reserve(self, id, postData):
        invitee = Invitee.objects.get(id=id)
        Hotel.objects.create(invitee=invitee, check_in=postData['in'], check_out=postData['out'])
        response = "Successfully reserved hotel room"
        return True, response

class Invitee(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    guests_count = models.IntegerField()
    rsvp_date = models.DateTimeField(null=True, blank=True)
    rsvp = models.NullBooleanField(null=True, blank=True)
    objects = InviteeManager()

class Guest(models.Model):
    name = models.CharField(max_length=100)
    invitee = models.ForeignKey(Invitee)
    objects = GuestManager()

class Dinner(models.Model):
    preferred_name = models.CharField(max_length=100)
    invitee = models.ForeignKey(Invitee,null=True, blank=True)
    dinner = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField()
    objects = DinnerManager()

class Hotel(models.Model):
    invitee = models.ForeignKey(Invitee)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    objects = HotelManager()


