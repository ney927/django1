from django.shortcuts import render
from .models import Profile, Pins
from Files.models import File

def profile_view(request):
  pins = Pins.objects.all()
  context = {
    'pins': pins
  }
  return render(request, 'profile.html', context)

def pin_item_view(request, id):
  f = File.objects.get(id=id)
  u = Profile.objects.get(user = request.user)
  # allPins = Pins.objects.filter(prof=u, pin=f.file)
  p = Pins(prof=u, pin=f.file)
  p.save()
  context = {
    'file': f
  }
  return render(request, 'profile.html', context)
