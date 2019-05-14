from django.db import models

class StatsModel(models.Model):
    total_xp_gain = models.IntegerField(default = 0)
    total_levels_gain = models.IntegerField(default = 0)
    stats_name = models.CharField(max_length = 10)