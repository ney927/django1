from django.shortcuts import render
from .models import Profile, Pins

def profile_view(request):
  pins = Pins.objects.all()
  context = {
    'pins': pins
  }
  return render(request, 'profile.html', context)
