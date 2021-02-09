from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, )
  pins = ArrayField(models.FileField(), blank = True)

class File(models.Model):
  file = models.FileField()
  tags = ArrayField(models.CharField(max_length=200), blank=True)
