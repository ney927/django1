from django.shortcuts import render
from .models import File

def files_view(request):
  files = File.objects.all()
  context ={
    'files': files
  }
  return render(request, 'files.html', context)
