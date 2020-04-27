from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'leaderboard/home.html', context)

def about(request):
    return render(request, 'leaderboard/about.html')