from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User)

    user_location = models.CharField(max_length=50)
    user_job = models.CharField(max_length=50)
    user_website = models.CharField(max_length=50)


class UserSkills(models.Model):
    user = models.ForeignKey(User)

    user_skill = models.CharField(max_length=50)
    user_skill_point = models.IntegerField(default=0)
