from django.db import models

class UserLevel(models.Model):
    level_rank = models.IntegerField()
    xp_threshold = models.IntegerField(default = 100)
    
    def __str__(self):
        # Return how the class should be displayed
        return 'Level %s' % self.level_rank
        

# # # The below commented-out line was used in the Django shell to populate the
# # # UserLevel database with levels and xp_threshold values
# # # Kept here for reference
# UserLevel.objects.bulk_create([UserLevel(level_rank = level, xp_threshold = level * 100) for level in range(1, 101)])