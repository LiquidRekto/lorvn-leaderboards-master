from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
import leaderboard_main.lorvn.database as player_db
import datetime

posts = [
    {
        'author':'LiquidRekto',
        'title':'Hello, World!',
        'time':'20 Jan',
        'content':'LuL'
    },
    {
        'author':'SarahBong',
        'title':'Hello, World 2!',
        'time':'20 Feb',
        'content':'Lmao'
    }
]


# Create your views here.

def home(request):
    context = {
        'posts':posts
    }
    player_db.getMastersData('sea')
    return render(request, 'leaderboard/leaderboard.html', context)

def about(request):
    return render(request, 'leaderboard/about.html')

def auto_redirect(request):
    response = redirect('/leaderboards/')
    return response