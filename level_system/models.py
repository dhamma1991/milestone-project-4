from django.db import models

class UserLevel(models.Model):
    level_rank = models.IntegerField()
    xp_threshold = models.IntegerField()
