from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "./index.html")


def game_creation(requset):
    return render(requset, "./game_creation.html")


def team_creation(request):
    return ""
