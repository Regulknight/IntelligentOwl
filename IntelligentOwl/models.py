from django.db import models

# Create your models here.


class GameParticipant(models.Model):
    name = models.CharField(max_length=255)


class Player(GameParticipant):
    player_reg_id = models.IntegerField(unique=True)
    birthday = models.DateField(null=True)
    grade = models.IntegerField(null=True)
    player_team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.player_reg_id) + ") " + self.name


class Team(GameParticipant):
    team_reg_id = models.IntegerField()
    school = models.CharField(max_length=255, default="")
    league = models.CharField(max_length=255)
    captain = models.OneToOneField(Player, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.team_reg_id) + ") " + self.name


class Tour(models.Model):
    order_number = models.IntegerField()
    questions_count = models.IntegerField()
    game = models.ForeignKey('Game', on_delete=models.CASCADE)


class Game(models.Model):
    name = models.CharField(max_length=255)
    tour_count = models.IntegerField()
    questions_count = models.IntegerField()
    game_coefficient = models.FloatField()
    participants = models.ManyToManyField(GameParticipant)

    def __str__(self):
        return self.name


class TourEntry(models.Model):
    participant = models.ForeignKey(GameParticipant, on_delete=models.CASCADE)


class Question(models.Model):
    value = models.FloatField(null=True)
    rating = models.IntegerField(null=True)
    order_number = models.IntegerField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)


class QuestionResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tour_entry = models.ForeignKey(TourEntry, on_delete=models.CASCADE)
    isCorrect = models.BooleanField()
