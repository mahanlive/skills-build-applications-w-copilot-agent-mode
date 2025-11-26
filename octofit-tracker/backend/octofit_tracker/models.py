
from django.db import models
from djongo import models as djongo_models
from bson import ObjectId


class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    date = models.DateField()

    def __str__(self):
        return f"{self.type} by {self.user.name} on {self.date}"


class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField(User, related_name='workouts', blank=True)

    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - {self.points} points"
