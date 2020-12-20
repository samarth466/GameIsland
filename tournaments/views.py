from django.shortcuts import render
from tournaments.models import Room
from django.http import HttpResponse
from UserAuth.models import User
from datetime import date

# Create your views here.


def home(request, mode):
    if str(mode) == 'create':
        form = Room(code='12F50D', host='Samarth Saxena')
        form.save()
        u = User(user_name='Samarth Saxena', user_username='archer_home', user_email='samarths466@gmail.com',
                 user_password=hash('1234'), user_birth_date=date(2007, 2, 6), logged_in=True, security_pin=hash('sam456'), room=form)
        u.save()
        return HttpResponse(str(User.objects.filter(user_name='Samarth Saxena')))
    elif str(mode) == 'delete':
        return HttpResponse(str(Room.objects.all().first().delete()))
    return HttpResponse('That method is not valid.')
