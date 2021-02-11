from django.shortcuts import render
from .models import Profile, Pins
from Files.models import File

def profile_view(request):
  pins = Pins.objects.all()
  profs = Profile.objects.all()
  context = {
    'pins': pins,
    'profiles': profs
  }
  return render(request, 'profile.html', context)

def pin_item_view(request, id):
  f = File.objects.get(id=id)
  u = Profile.objects.get(user = request.user)
  allPins = Pins.objects.filter(prof=u, pin=f)
  if not allPins.exists():
    p = Pins(prof=u, pin=f)
    p.save()
  else:
    print("DUPLICATE, NOT SAVED")
    print(allPins)
  pins = Pins.objects.all()
  profs = Profile.objects.all()
  context = {
    'pins': pins,
    'profiles': profs
  }
  # context = {
  #   'file': f
  # }
  return render(request, 'profile.html', context)

def delete_pin_view(request, id):
  p = Pins.objects.get(id=id)
  p.delete()
  pins = Pins.objects.all()
  profs = Profile.objects.all()
  context = {
    'pins': pins,
    'profiles': profs
  }
  return render(request, 'profile.html', context)
