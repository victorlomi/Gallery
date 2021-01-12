from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

	def save_location(self, *args, **kwargs):
		self.save(*args, **kwargs) 

	def update_location(self, name):
		self.name = name

	def delete_location(self):
		self.delete()
    
class Category(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

	def save_category(self, *args, **kwargs):
		self.save(*args, **kwargs) 

	def update_category(self, name):
		self.name = name

	def delete_category(self):
		self.delete()

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

	@classmethod
	def filter_by_location(cls, location):
		location_images = cls.objects.filter(location__name__icontains=location)
		return location_images

	def save_image(self):
		self.save()

	def delete_image(self):
		self.delete()

	def update_image(self, img):
		self.image = img.image
		self.name = img.name
		self.description = img.description
		self.location = img.location
		self.category = img.category
	
	@classmethod 
	def get_image_by_id(cls, id):
		return cls.objects.get(id=id)

