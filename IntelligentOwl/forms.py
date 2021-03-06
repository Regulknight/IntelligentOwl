from django.forms import ModelForm, forms, modelformset_factory, inlineformset_factory, models
from django import forms

from IntelligentOwl.models import Team, Player, Game


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'grade', 'birthday']


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'school']


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'tour_count', 'questions_count', 'game_coefficient']





