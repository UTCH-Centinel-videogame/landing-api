from django.db import models

# Create your models here.

class Vote(models.Model):
    gameplay = models.IntegerField()
    music = models.IntegerField()
    art = models.IntegerField()
    story = models.IntegerField()
    difficulty = models.IntegerField()