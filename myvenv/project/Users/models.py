from django.db import models
from django.contrib.auth.models import User
from Files.models import File

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

class Pins(models.Model):
  prof = models.ForeignKey(Profile, on_delete=models.CASCADE)
  pin = models.ForeignKey(File, on_delete=models.CASCADE)
