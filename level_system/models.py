from django.db import models

class UserLevelSystem(models.Model):
    level_rank = models.IntegerField()
    xp_threshold = models.IntegerField()
