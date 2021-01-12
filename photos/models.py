from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name
    
class Category(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Image(models.Model):
	image = models.ImageField(upload_to="photos/")
	name = models.CharField(max_length=60)
	description = models.TextField()
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	
		
	def __str__(self):
		return self.name

	@classmethod
	def search_image(cls, category): 
		category_images = cls.objects.filter(category__name__icontains=category)
		return category_images

