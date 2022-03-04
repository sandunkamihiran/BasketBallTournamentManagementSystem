from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class Team(models.Model):
    name = models.CharField(max_length=100)
    average_score = models.FloatField()

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=50)

    age = models.IntegerField()
    number_of_games_played = models.IntegerField()
    penalty_count = models.IntegerField()

    height = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    average_score = models.FloatField()

    is_team_captain = models.BooleanField()
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Round(models.Model):
    round_no = models.IntegerField()
    round_code = models.CharField(max_length=10)
    round_name = models.CharField(max_length=50)

    def __str__(self):
        return self.round_code


class Match(models.Model):
    match_no = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=50)

    round = models.ForeignKey(Round, on_delete=models.RESTRICT)
    host_team = models.ForeignKey(Team, on_delete=models.RESTRICT, related_name='host_team')
    guest_team = models.ForeignKey(Team, on_delete=models.RESTRICT, related_name='guest_team')
    winner_team = models.ForeignKey(Team, on_delete=models.RESTRICT, related_name='winner_team')

    host_team_final_score = models.IntegerField()
    guest_team_final_score = models.IntegerField()

    def __str__(self):
        return self.match_no


class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['groups_id', 'email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username
