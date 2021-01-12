from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=60)
    
class Category(models.Model):
	name = models.CharField(max_length=60)

class Image(models.Model):
	image = models.ImageField(upload_to="photos/")
	name = models.CharField(max_length=60)
	description = models.TextField()
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)