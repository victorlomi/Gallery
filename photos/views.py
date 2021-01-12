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

def search_results(request):
	#Search for a category or a location
    if 'tag' in request.GET and request.GET["tag"]:
        search_term = request.GET.get("tag")
        searched_categories = Image.search_image(search_term)
        message = f"{search_term}"
        # return render(request, 'all-news/photo.html',{"message":message,"articles": searched_articles})
        return HttpResponse(f"success {message}")
    else:
        message = "You haven't searched for any term"
        # return render(request, 'all-news/search.html',{"message":message})
        return HttpResponse(f"failed {message}")