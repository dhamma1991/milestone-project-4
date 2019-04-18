from django.db import models

class UserLevel(models.Model):
    level_rank = models.IntegerField()
    xp_threshold = models.IntegerField(default = 100)
    
    def __str__(self):
        # Return how the class should be displayed
        return 'Level %s' % self.level_rank