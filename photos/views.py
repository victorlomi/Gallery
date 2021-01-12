from django.shortcuts import render
from django.http import HttpResponse

from .models import Image

def index(request):
	"""Render a homepage with a grid of images"""
	photos = Image.objects.all()
	return render(request, 'homepage.html', {"photos": photos})

def photo(request, photo_id):
	"""Render a photo with a specific image"""
	photo = Image.objects.get(id=photo_id)
	return render(request, 'photo.html', {"photo": photo})