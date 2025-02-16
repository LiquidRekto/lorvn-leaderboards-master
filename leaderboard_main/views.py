from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
import leaderboard_main.lorvn.database as player_db
import datetime
import os


data = []


# Create your views here.

def home(request):
    dat = {
        'americas': player_db.getMastersData('americas'),
        'asia': player_db.getMastersData('asia'),
        'europe': player_db.getMastersData('europe'),
        'sea': player_db.getMastersData('sea')
    }
    context = {
        'data': str(dat),
        'default_region': os.environ['DEFAULT_REGION']

    }

    return render(request, 'leaderboard/leaderboard.html', context)

def dev(request):
    dat = {
        'americas': player_db.getMastersData('americas','list'),
        'asia': player_db.getMastersData('asia','list'),
        'europe': player_db.getMastersData('europe','list'),
        'sea': player_db.getMastersData('sea','list')
    }
    plyrs = {
        'americas': player_db.getMastersCount('americas'),
        'asia': player_db.getMastersCount('asia'),
        'europe': player_db.getMastersCount('europe'),
        'sea': player_db.getMastersCount('sea')
    }
    chosen = {
        'americas': player_db.getMastersData('americas','count'),
        'asia': player_db.getMastersData('asia','count'),
        'europe': player_db.getMastersData('europe','count'),
        'sea': player_db.getMastersData('sea','count')
    }
    context = {
        'data': str(dat),
        'default_region': os.environ['DEFAULT_REGION'],
        'count': str(plyrs),
        'listed': str(chosen)
    }

    return render(request, 'leaderboard/leaderboard_devh2xJVloI9K32.html', context)


def about(request):
    return render(request, 'leaderboard/about.html')

def auto_redirect(request):
    response = redirect('/leaderboards/beta/')
    return response