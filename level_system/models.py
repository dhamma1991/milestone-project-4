from django.db import models

# # # The below commented-out line was used in the Django shell to populate the
# # # UserLevel database with levels and xp_threshold values
# # # Kept here for reference
# UserLevel.objects.bulk_create([UserLevel(level_rank = level, xp_threshold = level * 100) for level in range(1, 101)])