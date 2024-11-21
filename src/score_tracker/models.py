from django.db import models
from django.contrib.auth.models import User
from user_management.models import SubProfile



class Activity(models.Model):
    """
    Représente une activité où un sous-profil peut obtenir un score.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Score(models.Model):
    """
    Représente le score d'un sous-profil sur une activité.
    """
    profile = models.ForeignKey(SubProfile, related_name='scores', on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, related_name='scores', on_delete=models.CASCADE)
    points = models.IntegerField()
    achieved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.name} - {self.activity.name}: {self.points}"
