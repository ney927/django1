from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Pins(models.Model):
  prof = models.ForeignKey(Profile, on_delete=models.CASCADE)
  pin = models.FileField(upload_to="media")
