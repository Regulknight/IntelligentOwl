from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader

from IntelligentOwl.models import Team


def index(request):
    return render(request, "./index.html")


def game_creation(requset):
    return render(requset, "./game_creation.html")


def team_editor(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, './team_editor.html', {'team': team})


def team_browser(request):
    team_list = Team.objects.order_by('name')[:50]
    template = loader.get_template('team_browser.html')
    context = {
        'team_list': team_list,
    }
    return HttpResponse(template.render(context, request))
