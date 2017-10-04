from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting_info(models.Model):
    meet_title = models.CharField(max_length=20)
    meet_catagory = models.CharField(max_length=20)
    meet_time_start = models.DateTimeField()
    meet_time_end = models.DateTimeField()
    meet_dur_start = models.DateTimeField()
    meet_dur_end = models.DateTimeField()
    meet_place = models.CharField(max_length=100)
    meet_comment = models.TextField()
