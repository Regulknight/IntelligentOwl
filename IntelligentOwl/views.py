from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader

from IntelligentOwl.models import Team, Player


def index(request):
    return render(request, "./index.html")


def game_browser(request):
    return render(request, "./game_browser.html")


def game_creation(request):
    return render(request, "./game_creation.html")


def team_editor(request, team_id):
    cur_team = get_object_or_404(Team, pk=team_id)
    player_list = cur_team.player_set.order_by("name")

    if len(player_list) < 6:
        for i in range(6-len(player_list)):
            reg_id = Player.objects.order_by("player_reg_id").last().player_reg_id
            Player.objects.create(player_team=cur_team, player_reg_id=reg_id+1)

    return render(request, './team_editor.html', {'team': cur_team, 'player_list': player_list})


def team_browser(request):
    team_list = Team.objects.order_by('name')
    template = loader.get_template('team_browser.html')
    context = {
        'team_list': team_list,
    }
    return HttpResponse(template.render(context, request))


def game_conduction(request):
    return render(request, './game_conduction.html')


def overall_rating(requset):
    return render(requset, './overall_rating.html')
