'''
Utilities for shortener
'''
from django.conf import settings
from random import choice
from string import ascii_letters, digits


SIZE = getattr(settings, "MAX_URL_CHARS", 7) #try to get val from settings

AVAILABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAILABLE_CHARS):
	#creates random string with predetermined size
	return ''.join([choice(chars) for _ in range(SIZE)])

def create_shortened_url(model_instance):
	randomCode =create_random_code()

	model_class = model_instance.__class__
	if model_class.objects.filter(short_url=randomCode).exists():
		return create_shortned_url(model_instance)

	return randomCode

