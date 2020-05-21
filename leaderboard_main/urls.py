from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="leaderboard_main-home"),
    path('about/', views.about, name="leaderboard_main-about"),
    path('devh2xJVloI9K32/',views.dev, name="leaderboard_main-dev")
]