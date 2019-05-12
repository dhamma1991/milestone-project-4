from django.db import models

class StatsModel(models.Model):
    total_xp_gain = models.IntegerField()
    total_levels_gain = models.IntegerField()
    stats_name = models.CharField(max_length = 10)