from django.db import models
from django.contrib.auth.models import User

class WordList(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='word_lists', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Word(models.Model):
    word = models.CharField(max_length=50)
    word_list = models.ForeignKey(
        WordList, related_name='words', on_delete=models.CASCADE
        )

    def __str__(self):
        return self.word
    
class Letter(models.Model):
    letter = models.CharField(max_length=1)
    word = models.ForeignKey(Word, related_name='letters', on_delete=models.CASCADE)

    def __str__(self):
        return self.letter
