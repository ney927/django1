from django.db import models
# import django.contrib.postgres.fields
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class File(models.Model):
  file = models.FileField()
