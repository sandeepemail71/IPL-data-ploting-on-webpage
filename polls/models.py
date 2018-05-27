from django.db import models

# Create your models here.


class Matches(models.Model):
    toss_decision = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    umpire2 = models.CharField(max_length=200)
    toss_winner = models.CharField(max_length=200)
    match_id = models.CharField(max_length=200)
    umpire1 = models.CharField(max_length=200)
    player_of_match = models.CharField(max_length=200)
    team1 = models.CharField(max_length=200)
    season = models.CharField(max_length=200)
    umpire3 = models.CharField(max_length=200)
    win_by_wickets = models.CharField(max_length=200)
    dl_applied = models.CharField(max_length=200)
    team2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    win_by_runs = models.CharField(max_length=200)
    winner = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)


class Deliveries(models.Model):
    is_super_over = models.CharField(max_length=200)
    noball_runs = models.CharField(max_length=200)
    ball = models.CharField(max_length=200)
    bye_runs = models.CharField(max_length=200)
    legbye_runs = models.CharField(max_length=200)
    inning = models.CharField(max_length=200)
    total_runs = models.CharField(max_length=200)
    match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)
    penalty_runs = models.CharField(max_length=200)
    extra_runs = models.CharField(max_length=200)
    over = models.CharField(max_length=200)
    fielder = models.CharField(max_length=200)
    batting_team = models.CharField(max_length=200)
    bowling_team = models.CharField(max_length=200)
    dismissal_kind = models.CharField(max_length=200)
    player_dismissed = models.CharField(max_length=200)
    non_striker = models.CharField(max_length=200)
    bowler = models.CharField(max_length=200)
    batsman_runs = models.CharField(max_length=200)
    batsman = models.CharField(max_length=200)
    wide_runs = models.CharField(max_length=200)

