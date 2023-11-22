from django.db import models

# Create your models here.
class NavItems(models.Model):
    nav_name = models.CharField(max_length=30)
    nav_link = models.CharField(max_length=50)
    nav_id   = models.PositiveIntegerField()

class AdvantageTileItems(models.Model):
    adv_title_up   = models.CharField(max_length=50)
    adv_main       = models.CharField(max_length=4)
    adv_title_down = models.CharField(max_length=50)