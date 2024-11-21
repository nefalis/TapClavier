from django.db import models
from django.contrib.auth.models import User


class SubProfile(models.Model):
    """
    Modèle pour les sous-profils associés à un utilisateur.
    """
    user = models.ForeignKey(User, related_name='sub_profiles', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    progress = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} (sous profil de {self.user.username})"