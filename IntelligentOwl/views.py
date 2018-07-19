from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from IntelligentOwl.forms import TeamForm, PlayerForm, GameForm
from IntelligentOwl.models import Team, Player, Game, Question, Tour


def index(request):
    return render(request, "./index.html")


def game_browser(request):
    game_list = Game.objects.order_by('id')
    template = loader.get_template('game_browser.html')
    context = {
        'game_list': game_list,
    }
    return HttpResponse(template.render(context, request))


def game_creation(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()
            for i in range(game.tour_count):
                tour = Tour.objects.create(game=game, order_number=i, questions_count=game.questions_count)
                for j in range(tour.questions_count):
                    Question.objects.create(tour=tour, order_number=j)
            return redirect('game_browser')
    else:
        form = GameForm()
    return render(request, "./game_creation.html", {'form': form})


def game_details(request, game_id):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if 'delete' in form.data:
            Game.objects.get(pk=game_id).delete()
            return redirect('game_browser')
        if form.is_valid():
            form.save()
            return redirect('game_browser')
    else:
        form = GameForm()
        game = Game.objects.get(pk=game_id)
        form.initial = {'name': game.name, 'tour_count': game.tour_count, 'questions_count': game.questions_count,
                        'game_coefficient': game.game_coefficient}
    return render(request, "./game_details.html", {'form': form})


def team_details(request, team_id):
    team = Team.objects.get(pk=team_id)
    player_list = team.player_set.order_by("player_reg_id")
    PlayerFormset = formset_factory(PlayerForm, min_num=6, max_num=6)
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if 'delete' in form.data:
            Team.objects.get(pk=team_id).delete()
            return redirect('team_browser')
        player_formset = PlayerFormset(request.POST)
        if form.is_valid() and player_formset.is_valid():
            for i in range(len(player_formset)):
                player = (player_formset[i].save(commit=False))
                player.player_team = Team.objects.get(pk=team_id)
                player.player_reg_id = get_player_reg_id()
                player.save()
                if i == 0:
                    team.captain = player
            team.team_reg_id = get_team_reg_id()
            form.save()
            if 'save_and_create_next' in form.data:
                return redirect('team_new')
            if 'save' in form.data:
                return redirect('team_details', team_id=team.id)

            return redirect('team_browser')
    else:
        form = TeamForm()
        player_formset = PlayerFormset()
        if team:
            form.initial = {'name': team.name, 'school': team.school}
            player_formset.initial = []
            for player in player_list:
                player_formset.initial.append({'name': player.name,
                                               'grade': player.grade, 'birthday': player.birthday})

    return render(request, './team_details.html', {'form': form, 'team': team, 'player_list': player_list,
                                               'player_formset': player_formset})


def team_new(request):
    PlayerFormset = formset_factory(PlayerForm, min_num=6, max_num=6)
    if request.method == 'POST':
        form = TeamForm(request.POST)
        player_formset = PlayerFormset(request.POST)
        if form.is_valid() and player_formset.is_valid():
            team = form.save(commit=False)
            team.team_reg_id = get_team_reg_id()
            team = form.save()
            for i in range(len(player_formset)):
                player = (player_formset[i].save(commit=False))
                player.player_team = team
                player.player_reg_id = get_player_reg_id()
                player.save()
            if 'save_and_create_next' in form.data:
                return redirect('team_new')
            if 'save' in form.data:
                return redirect('team_details', team_id=team.id)
            return redirect('team_browser')
    else:
        form = TeamForm()
        player_formset = PlayerFormset()
    return render(request, './team_creation.html', {'form': form, 'player_formset': player_formset, 'reg_id': get_team_reg_id()})


def team_browser(request):
    team_list = Team.objects.order_by('team_reg_id')
    template = loader.get_template('team_browser.html')
    context = {
        'team_list': team_list,
    }
    return HttpResponse(template.render(context, request))


def game_conduction(request):
    return render(request, './game_conduction.html')


def overall_rating(requset):
    return render(requset, './overall_rating.html')


def get_player_reg_id():
    player_list = Player.objects.all()
    return len(player_list)


def get_team_reg_id():
    team_list = Team.objects.all()
    return len(team_list)
