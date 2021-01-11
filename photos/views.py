from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	"""Render a homepage with a grid of images"""
	return render(request, 'homepage.html')

def photo(request, photo_id):
	"""Render a photo with a specific image"""
	return HttpResponse("showing a photo")