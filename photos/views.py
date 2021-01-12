from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Image

def index(request):
	"""Render a homepage with a grid of images"""
	photos = Image.objects.all()
	return render(request, 'homepage.html', {"photos": photos})

def photo(request, photo_id):
	"""Render a photo with a specific image"""
	photo = Image.objects.get(id=photo_id)
	full_url = request.build_absolute_uri(photo.image.url)
	return render(request, 'photo.html', {"photo": photo, "full_url": full_url})