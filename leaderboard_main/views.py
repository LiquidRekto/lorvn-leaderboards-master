from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
import leaderboard_main.lorvn.database as player_db
import datetime


data = []


# Create your views here.

def home(request):
    sea_dat = player_db.getMastersData('sea')
    context = {
        'data': sea_dat
    }
    
    return render(request, 'leaderboard/leaderboard.html', context)

def about(request):
    return render(request, 'leaderboard/about.html')

def auto_redirect(request):
    response = redirect('/leaderboards/')
    return response