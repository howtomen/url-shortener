'''
URL shortner model
'''

from django.db import models
from .utils import create_shortened_url

# Create your models here.
class Shortener (models.Model):
	#in here we weill create a short URL based on the long one
	created = models.DateTimeField(auto_now_add = True) #hour and date shortener was created
	times_hit = models.PositiveIntegerField(default=0) #times the short link was followed
	long_url = models.URLField() #the original url
	short_url = models.CharField(max_length=15,unique=True, blank=True) #shortened link https://domain/(short_url)

	class Meta:
		ordering = ["-created"]

	def __str__(self):

		return f'{self.long_url} to {self.short_url}'

	def save(self, *args, **kwargs):

		if not self.short_url:
			self.short_url = create_shortened_url(self) #pass model instance being saved 
		super().save(*args, **kwargs)


